# Veapysh
A terminal utility programmed in python and bash script, for the automation of basic processes for the end user. Only available on Linux systems.

This utility makes use of the commands offered by the Linux terminal to automate simple tasks such as making backup copies for a certain time. It also offers a registry file to see in real time the changes made by the program.

## Sections:

## Install veapysh
To install Veapysh, simply clone this repository with the following commands:
    
    cd ~/Downloads
    git clone https://github.com/TheWatcherMultiversal/Veapysh.git

We enter the folder and execute the following command:

    cd Veapysh
    ./install.sh
    
- Note: To remove the program, simply run the same command with the -u option to revert the changes.

Now we just test if the program has been installed correctly by executing the following command in the terminal.

    veapysh
    
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
