#!/bin/bash

# Veapysh: is a terminal utility available on Linux systems for automated administration of basic scripts.
# License: GNU General Public License v2.0
# Developed by: Angel Gabriel Mortera Gual
# Github project: https://github.com/TheWatcherMultiversal/Veapysh

# Install program =======================================================================================

sudo echo -e "\e[32mThe installation process has started, use this same executable with the \e[0m-u\e[32m option to reverse the process.\e[0m"

# Options

case "$1" in
-u)
	sudo rm -Rf /etc/veapysh/
	sudo rm /sbin/veapysh
	sudo rm /usr/share/man/man1/veapysh.1.gz
	sudo update-rc.d veapysh-generatorbackups remove
	sudo update-rc.d veapysh-generatorupgrades remove
	sudo rm /etc/init.d/veapysh-generatorbackups
	sudo rm /etc/init.d/veapysh-generatorupgrades
	sudo rm -Rf /usr/share/veapysh/
	echo "Deleted program."
	;;
*)

# Checking if the necessary binaries exist. =============================================================

	echo ""; echo "Checking if the necessary files exist for the program to work:"
	if type dd 2>&1> /dev/null; then
		echo "The dd command if it exists..."
		sleep 1s
	else
		echo "This program makes use of the dd command, install it to make it work."
		sleep 1s
	fi

	if type update-rc.d 2>&1> /dev/null; then
		echo "The update-rc.d command if it exists..."
		sleep 1s
	else
		echo "This program makes use of the update-rc.d command, install it to make it work."
                sleep 1s
	fi

# Organization of binary, executable and configuration files. ===========================================
	
	echo ""; echo "Organizing configuration files."
	sudo mkdir /etc/veapysh/; sudo cp -r Configuration /etc/veapysh/; sudo mkdir /etc/veapysh/Backups
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/veapysh_backup.sh
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/veapysh_configuration.py
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/veapysh_upgrade.sh
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/veapysh_viewprocess.sh
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s1/backup_script.py
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s1/list_backups.sh
	sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s2/upgrade_script.py
	sudo mkdir /usr/share/veapysh/
	sudo cp ./usr/share/veapysh/veapysh-requeriments.sh /usr/share/veapysh/
	sudo chmod u=rxw,g=rx,o=rx /usr/share/veapysh/veapysh-requeriments.sh
	sleep 2s

	echo ""; echo "Extracting executable."
	sudo cp ./Command/veapysh /sbin/
	sudo sudo chmod u=rwx,g=rx,o=rx /sbin/veapysh
	sleep 2s

	echo ""; echo "Adding man page."
	gzip ./Man\ page/veapysh.1
	sudo cp ./Man\ page/veapysh.1.gz /usr/share/man/man1/
	gunzip ./Man\ page/veapysh.1.gz
	sleep 2s

	echo ""; echo "Finishing process. Run the Veapysh command to verify the installation."

esac
