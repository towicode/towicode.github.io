# Setup Guide 2016 for Ubuntu. #


## All About terminal

To follow this tutorial you should be familiar with terminal in UNIX style machines. The terminal or shell is a powerful tool you can use to quickly navigate, modify, and administer files and programs on your machine. It’s also a necessary tool when you want to access a server’s machine via SSH. To start a terminal in ubuntu Unity do one of the following.

> Dash -> Search for Terminal

> Dash -> More Apps -> 'See More Results' -> Terminal

> Dash -> More Apps -> Accessories -> Terminal

> Keyboard Shortcut: Ctrl + Alt + T

### File & Directory Commands:

The tilde (~) symbol stands for your home directory. If you are user, then the tilde (~) stands for /home/user

To save on typing, you can substitute '~' in place of the home directory. **Note** that if you are using mv with sudo you can use the ~ shortcut, because the terminal expands the ~ to your home directory. However, when you open a root shell with sudo -i or sudo -s, ~ will refer to the root account's home directory, not your own.

**pwd:** The pwd command will allow you to know in which directory you're located (pwd stands for "print working directory"). Example: "pwd" in the Desktop directory will show "~/Desktop". Note that the GNOME Terminal also displays this information in the title bar of its window. A useful gnemonic is "present working directory."

**ls:** The ls command will show you ('list') the files in your current directory. Used with certain options, you can see sizes of files, when files were made, and permissions of files. Example: "ls ~" will show you the files that are in your home directory.

**cd:** The cd command will allow you to change directories. When you open a terminal you will be in your home directory. To move around the file system you will use cd. Examples:

    To navigate into the root directory, use "cd /"

    To navigate to your home directory, use "cd" or "cd ~"

    To navigate up one directory level, use "cd .."

    To navigate to the previous directory (or back), use "cd -"

    To navigate through multiple levels of directory at once, specify the full directory path that you want to go to. For example, use, "cd /var/www" to go directly to the /www subdirectory of /var/. As another example, "cd ~/Desktop" will move you to the Desktop subdirectory inside your home directory.

**cp:** The cp command will make a copy of a file for you. Example: "cp file foo" will make an exact copy of "file" and name it "foo", but the file "file" will still be there. If you are copying a directory, you must use "cp -r directory foo" (copy recursively). (To understand what "recursively" means, think of it this way: to copy the directory and all its files and subdirectories and all their files and subdirectories of the subdirectories and all their files, and on and on, "recursively")

**mv:** The mv command will move a file to a different location or will rename a file. Examples are as follows: "mv file foo" will rename the file "file" to "foo". "mv foo ~/Desktop" will move the file "foo" to your Desktop directory, but it will not rename it. You must specify a new file name to rename a file.

**rm:** Use this command to remove or delete a file in your directory.

**rmdir:** The rmdir command will delete an empty directory. To delete a directory and all of its contents recursively, use rm -r instead.

**mkdir:** The mkdir command will allow you to create directories. Example: "mkdir music" will create a directory called "music".

**man:** The man command is used to show you the manual of other commands. Try "man man" to get the man page for man itself. See the "Man & Getting Help" section down the page for more information.

**sudo:** The sudo command is used to perform file operations on files that the Root User would only be allowed to change. An example would be trying to move one of your documents that another user accidentally moved to / back to your documents directory. Normally, to move the file, you would type mv /mydoc.odt ~/Documents/mydoc.odt, but you are not allowed to modify files outside of your home directory. To get around this, you would type sudo mv /mydoc.odt ~/Documents/mydoc.odt. This will successfully move the file back to its correct location, provided that you are not a standard user, who has less (administrative) ability than an administrator. Be aware, though, that by using the sudo command, you need to be extra careful. It is easier to damage your system by using the sudo command. For more information about the sudo command, click here.

### Ubuntu packages we need to install

To be able to use the dev environment we have to install a few pre-requisite packages. To install them simply copy and paste these into a terminal shell one by one. note that paste in terminal ubuntu is default ctrl-shift-v

`sudo apt-get install zsh`

`sudo add-apt-repository ppa:gnome-terminator`

`sudo apt-get update`

`sudo apt-get install terminator`

`sudo apt-get install git`

`sudo apt-get install git-flow`

`sudo apt-get install libpq-dev`

`sudo apt-get install libxml2-dev libxslt1-dev`

`sudo apt-get install python-dev`

`sudo apt-get install python-pip`

`sudo apt-get install python-flake8`

`sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"`

`sudo pip install virtualenvwrapper`


### Opening and using terminator
Now you should have powerful tool named terminator installed on your computer. You can open it similarly to how you opened terminal before

