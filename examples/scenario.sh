# first commit
PYTEST_UPDATE_REFS=1 pytest  # run all tests
git add tests/dumps/*txt
git commit -m "added test dumps"
git push


# later commits
...update the code...

pytest  # run all tests
...inspect differences in failed tests...
# once differences are considered valid
PYTEST_UPDATE_REFS=1 pytest
git add tests/dumps/*txt

...commit and push...
