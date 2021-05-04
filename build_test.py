# python3 -m pip install PyGithub
# docker build -t pygit pygithub/
# docker run --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit python build_test.py
# curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz

from github import Github
import sys

#print('Token is ', sys.argv[1])
#print('Repo ', sys.argv[2])
token=sys.argv[1]
get_repo=sys.argv[2]
operation =sys.argv[3]

g = Github(token)
for repo in g.get_user().get_repos():
   if repo.name == get_repo:
        break;
else:
        repo = None

#get_rel = repo.get_latest_release()


rel_list = repo.get_releases()
latest = rel_list[0]
for rel in rel_list:
    if rel.created_at > latest.created_at:
        latest = rel

if operation.lower() == "download":
    assert len(list(rel.get_assets())) == 1
    asset = rel.get_assets()[0]
    print(asset.url)