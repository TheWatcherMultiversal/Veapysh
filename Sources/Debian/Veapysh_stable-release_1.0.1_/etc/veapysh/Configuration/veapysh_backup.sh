#!/bin/bash

# This script will test the system to create the backup.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

# Checking if the backup script exists.

clear
if [ -f /etc/init.d/veapysh-generatorbackups ]; then

	i=0
	while [ $i -lt 1 ]; do
		echo "There is already a script for backups."
	        echo "Do you want to create a new script?"
        	echo ""; echo 'Type "y" to create a new script.'
        	echo 'Type "n" to ignore this message.'
        	echo 'Type "x" to kill the running backup script.'

		read OPTION_A
		case "$OPTION_A" in
		y|Y)
			echo ""; echo "Creating new script..."
			sudo update-rc.d veapysh-generatorbackups remove
			sudo rm /etc/init.d/veapysh-generatorbackups
			echo "`date +%b | tr 'a-z' 'A-Z' | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh backup script disabled" >> /var/log/veapysh.log
			sleep 2s
			sudo python3 /etc/veapysh/Configuration/s1/backup_script.py
			i=1
			;;
		n|N)
			echo ""; i=1
			;;
		x|X)    
                        sudo update-rc.d veapysh-generatorbackups remove
			sudo rm /etc/init.d/veapysh-generatorbackups
			echo "`date +%b | tr 'a-z' 'A-Z' | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh backup script disabled" >> /var/log/veapysh.log
			echo""; echo "The script has been removed."
			sleep 2s
			i=1
                        ;;
		*)
			echo ""
		esac
	done
else
	I=0
	      while [ $I -lt 1 ]; do
		echo "Are you sure to create the script for the backups? [Y/n]"; read OPTION_B
                case "$OPTION_B" in
                y|Y)
                        echo ""; sudo python3 /etc/veapysh/Configuration/s1/backup_script.py
			I=1
                        ;;
                n|N)
                        echo ""; I=1
                        ;;
                *)
                        echo ""
                esac
        done
fi

