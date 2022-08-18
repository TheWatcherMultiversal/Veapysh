#!/usr/share/veapysh/veapysh-requeriments.sh

# This script is responsible for checking user permissions.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

# Checking user.

USER_PRIVILEGES=`id -u`

case "$USER" in
root)
	case "$USER_PRIVILEGES" in
	0)
		return 0
		;;
	*)
		echo "Error: You must run this command as sudo"
		return 1
	esac
	;;
*)
	echo "Error: You must run this command as sudo"
	return 1
esac
