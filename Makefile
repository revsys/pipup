.PHONY: version

include .version

version:
    bumpversion patch
    git push
    git push --tags