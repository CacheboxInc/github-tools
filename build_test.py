# python3 -m pip install PyGithub
# docker build -t pygit pygithub/
# docker run --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit bash
# docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit python build_test.py
# curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz

from github import Github

g = Github("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")
for repo in g.get_user().get_repos():
   if repo.name == "hyc":
        break;
else:
        repo = None

#get_rel = repo.get_latest_release()


rel_list = repo.get_releases()
latest = rel_list[0]
for rel in rel_list:
    if rel.created_at > latest.created_at:
        latest = rel

print(latest.tag_name)
