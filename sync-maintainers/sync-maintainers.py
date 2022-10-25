#!/usr/bin/env python3
import requests
import json
import subprocess
import os
import sys
import argparse

def parse(m):
    para = []
    repos = []
    while len(m):
        line = m.pop(0)
        if line == '# Maintainers':
            line = m.pop(0)
            while not line.startswith('#'):
                para.append(line)
                line = m.pop(0)
        if line.startswith('###'):
            repo = line.split('### ')[1].strip()
            maint = []
            m.pop(0) # maintainers:
            line = m.pop(0)
            while line.startswith('* '):
                maint.append(line)
                line = m.pop(0) if len(m) else ''
            if repo != 'Flatcar':
                repos.append((repo, maint))
    return para, repos

MAINTAINERS_TEMPLATE = '''# Maintainers

{maintainers}

{paragraph}

The contents of this file are synchronized from [Flatcar/MAINTAINERS.md](https://github.com/flatcar-linux/Flatcar/blob/main/MAINTAINERS.md).
'''

def write_maintainers_file(repo_name, paragraph, maintainers):
    maintainers_entry = '\n'.join(maintainers)
    maintainers_content = MAINTAINERS_TEMPLATE.format(maintainers=maintainers_entry, paragraph=paragraph)
    repo_filename = '{}/MAINTAINERS.md'.format(repo_name)
    with open(repo_filename, 'w') as f:
        f.write(maintainers_content)

BRANCH_NAME = 'sync-maintainers'
def checkout_branch(repo_name):
    return subprocess.run(['git', '-C', repo_name, 'checkout', '-B', BRANCH_NAME, 'origin/HEAD'], check=True)

def commit(repo_name):
    subprocess.run(['git', '-C', repo_name, 'add', 'MAINTAINERS.md'], check=True)
    subprocess.run(['git', '-C', repo_name, 'commit', '-m', 'Sync maintainers file from flatcar/flatcar repository'], check=True)

def push(repo_name):
    subprocess.run(['git', '-C', repo_name, 'push', '--force', 'origin', BRANCH_NAME], check=True)

def parse_maintainers(repo=None):
    maint_file = '../MAINTAINERS.md'
    with open(maint_file) as f:
    	m = f.read().splitlines()
    para, repos = parse(m)
    paragraph = '\n'.join(para).strip()
    if repo:
        repos = [r for r in repos if r[0] == repo]
    return repos, paragraph

def main_repo(args):
    repos, paragraph = parse_maintainers(args.repo)
    for (repo_name, maintainers) in repos:
        repo_url = 'git@github.com:flatcar/{}'.format(repo_name)
        subprocess.run(['git','clone','--depth=1', repo_url])
        checkout_branch(repo_name)
        write_maintainers_file(repo_name, paragraph, maintainers)
        commit(repo_name)
        push(repo_name)


def prepare_req(repo, token, api):
    url = 'https://api.github.com/repos/flatcar/{}{}'.format(repo, '/' + api if api else '')
    headers = {'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {}'.format(token)
    }
    return url, headers
    
def get_pr(repo, token):
    url, headers = prepare_req(repo, token, 'pulls')
    params = {'state': 'open', 'head': 'flatcar:{}'.format(BRANCH_NAME)}
    return requests.get(url, headers=headers, params=params)

def get_default_branch(repo, token):
    url, headers = prepare_req(repo, token, '')
    resp = requests.get(url, headers=headers).json()
    return resp['default_branch']

def create_pr(repo, token, base):
    url, headers = prepare_req(repo, token, 'pulls')
    data = {'title': 'Sync MAINTAINERS.md', 'head': 'flatcar:{}'.format(BRANCH_NAME), 'base': base}
    return requests.post(url, headers=headers, json=data)

def update_assignees(repo, token, pr, assignees):
    url, headers = prepare_req(repo, token, 'pulls/{}/requested_reviewers'.format(pr))
    data = {'reviewers': assignees}
    return requests.post(url, headers=headers, json=data)

def get_assignees(maintainers):
    assignees = [e.split('@')[1]  for e in maintainers]
    return assignees
def main_github(args):
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise Exception('Missing GITHUB_TOKEN env variable')
    repos, _ = parse_maintainers(args.repo)
    for (repo_name, maintainers) in repos:
        pr = get_pr(repo_name, token).json()
        if not pr:
            print('{} creating pr'.format(repo_name))
            base = get_default_branch(repo_name, token)
            pr = create_pr(repo_name, token, base).json()
            pr = [pr]
        prnum = pr[0]['number']
        assignees = get_assignees(maintainers)
        resp = update_assignees(repo_name, token, prnum, assignees)
        if resp.status_code != 201:
            print(resp.json())
        else:
            print('{} ok'.format(repo_name))

def main_list(args):
    repos, _ = parse_maintainers()
    for (repo_name, _) in repos:
        print(repo_name)

parser = argparse.ArgumentParser(prog='sync-maintainers.py')
subparser = parser.add_subparsers(required=True, dest='cmd')
parser_repo = subparser.add_parser('repo', help='perform git repository operations')
parser_repo.add_argument('--repo', help='Repository to operate on; default all')
parser_repo.set_defaults(func=main_repo)
parser_github = subparser.add_parser('github', help='perform github pull request operations')
parser_github.add_argument('--repo', help='Repository to operate on; default all')
parser_github.set_defaults(func=main_github)
parser_list = subparser.add_parser('list', help='list all repositories with entries')
parser_list.set_defaults(func=main_list)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
    #main()
