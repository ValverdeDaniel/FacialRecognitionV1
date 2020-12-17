# FacialRecognitionV1

##if you would like to go the terminal route here is the comprehensive Danny Walkthrough for PC Users
#most of the commands should be the same for mac people especially if the command starts with git

#you can download git bash here
https://git-scm.com/downloads

#When you get to the pushing main branch portion im pretty sure that it will require that you have connected your git bash terminal to your github account... i remember that once i tried doing my first pull or push it gave me some error message and asked me to login. There's also connecting using SSH but if you can just do the login portion it's definitely easier.

#the lines with the $ contain the commands you type. type the commands without the $

### THE GETTING STARTED and maneuvering directories PORTION
#this command should take you to your desktop directory

$ cd ~/desktop

#this command shows you the different directories and files that you currently have access to

$ ls

#creates a folder on your desktop labeled WinterGroupProject2020

$ mkdir WinterGroupProject2020

#moves you to the directory WinterGroupProject2020... if you press tab once you've started typing it auto-fills in the rest of the word

$ cd WinterGroupProject2020

#this command will make a version of the github repository... you can find the link

$ git clone https://github.com/ValverdeDaniel/FacialRecognitionV1.git

#move into the directory FacialRecognitionV1

$cd FacialRecognitionv1

#move backwards one directory

$ cd ../

#move back into facial recognition directory

$cd FacialRecognitionv1

#inspect directory

$ ls

# THE PUSHING TO MAIN BRANCH PORTION

#pulls all updates to your directory... good practice to do this before making any updates
$ git pull

#open up the directory of FacialRecognitionV1 in pycharm and open the readme.md file
#write something down on the file and save it

#back in the git bash terminal type and it should mention some modifications
$ git status

#the following series of commands will push your changes to git hub as long as you are a collaborator and have connected your git bash terminal to your github account

#stages all of your updates

$git add .

$ git status

#prepares your updates so that all the added updates are ready to be pushed... the stuff in "" is a message to yourself and the group summarizing what you have done it's good for keeping tabs

$git commit -m "my tests"
 
#pushes all of your committed changes to the branch you specified

$git push origin main


# THE BRANCHING PORTION OF THE TUTORIAL
#this creates a new branch

$git checkout -b "myNameBranch"

# Pulling is good practice and one should almost always pull the contents from main to your branch in order to keep your branch up to date before doing work on your branch. when in doubt git PULL

$git pull


#This makes it so that when ever you do git pull you pull the contents from the main branch

$git branch --set-upstream-to=origin/main myNameBranch

#this makes it so that if more than one person is working on branch when you type git pull you pull any new contents from myNameBranch

$git branch --set-upstream-to=origin/myNameBranch

$git pull

#this creates a txt file within your branch

$touch myName.txt

#the following few commands up until the git push will push all of your additions to your branch assuming you're still in your branch

$git status

# it is also good practice to pull before pushing in order to make sure there's no merge conflicts

$git pull

$git add .

$git status

$git push origin myNameBranch

#lastly in order to merge your branch with the main branch you go to the github repo ##online and select your branch on the top left currently you should see the word main and a drop down arrow when you click it you will hopefully see your branch and once you've selected your branch you can click pull request over to the right under the big green button
Follow the pull request steps and boom you have now merged your branch with main

#For some extra practice make sure that you are in your branch delete the myName.txt file and try merging that with master so there is no more myName.txt file

#This places you back in the main branch

$git checkout main

