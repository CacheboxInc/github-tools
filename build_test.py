# python3 -m pip install PyGithub
# docker build -t pygit pygithub/
# docker run --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit python build_test.py
# curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz

from github import Github
import sys
import argparse

parser = argparse.ArgumentParser(description="""Helper utility to manage git release and binaries associated with a release.
The output is intended for use directly into the jenkins script. Hence the output is short so that
we can script it.""")
# full link of https://bit.ly/3xOGgV1 is https://docs.google.com/document/d/1x8RFJMDIj6AGah9vrPshmz-eeTcZoP_Fg8alhH8rg_U/edit#heading=h.wocagyekg2yq
parser.add_argument('-a', required = True, dest = 'auth', help='Auth token for github access. The steps are documented here https://bit.ly/3xOGgV1')
parser.add_argument('-r', required = True, dest = 'repo', help='Git repository on when we need to operate.')
parser.add_argument('-f', required = True, dest = 'file',help='Name of asset/file which we want to operate on.')
parser.add_argument('operation', choices = ["download", "upload"], help='Operation to perfrom download/upload asset file.')
args = parser.parse_args()

token=args.auth
get_repo=args.repo
file_asset = args.file
operation = args.operation

g = Github(token)
for repo in g.get_user().get_repos():
   if repo.name == get_repo:
        break;
else:
        repo = None

rel_list = repo.get_releases()
latest = rel_list[0]
for rel in rel_list:
    if rel.created_at > latest.created_at:
        latest = rel

if operation.lower() == "download":
    for asset in latest.get_assets():
        if asset.name == file_asset:
            print(asset.url)
    