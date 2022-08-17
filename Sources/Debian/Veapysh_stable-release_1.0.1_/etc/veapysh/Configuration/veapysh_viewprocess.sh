# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

echo ""
echo 'Script:                              Status:'
if [ -f /etc/init.d/veapysh-generatorbackups ]; then
        echo "veapysh-generatorbackups" "            (\e[32mEnabled\e[0m)"
else
        echo "veapysh-generatorbackups" "            (\e[31mDisabled\e[0m)"
fi

if [ -f /etc/init.d/veapysh-generatorupgrades ]; then
        echo "veapysh-generatorupgrades" "           (\e[32mEnabled\e[0m)"
else
        echo "veapysh-generatorupgrades" "           (\e[31mDisabled\e[0m)"
fi       

case $1 in
-l)
        echo ""
        ;;
*)
        echo ""; echo "Press" "\e[32mENTER\e[0m" " to finish the process."

        i=1
        read OPX
        while [ "$i" = "1" ]; do
        case "$OPX" in
        *)
        i=0
        esac
        done
esac
