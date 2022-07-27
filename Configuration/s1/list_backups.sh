#!/bin/bash

# This script lists the backups.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal


echo ""; echo -e "System backups:"
BACKUPS=`ls /etc/veapysh/Backups/`
for i in $BACKUPS; do
  echo -e "Backup in:" "\e[32m$i\e[0m" 
done
echo ""
