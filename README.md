# Marcel Broccoli

Marcel's broccoli module for simplifying his coding.


## Module

### Structure

```
-Marcel
 |-functions            Custom functions
   |-starts_with        Check if string starts with pattern (case sensitive or case insensitive)
   |-str2datetime       Convert from all date and date time sources to date object
   |-datetime2str       Convert date to string in HomeBank format
 |-logger               Custom logging
   |-mylogger           Logger object
   |-setup              Setup custom logger
   |-log                Write log entry
```


## Manage Releases

Default branch is `dev` for development and updates of module.

Example for release 1.0.0.
```bash
# Create and checkout a new "release" branch.
git checkout -b release-1.0.0 dev
# Finalize code and update version in setup.py
# Merge final version of release into `dev` and `main`.
git checkout main
git merge release-1.0.0
git push
git checkout dev
git merge release-1.0.0
git push
# Delete branch release-1.0.0
git branch -d release-1.0.0
# Create and push tag to main branch
git tag -a 1.0.0 -m "first release" main
git push --tags
git push
```

Create a new release on GitHub with the created tag.


## Use Release in pip

1. Jump to the release page of the repository on GitHub.
1. Copy the tar.gz link of the release.
1. use the link for `pip install`.

```bash
pip install https://github.com/chemage/marcelbroccoli/archive/refs/tags/1.0.0.tar.gz
```
