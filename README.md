# Smalr.io  -- VERY ROUGH DRAFT OF README#

Django based secure link shortening service. To be hosted on the cloud (which server is to be determined)

### Code ###
Relevant code is stored in this repository which is setup as a standard Django project!

### How do I get set up? ###
If added to the project, new user should clone this repository and use the following git workflow.

1. Create your own local branch via. `git checkout -b feature`
2. Add your code to the new branch (rebase from master) `git rebase master`
3. Commit code to your new branch
4. Checkout master branch and pull most recent changes from server with `git pull origin master`
5. Merge the branch you were working on into main via `git merge branch`
6. If all works well you can push the changes to our sever repo: `git push`

**NOTE:**  Make sure your code is clean and well documented! Remember to supply useful commit messages that include what you changed/added and why you did so! I recommend not supplying -m flag to commit so you can write you messages in your text editor!

### Contribution guidelines ###
* Be sure to write tests
* Code review
* Document your code in a clear meaningful manner this includes comments and updating the header comment found 
at the beginning of all the code files. Namely it means updating who edited the file last and the date and time they did so as
well as the TODO specific to the code file.

### Who do I talk to? ###
* Joey DeFrancesco - jdefr89@gmail.com
* Other team members!