<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00382b&height=130&section=header&text=Veapysh&fontSize=39&fontColor=fff&animation=twinkling&fontAlignY=35"/> 

<div align="center"> 
<p>Technologies used:</p>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Linux-1e1f20?style=for-the-badge&logo=linux&logoColor=yellow"</a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Python-141b4a?style=for-the-badge&logo=python&logoColor=green"</a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Bash-082405?style=for-the-badge&logo=gnu bash&logoColor=white"</a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Git-161618?style=for-the-badge&logo=git&logoColor=orange"</a>
</div>
    
##
    
A terminal utility programmed in python and bash script, for the automation of basic processes for the end user. Only available on Linux systems. This utility makes use of the commands offered by the Linux terminal to automate simple tasks such as making backup copies for a certain time. It also offers a registry file to see in real time the changes made by the program.

## Install veapysh
To install Veapysh, simply clone this repository with the following commands:
    
    cd ~/Downloads
    git clone https://github.com/TheWatcherMultiversal/Veapysh.git

We enter the folder and execute the following command:

    cd Veapysh
    chmod +x ./install.sh
    ./install.sh
    
- Note: To remove the program, simply run the same command with the -u option to revert the changes.

Now we just test if the program has been installed correctly by executing the following command in the terminal.

    sudo veapysh
    
With this, we should have the Veapysh utility up and running.

## Start using veapysh
To start using Veapysh, we run it with its name to display a screen like this:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_1.png?raw=true)

Here we have several options that we will explore in this section.

### System backup & system updater
In these options we can activate the scripts that are available at the moment, first asking us if we want to create the script and then asking us how often the script will be activated. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_2.png?raw=true)

In the case of creating the backup script, it will ask us to choose the partition to perform the backup. It is important to write the partition correctly to avoid problems with the program, since it uses the "dd" command to work correctly. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_3.png?raw=true)

In case you have chosen the system update script option, you only specify the package manager that you have in your distribution. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_8.png?raw=true)

Once the parameters of the script are filled in, it will be executed when we restart the system.

- Note: To disable the scripts, just call the request again so you can kill them right there.

### View active scripts
This request will only show information about the status of the running scripts. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_4.png?raw=true)

This request can also be displayed as follows:

    sudo veapysh -l
    
### Restore system with backup
This request will help us find our backups that have been made with the script, specifying the partition to restore as the first option. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_5.png?raw=true)

Once we have chosen our partition to restore, we choose the backup file for partition restoration. Example:

![1](https://github.com/TheWatcherMultiversal/Veapysh/blob/main/View/Screenshots/Screenshot_6.png?raw=true)

- Note: Choose your options well in this section since the restoration is done directly to your partition, data recovery can be very difficult.

### More
This is a simple section where you can find help information and information about the project.

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
