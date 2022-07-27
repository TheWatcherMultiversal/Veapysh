#!/bin/bash

# This is a simple script to check active processes.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal

echo ""
echo 'Script:                              Status:'
if [ -f /etc/init.d/veapysh-generatorbackups ]; then
	echo -e "veapysh-generatorbackups" "	     (\e[32mEnabled\e[0m)"
else
	echo -e "veapysh-generatorbackups" "            (\e[31mDisabled\e[0m)"
fi

if [ -f /etc/init.d/veapysh-generatorupgrades ]; then
        echo -e "veapysh-generatorupgrades" "           (\e[32mEnabled\e[0m)"
else
        echo -e "veapysh-generatorupgrades" "           (\e[31mDisabled\e[0m)"
fi       
echo ""; echo -e "Press" "\e[32mENTER\e[0m" " to finish the process."

i=1
read OPX
while [ "$i" = "1" ]; do
  case "$OPX" in
  *)
    i=0
  esac
done
