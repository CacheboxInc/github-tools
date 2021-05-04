# Tools for HDM build

```
python3 -m pip install PyGithub
docker build -t pygit pygithub/
docker run --rm -it pygit bash
docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit bash
docker run -v /Users/mitra/VM-REMOTE/primary-io/git-test/:/app --rm -it pygit python build_test.py
docker run -v `pwd`/github-tools:/app --rm -it pygit python build_test.py
docker run -v `pwd`/github-tools:/app --rm -it pygit ls -l
curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz
curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token ' -X GET  https://api.github.com/repos/CacheboxInc/hyc-ha/releases/assets/36081908  --output /tmp/pygit.tar.gz
docker run -v /Users/mitra/VM-REMOTE/primary-io/github-tools/:/app --rm -it pygit python build_test.py <token> hyc-ha download
```

echo FAST BUILD placeholder
curl -L -H 'Accept: application/octet-stream'   -H 'Authorization: token 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' -X GET  https://api.github.com/repos/CacheboxInc/hyc/releases/assets/36295389 --output /tmp/pygit.tar.gz
docker load -i /tmp/pygit.tar.gz

git clone https://github.com/CacheboxInc/github-tools.git

docker run -v `pwd`/github-tools:/app --rm -it pygit ls -l

exit 1

