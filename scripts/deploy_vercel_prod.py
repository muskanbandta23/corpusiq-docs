#!/usr/bin/env python3
"""Deploy corpusiq-docs site/ to Vercel production (docs.corpusiq.io).

Prebuilt mode: site/ is the final static output (MkDocs builds locally).
vercel.json is copied into site/ so the production redirects and
outputDirectory settings travel with the deployment.
"""
import json
import os
import shutil
import subprocess
import sys

REPO = '/home/hermes/corpusiq-docs'
SECRETS = '/home/hermes/.hermes/profiles/corpusiq/secrets/vercel.json'
TEAM_ID = 'team_btwsQPaxGRECjJjdKQOMcMUQ'

def main():
    with open(SECRETS) as f:
        creds = json.load(f)
    tok = creds.get('token', '')
    if not tok:
        print('ERROR: no token')
        sys.exit(1)
    shutil.copy(os.path.join(REPO, 'vercel.json'), os.path.join(REPO, 'site', 'vercel.json'))
    env = dict(os.environ)
    env['VERCEL_PROJECT_ID'] = creds.get('docs_project_id', '')
    env['VERCEL_ORG_ID'] = TEAM_ID
    cmd = ['npx', '--yes', 'vercel@latest', 'deploy', 'site',
           '--yes', '--prod', '--token', tok, '--scope', TEAM_ID]
    print('Running: npx vercel deploy site --prod (vercel.json inside site/)')
    proc = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True, text=True, timeout=600)
    print(proc.stdout[-3000:])
    print(proc.stderr[-1500:])
    sys.exit(proc.returncode)

if __name__ == '__main__':
    main()
