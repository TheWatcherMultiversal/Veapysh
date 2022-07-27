#!/usr/bin/python3

# Creating the upgrade script.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

import subprocess
import time
from colorama import Fore, init
init()

def update_script():

# Main format of the script.

    subprocess.run("echo \#!/bin/bash > /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '### BEGIN INIT INFO' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Provides:           veapysh-generatorupgrades' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Required-Start:     $syslog' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Required-Stop:      $syslog' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Default-Start:      2 3 4 5' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Default-Stop:       0 1 6' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Short-Description:  Upgrade script' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Description:        Veapysh upgrade script' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '### END INIT INFO' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# Author:             Angel Gabriel Mortera Gual' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo '# ========================================================' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \# \"This upgrade script is executed automatically with\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \# \"respect to the parameters provided by the user.\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \# \"Only modify the source code if you know what you are doing.\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \# \"Date data.\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

    subprocess.run("echo \"TIMEDATA=\`date +%H\`\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"TIMEDATA_DAY=\`date +%d\`\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"TIMEDATA_DAY_WEEK=\`date +%u\`\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"TIMEDATA_MONTH=\`date +%m\`\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"TIMEDATA_YEAR=\`date +%Y\`\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    
    subprocess.run("echo \"sleep 30m\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"i=1\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

# User interaction to get the data from the script.

    print(Fore.GREEN + "Fill in the options to complete the script :)" + Fore.RESET)
    QA = True
    while QA:
        print("\r\nSelect a" + Fore.YELLOW + " time period" + Fore.RESET + " for a system upgrade to be generated.\r\n")
        print("   a) Per month\r\n   b) Per week\r\n   c) Per day\r\n")

        opc_1 = input("Select an option [a/b/c] ")

# Option "a" - Per month ============================================================================================================================

        if opc_1 == "a":
            print("")

            Qs=True
            while True:
                try:
                    opc_2 = int(input("Indicates the day of the month for the upgrade [1-28] "))

                    if opc_2 > 28:
                        print(Fore.RED + "\r\nTry a lower value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    elif opc_2 < 1:
                        print(Fore.RED + "\r\nTry a higher value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        break

                except ValueError:
                    print(Fore.RED + "\r\nOnly accept numbers as input!!!\r\n" + Fore.RESET)
                    time.sleep(2)
                    subprocess.run("clear", shell=True)

            month_number_str = str(opc_2)
            for i in range(1,10):
                I = str(i)
                if month_number_str == I:
                    Time_period = "0" + month_number_str
                    break
                else:
                    Time_period = month_number_str
                                                    
            command_a = 'echo \'TIME_PERIOD=\"' + Time_period + '\"\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            
            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)            
            subprocess.run("echo '  case \"$TIMEDATA_DAY\" in' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True) 
            subprocess.run("echo '  " + Time_period  +")' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qzs=True
            while Qzs:
                subprocess.run("clear", shell=True)
                print(Fore.CYAN + "Choose the package manager your distribution uses.")
                print("In case you use yum as a package manager, the system already")
                print("has a script that performs this process.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " apt, yum or pacman")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://en.wikipedia.org/wiki/Package_manager \r\n")
                subprocess.run("lsb_release -i; echo ''", shell=True)
                opc_3 = input("Select your package manager: ")

                if opc_3 == "apt":
                    subprocess.run("echo '    sudo apt-get update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    sudo apt-get upgrade --no-remove' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                elif opc_3 == "yum":
                    subprocess.run("echo '    sudo yum update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False
                
                elif opc_3 == "pacman":
                    subprocess.run("echo '    sudo pacman -Syu' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False
                
                else:
                    print(Fore.RED + "\r\nPackage manager not available.\r\n" + Fore.RESET)
                    time.sleep(2)

            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            
            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s2/veapysh-generatorupgrades /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorupgrades defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh upgrades script activated on path /etc/init.d/veapysh-generatorupgrades >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe upgrade script is ready!!!\r\n" + Fore.RESET)
            time.sleep(5)

            QA=False

# Option "b" - Per week ============================================================================================================================

        elif opc_1 == "b":

            print("")
            Qs=True
            while True:
                try:
                    opc_2 = int(input("Indicates the day of the week, being Monday the value \"1\" [1-7] "))

                    if opc_2 > 7:
                        print(Fore.RED + "\r\nTry a lower value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    elif opc_2 < 1:
                        print(Fore.RED + "\r\nTry a higher value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        break

                except ValueError:
                    print(Fore.RED + "\r\nOnly accept numbers as input!!!\r\n" + Fore.RESET)
                    time.sleep(2)
                    subprocess.run("clear", shell=True)

            week_number_str = str(opc_2)
            command_a = 'echo \'TIME_PERIOD=\"' + week_number_str + '\"\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  case \"$TIMEDATA_DAY_WEEK\" in' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  " + week_number_str  +")' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qzs=True
            while Qzs:
                subprocess.run("clear", shell=True)
                print(Fore.CYAN + "Choose the package manager your distribution uses.")
                print("In case you use yum as a package manager, the system already")
                print("has a script that performs this process.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " apt, yum or pacman")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://en.wikipedia.org/wiki/Package_manager \r\n")
                subprocess.run("lsb_release -i; echo ''", shell=True)
                opc_3 = input("Select your package manager: ")

                if opc_3 == "apt":
                    subprocess.run("echo '    sudo apt-get update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    sudo apt-get upgrade --no-remove' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                elif opc_3 == "yum":
                    subprocess.run("echo '    sudo yum update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                elif opc_3 == "pacman":
                    subprocess.run("echo '    sudo pacman -Syu' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                else:
                    print(Fore.RED + "\r\nPackage manager not available.\r\n" + Fore.RESET)
                    time.sleep(2)

            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s2/veapysh-generatorupgrades /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorupgrades defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh upgrades script activated on path /etc/init.d/veapysh-generatorupgrades >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe upgrade script is ready!!!\r\n" + Fore.RESET)
            time.sleep(5)

            QA=False

# Option "c" - Per day ============================================================================================================================

        elif opc_1 == "c":

            print("")

            Qs=True
            while True:
                try:
                    opc_2 = int(input("Indicates the time of day in 24-hour format for the system upgrade [0-23] "))

                    if opc_2 > 23:
                        print(Fore.RED + "\r\nTry a lower value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    elif opc_2 < 0:
                        print(Fore.RED + "\r\nTry a higher value!!!\r\n" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        break

                except ValueError:
                    print(Fore.RED + "\r\nOnly accept numbers as input!!!\r\n" + Fore.RESET)
                    time.sleep(2)
                    subprocess.run("clear", shell=True)

            hour_number_str = str(opc_2)
            for i in range(0,10):
                I = str(i)
                if hour_number_str == I:
                    Time_period = "0" + hour_number_str
                    break
                else:
                    Time_period = hour_number_str
            
            command_a = 'echo \'TIME_PERIOD=\"' + Time_period + '\"\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  case \"$TIMEDATA\" in' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  " + Time_period  +")' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qzs=True
            while Qzs:
                subprocess.run("clear", shell=True)
                print(Fore.CYAN + "Choose the package manager your distribution uses.")
                print("In case you use yum as a package manager, the system already")
                print("has a script that performs this process.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " apt, yum or pacman")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://en.wikipedia.org/wiki/Package_manager \r\n")
                subprocess.run("lsb_release -i; echo ''", shell=True)
                opc_3 = input("Select your package manager: ")

                if opc_3 == "apt":
                    subprocess.run("echo '    sudo apt-get update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    sudo apt-get upgrade --no-remove' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                elif opc_3 == "yum":
                    subprocess.run("echo '    sudo yum update' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                elif opc_3 == "pacman":
                    subprocess.run("echo '    sudo pacman -Syu' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: System upgrade generated successfully >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
                    Qzs=False

                else:
                    print(Fore.RED + "\r\nPackage manager not available.\r\n" + Fore.RESET)
                    time.sleep(2)

            subprocess.run("echo '    sleep 1h' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '    sleep 1h' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)

            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s2/veapysh-generatorupgrades", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s2/veapysh-generatorupgrades /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorupgrades defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh upgrades script activated on path /etc/init.d/veapysh-generatorupgrades >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe upgrade script is ready!!!\r\n" + Fore.RESET)
            time.sleep(5)

            QA=False


        else:
            subprocess.run("clear", shell=True)

update_script()