> Dash -> Search for Terminator

You can give this web page a brief read, try to learn how to split windows horizontally and vertically.
http://gnometerminator.blogspot.com/p/introduction.html


### Setting up your terminal to be more productive
The following is a short guide on how to setup ZSH with some plugins and a theme. 
This is not the only way to customize your terminal and everybody has different preferences towards colors and themes.
For a more interactive terminal you may also want to checkout [fish](https://fishshell.com/)

#### Installing a powerline font
Goto [here](https://github.com/powerline/fonts/blob/master/DejaVuSansMono/DejaVu%20Sans%20Mono%20for%20Powerline.ttf) and Install the font by opening this file (may have to click (view raw)) and then clicking install on the top right of the ubuntu font window.

On terminator 
right click -> preferences -> profiles -> default -> uncheck ‘use system fixed width font’ -> deja vu sans mono powerline’


#### Installing and enabling ZSH plugins

Copy any paste the following line into your terminal, It will install a helpful ZSH plugin that auto completes previous commands that you have typed. Simply use the right arrow key to activate the auto-complete feature.

`git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions`

Now we are going to modify your .zshrc file. This file is the configuration file for ZSH. We are going to do a couple of things here including; setting up our virtual environment wrapper, setting the default user, enabling plugins and finally changing the theme of ZSH. 

1. type `whoami` and remember the output, for me it was todd
2. `nano ~/.zshrc`
3. goto end of file (Ctrl + w + v)
4. paste the following (ctrl + shift + v)
    
    ```export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh```
5. While you are at the bottom of the file add the following line, replacing todd with the whoami output from above

    `export DEFAULT_USER=”todd”`

6. find plugins (ctrl-w plugins) you should find something like plugins=(git) replace it with this.

    `plugins=(zsh-autosuggestions gulp nvm git git-flow)`

7. find ZSH_THEME (ctrl-w ZSH_THEME) Change the theme to agnostic, a more productive theme. (should originally be robby or something)

    `ZSH_THEME="agnoster"`
    
8.  restart zsh by typing `zsh` in the terminal window

## Global Installs

These are things you should only have to once when setting up your computer.

### Installing nvm
Run the following command to install node version manager. A program that let’s you install multiple versions of node to work on different projects.

`curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash`

restart zsh by typing:

`zsh`

finally have NVM install node 0.12, the default node we use for our projects
`nvm install 0.12`
if you ever get an error about node not being installed you can now simply type
`nvm use default`

### Virtual Environments

Python virtual environments help us with consistency in our development environment. You will need to use one whenever working on any ehip-project
Create a virtualenv by running 

`mkvirtualenv yourname-projectname`

you can exit a virtualenv by typing 

`deactivate`
you can activate an already existing virtualenv by typing

`workon yourname-projectname`


### Bitbucket and SSH:
1. goto https://bitbucket.org/account/user/<bitbucket_username>/ssh-keys/
2. click add key
3. give it a reasonable name ‘Todd-Work-Computer-ubuntu’
4. in terminator
     1. `ssh-keygen` (use defaults, no passphrase)
     2. `ssh-agent /bin/bash`
     3. `ssh-add ~/.ssh/id_rsa`
     4. `cat ~/.ssh/id_rsa.pub`
5. copy the text including the user@user-machine part. (right click -> copy)
paste it in the key box

### Atom Editor:

Atom is a free open-source editor that is very powerful. Since we primarily deal with javascript, python and html it’s an ideal candidate for editing.
grab the latest version of atom at https://atom.io/

Install the following helpful packages: Make sure to briefly read through them so you know what they do.
https://atom.io/packages/linter-flake8

https://atom.io/packages/linter-jshint

https://atom.io/packages/linter

https://atom.io/packages/docblockr

https://atom.io/packages/atom-beautify

https://atom.io/packages/emmet

To open a project directory in atom simply type:

`cd ~/<project>/django`

`atom .`
### Javascript Global Install:


The following are important global modules that you will need to start developing. both npm and jspm are package managers that we use to install various packages.

Note that you should only have to do this once when you are setting up your machine. If you get an error ‘command not found: npm’
that means you don’t have node installed or activated. Try typing `nvm use default` before installing, and if that doesn’t work scroll up to the installing nvm section.

`npm install -g jspm@0.15 jspm-git gulp`

##### Configuring jspm registries
These registry configurations must be completed once after installing jspm with npm. This must be completed on every environment including Vagrant, but once it is configured, it is saved to that installation of jspm.
Configure the bitbucket registry ** NOTE: this setting is global, so you should only need to run it once.
You will need to have setup an ssh key with Bitbucket. You should give Bitbucket a public key that does not include a passphrase. There is a bug in that jspm install does not work with Bitbucket when the public key has a passphrase. Or maybe it is a bug wiht https://github.com/Orbs/jspm-git.

    jspm registry create bitbucket jspm-git
    Enter the base URL of your git server e.g. https://code.mycompany.com/git/: ssh://git@bitbucket.org/
    Set advanced configurations? [no]:
    Registry bitbucket configured successfully.

Configure the github endpoint 

**NOTE: this setting is global, so you should only need to run it once.** 

Optional, though highly recommended: **Sometimes during jspm install github's public API will rate-limit your access, so we need to authenticate.** You'll need a github access token. **Make sure to enable repo, and public_repo access.** You can regenerate this token if you are rebuilding a development environment.

    jspm registry config github
     Would you like to set up your GitHub credentials? [yes]:
     If using two-factor authentication or to avoid using your password you can generate an access token at https://github.com/settings/tokens.
     Enter your GitHub username: <username>
     Enter your GitHub password or access token: <token>
     Would you like to test these credentials? [yes]:
     ok   GitHub authentication is working successfully.
     ok   Registry github configured successfully.```

#### Setting up PSQL: (this is just a torn down version of [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)

Ubuntu's default repositories contain Postgres packages, so we can install them without a hassle using the apt packaging system.
Since we haven't updated our local apt repository lately, let's do that now. We can then get the Postgres package and a "contrib" package that adds some additional utilities and functionality:

`sudo apt-get install postgresql postgresql-contrib`

Upon installation Postgres is set up to use "ident" authentication, meaning that it associates Postgres roles with a matching Unix/Linux system account. If a Postgres role exists, it can be signed in by logging into the associated Linux system account.
The installation procedure created a user account called postgres that is associated with the default Postgres role. In order to use Postgres, we'll need to log into that account. You can do that by typing:

`sudo -i -u postgres`


You will be asked for your normal user password and then will be given a shell prompt for the postgresuser.
You can get a Postgres prompt immediately by typing:

From the postgres Linux account, you have the ability to log into the database system. However, we're also going to demonstrate how to create additional roles. The postgres Linux account, being associated with the Postgres administrative role, has access to some utilities to create users and databases.
We can create a new superuser role by typing, replace todd with your ‘whoami’ command result.

`createuser -P -s -e todd`

Now you will be able to use database commands from your main user account.
press (ctrl -d) to exit the prompt and then create a new database by typing:

`createdb bcf-core`


## Things to do for every project you install:

### Setting up to work on a new project:

It’s probably important to have a dedicated work directory so you can easily find and manage all your projects at once. I prefer just to put all my projects in my home folder on ubuntu, mainly because I don’t use my work computer for anything other than work.

Here is an example of how I set up a new project from our bitbucket

1.  `cd`  (goto home directory)
2. `mkdir bcf-core ` (we make a directory to hold the project)
3. `git clone git@bitbucket.org:BCF_ARL/bcf-core.git bcf-core`
    * note this command has 4 arguments
        1. git 
        2. clone - we want to clone an existing project
        3. git@bit… - the address we want to clone from
        4. bcf-core - the folder we just created that we are going to clone into.
    
This is my prefered setup because you can always change projects just by typing:
1. `cd ~/<project>`


### Install Python Requirements.

make sure you are in your django/bcfsrc folder
Type the following command to install all python requirements for the project.

`pip install -r requirements.txt`

Possible errors:
Error: [Errno 13] Permission denied:
Make sure you are in a virtualenv. for example 

`workon todd-bcf-core`




### Install Javascript Requirements:

(make sure you are in the directory with the file  package.json in it)
Type the following commands to install all javascript requirements for the project.
`npm install`

`jspm init` 
 #when asked to create config.js file say yes.  Don't do advanced options.  If asked to create a package.json file, then oops you are running this command from the wrong place - see note above about being in the bcfsrc folder`

`jspm install`

`gulp`

### Create a Database: 
`createdb <project-name>`

example: `createdb bcf-core`


### Creating local settings:

Navigate to the settings folder in your project. <project>/django/settings OR <project>/bcfsrc/settings.
Copy the example to a new file called local.py

`cp local_example.py local.py`

open local.py in atom, `atom local.py`

Edit all the fields in <> brackets. including the following.
NAME - the name of the database you created - example: bcfcore
USER - the user you created for psql, probably equal to your whoami status - example: todd
PASSWORD - password

Add Django Apps to settings/local.py
See settings/README.md...if it exists...you will need to add installed apps to your settings/local.py file.

