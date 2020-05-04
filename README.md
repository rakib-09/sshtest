# Automate your Uploading to remote server from GIT using Pyhton Fabric

Upload Project to hosting direct from Git Server

*	First of all, open fabfile.py file. 
*	There you will find 5 variables
*	Project_dir
*	Root_dir
*	REPO_URL
*	Env.hosts
*	Env.user

## Project_dir:

	Your Project directory name of git server.

## Root_dir:

	Your file path at hosting.

 ## REPO_URL:

	Your Git server link…(.git)

## Env.hosts:

	Your Hostname of Hosting server (To connect through SSH)

## Env.user :
	UserName of Hosting server (To connect through SSH)
 
 #### After Changing all of this information you are good to go!!! 😊 
 
 * Now just write
 ```
 fab deploy
```

