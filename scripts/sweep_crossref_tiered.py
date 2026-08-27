#!/usr/bin/env python3
"""Tiered skills.sh sweep cross-reference (verified Aug 21 evening, 2026).

Runs the standard 15 skills.sh API queries, dedupes, and cross-references each
skill against the docs tree in three tiers:
  name hit in hermes/skills/           -> covered (skip)
  repo hit in hermes/skills/           -> PARTIAL (repo documented, skill name missing)
  repo hit anywhere in corpusiq-docs   -> ecosystem-covered (distribution docs)
  otherwise                            -> NEW

Output: NEW and PARTIAL grouped by source with install counts, plus a DECISION
line. PARTIAL entries >=100 installs are the candidates for the Aug 21
discrete-guide rule — verify each by fetching default_branch + git tree
SKILL.md path + raw.githubusercontent content before drafting.

Usage:  cd ~/corpusiq-docs && python3 scripts/sweep_crossref_tiered.py
"""
import json
import os
import subprocess
import urllib.parse
import urllib.request

DOCS_SKILLS = os.path.expanduser('~/corpusiq-docs/hermes/skills/')
DOCS_ROOT = os.path.expanduser('~/corpusiq-docs/')

QUERIES = [
    ('nousresearch/hermes-agent', 96), ('aradotso/hermes-skills', 96),
    ('hermes', 50), ('hermes agent', 50), ('hermes skill', 50),
    ('hermes automation', 50), ('hermes agent new', 50),
    ('garrytan/gbrain', 50), ('plastic-labs/honcho', 50),
    ('aradotso/devtools-skills', 50), ('sickn33/antigravity-awesome-skills', 50),
    ('kcchien/clawpilot', 50), ('rethinking-studio/clawpilot-skills', 50),
    ('varnan-tech/opendirectory', 96), ('cosmicstack-labs/mercury-agent-skills', 50),
]
SKIP_SOURCES = {'facebook/hermes'}


def rg_hits(pattern, path):
    """True if any file under path matches pattern (fixed-string, case-insensitive)."""
    try:
        r = subprocess.run(['rg', '-li', '-F', '--', pattern, path],
                           capture_output=True, text=True, timeout=20)
        return bool(r.stdout.strip())
    except Exception:
        try:
            r = subprocess.run(['grep', '-rli', '--', pattern, path],
                               capture_output=True, text=True, timeout=20)
            return bool(r.stdout.strip())
        except Exception:
            return False


def main():
    skills = {}
    for q, limit in QUERIES:
        url = 'https://skills.sh/api/search?q=' + urllib.parse.quote(q) + f'&limit={limit}'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Hermes sweep)'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode())
            for s in data.get('skills', []):
                src = (s.get('source') or '').strip()
                name = (s.get('name') or '').strip()
                if src in SKIP_SOURCES or not name:
                    continue
                skills.setdefault(f'{src}|{name}',
                                  {'source': src, 'name': name,
                                   'installs': int(s.get('installs', 0) or 0)})
        except Exception as e:
            print(f'QUERY ERROR {q}: {e}')

    new_list, partial_list = [], []
    for s in skills.values():
        if rg_hits(s['name'], DOCS_SKILLS):
            continue
        if rg_hits(s['source'], DOCS_SKILLS):
            partial_list.append(s)
            continue
        if rg_hits(s['source'], DOCS_ROOT):
            continue
        new_list.append(s)
    new_list.sort(key=lambda x: -x['installs'])
    partial_list.sort(key=lambda x: -x['installs'])

    print(f'UNIQUE: {len(skills)} | NEW: {len(new_list)} | PARTIAL: {len(partial_list)}')

    print('\n=== NEW grouped by source (top installs first, max 8/source) ===')
    by_src = {}
    for s in new_list:
        by_src.setdefault(s['source'], []).append(s)
    for src, items in by_src.items():
        items.sort(key=lambda x: -x['installs'])
        for s in items[:8]:
            print(f"NEW | {s['source']} | {s['name']} | {s['installs']}")

    print('\n=== PARTIAL >=100 installs (Aug 21 discrete-guide rule candidates) ===')
    for s in [x for x in partial_list if x['installs'] >= 100][:40]:
        print(f"PARTIAL | {s['source']} | {s['name']} | {s['installs']}")

    high_new = [s for s in new_list if s['installs'] >= 100]
    high_partial = [s for s in partial_list if s['installs'] >= 100]
    if high_new or high_partial:
        print(f'\nDECISION: REPORT — {len(high_new)} new + {len(high_partial)} partial >=100 installs')
    elif len(new_list) >= 5:
        print(f'\nDECISION: CHECK RELEVANCE — {len(new_list)} new, all <100 installs')
    else:
        print(f'\nDECISION: [SILENT] — {len(new_list)} new, all niche')


if __name__ == '__main__':
    main()
