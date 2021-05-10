# python3 -m pip install PyGithub
# docker build -t pygit pygithub/
# docker run --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit python build_test.py
# curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz

from github import Github
import sys
import argparse
import json
import pprint

class gitTools:
    "Misc tools to manipulate github"
    def __init__(self, token):
        self.token = token
        self.github = Github(token)
        self.repo_list = self.github.get_user().get_repos()

    def get_repo(self, name):
        for repo in self.repo_list:
            if repo.name == name:
                return repo
        return None

    def get_latest_release(self, repo):
        rel_list = repo.get_releases()
        latest = rel_list[0]
        for rel in rel_list:
            if rel.created_at > latest.created_at:
                latest = rel
        return latest
    
    def get_asset_url(self, release, asset_name):
        for asset in release.get_assets():
            if asset.name == asset_name:
                return asset.url
        assert False , "No such asset"

    def get_latest_rel_url(self, repo_name, asset_name):
        repo = self.get_repo(repo_name)
        rel = self.get_latest_release(repo)
        return self.get_asset_url(rel, asset_name)


parser = argparse.ArgumentParser(description="""Helper utility to manage git release and binaries associated with a release.
The output is intended for use directly into the jenkins script. Hence the output is short so that
we can script it.""")
# full link of https://bit.ly/3xOGgV1 is https://docs.google.com/document/d/1x8RFJMDIj6AGah9vrPshmz-eeTcZoP_Fg8alhH8rg_U/edit#heading=h.wocagyekg2yq
parser.add_argument('-a', required = True, dest = 'auth', help='Auth token for github access. The steps are documented here https://bit.ly/3xOGgV1')
parser.add_argument('-r', required = True, dest = 'repo', help='Git repository on when we need to operate.')
parser.add_argument('-f', required = True, dest = 'file',help='Name of asset/file which we want to operate on.')
parser.add_argument('operation', choices = ["download", "upload", "json"], help='Operation to perfrom download/upload asset file. In json we provide a json file with list of repositories and files')
args = parser.parse_args()

token=args.auth
get_repo=args.repo
operation = args.operation
file_asset = args.file

g = gitTools(token)

if operation.lower() == "download":
    url = g.get_latest_rel_url(get_repo, file_asset)
    print(url)

if operation.lower() == "json":
    with open(file_asset,'r',encoding = 'utf-8') as f:
        json_data = json.load(f)
        for repo in json_data:
            for asset in json_data[repo]:
                url = g.get_latest_rel_url(repo, asset)
                print(url)
