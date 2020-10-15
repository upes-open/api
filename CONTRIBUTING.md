
# CONTRIBUTING

### Contributing Guidelines!

 Read this space to know the contributing guidelines. Please follow the guidelines for smooth contribution. Following the guidelines reflect your courtesy towards the open source contribution. The issues, potential changes and pull requests will be addressed in compliance with the quality of need and urgency.  

### Expected Contribution:
In case you are willing to contribute in any form, You're most Welcome! Improvement in documentation, reporting bugs and mistakes is expected in general.

# Getting started

## Ground Rules
Issues should be created to submit a change to the repository before opening a pull request. Communication in any form except the repository channels is not expected and will not be entertained.

## How to Contribute:

1. Fork the repository to your own GitHub account.

2. Clone the repository to your local machine
```
$ git clone "https://www.github.com/{Username}/{Repository}"
```
where username is your GitHub account username.

3. Create a branch where you can do your local work.
Never work on **master** branch.
```
$ git branch {branchname}
$ git checkout branchname
```

4. Add your work and stage your changes.
```
$ git add <filename>
```

5. Commit you changes with a commit message containing your name, file(s) worked upon, changes added.
```
$ git commit -m "Name| files| Changes"
```

6. Push changes to your forked repository
```
$ git push -u origin branchname
```
7. Create a pull request to the upstream repository.

# Synchronize forked repository with Upstream repository

1. Create upstream as our repository
```
$ git remote add upstream {Repository Link}
```

2. Fetch upstream changes in local machine
```
$ git fetch upstream
```

3. Switch to master branch
```
$ git checkout master
```

4. Merge changes in local machine
```
$ git merge upstream/master
```

5. Push changes to your forked GitHub repository
```
$ git push -f origin master
```
