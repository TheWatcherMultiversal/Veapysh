#!/usr/bin/python3

# Creating the backup script.
# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

import subprocess
import time
from colorama import Fore, init
init()

def backup_script():

# Main format of the script.

    subprocess.run("echo \#!/bin/bash > /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '### BEGIN INIT INFO' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Provides:           veapysh-generatorbackups' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Required-Start:     $syslog' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Required-Stop:      $syslog' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Default-Start:      2 3 4 5' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Default-Stop:       0 1 6' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Short-Description:  Backup script' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Description:        Veapysh backup script' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '### END INIT INFO' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# Author:             Angel Gabriel Mortera Gual' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo '# ========================================================' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \# \"This backup script is executed automatically with\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \# \"respect to the parameters provided by the user.\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \# \"Only modify the source code if you know what you are doing.\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \# \"Date data.\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

    subprocess.run("echo \"TIMEDATA=\`date +%H\`\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"TIMEDATA_DAY=\`date +%d\`\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"TIMEDATA_DAY_WEEK=\`date +%u\`\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"TIMEDATA_MONTH=\`date +%m\`\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"TIMEDATA_YEAR=\`date +%Y\`\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    
    subprocess.run("echo \"sleep 30m\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"i=1\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
    subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

# User interaction to get the data from the script.

    print(Fore.GREEN + "Fill in the options to complete the script :)" + Fore.RESET)
    QA = True
    while QA:
        print("\r\nSelect a" + Fore.YELLOW + " time period" + Fore.RESET + " for a backup to be generated.\r\n")
        print("   a) Per month\r\n   b) Per week\r\n   c) Per day\r\n")

        opc_1 = input("Select an option [a/b/c] ")

# Option "a" - Per month ============================================================================================================================

        if opc_1 == "a":
            print("")

            Qs=True
            while True:
                try:
                    opc_2 = int(input("Indicates the day of the month for the backup [1-28] "))

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
                                                    
            command_a = 'echo \'TIME_PERIOD=\"' + Time_period + '\"\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            
            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)            
            subprocess.run("echo '  case \"$TIMEDATA_DAY\" in' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True) 
            subprocess.run("echo '  " + Time_period  +")' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qsz = True
            disk_partitions = [] 
            while Qsz:
                subprocess.run("clear", shell=True)
                disk_partitions=list(set(disk_partitions))
                print(Fore.CYAN + "Carefully select partitions for backup, also note that you have")
                print("to type the partition name correctly.")
                print("Take into account the hard drive space you have.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " sda1")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://tldp.org/LDP/sag/html/partitions.html \r\n")
                subprocess.run("df | head -1", shell=True)
                subprocess.run("df | grep sd; echo", shell=True)
                print("Added partitions:")

                for partitions in disk_partitions:
                    print("- " + Fore.GREEN + partitions + Fore.RESET)
                print()
                opc_3 = input("Place your partition for backup, press \"q\" to end and \"x\" to delete: ")

                if opc_3 == "q" or opc_3 == "Q":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        Qsz = False

                elif opc_3 == "x" or opc_3 == "X":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        while True:
                            try:
                                disk_partitions.remove(input("Type the partition to remove from the list: "))
                                subprocess.run("clear", shell=True)
                                break
                            except ValueError:
                                print(Fore.RED + "\r\nThe value is not found in the list!!!\r\n" + Fore.RESET)
                                time.sleep(2)
       
                else:
                    disk_partitions.append(opc_3)
                    print(Fore.GREEN + "\r\nPartition added successfully :)" + Fore.RESET)
                    time.sleep(1)
                    subprocess.run("clear", shell=True)
            
            for partitions in disk_partitions:
                subprocess.run("echo '    rm /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img.bz2' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Generating backup in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    sudo dd if=/dev/" + partitions  + " of=/etc/veapysh/Backups/" + partitions  + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    bzip2 /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Backup generated successfully in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            
            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s1/veapysh-generatorbackups /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorbackups defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh backups script activated on path /etc/init.d/veapysh-generatorbackups >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe backup script is ready!!!\r\n" + Fore.RESET)
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
            command_a = 'echo \'TIME_PERIOD=\"' + week_number_str + '\"\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  case \"$TIMEDATA_DAY_WEEK\" in' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  " + week_number_str  +")' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qsz = True
            disk_partitions = []
            while Qsz:
                subprocess.run("clear", shell=True)
                disk_partitions=list(set(disk_partitions))
                print(Fore.CYAN + "Carefully select partitions for backup, also note that you have")
                print("to type the partition name correctly.")
                print("Take into account the hard drive space you have.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " sda1")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://tldp.org/LDP/sag/html/partitions.html \r\n")
                subprocess.run("df | head -1", shell=True)
                subprocess.run("df | grep sd; echo", shell=True)
                print("Added partitions:")

                for partitions in disk_partitions:
                    print("- " + Fore.GREEN + partitions + Fore.RESET)
                print()
                opc_3 = input("Place your partition for backup, press \"q\" to end and \"x\" to delete: ")

                if opc_3 == "q" or opc_3 == "Q":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        Qsz = False

                elif opc_3 == "x" or opc_3 == "X":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        while True:
                            try:
                                disk_partitions.remove(input("Type the partition to remove from the list: "))
                                subprocess.run("clear", shell=True)
                                break
                            except ValueError:
                                print(Fore.RED + "\r\nThe value is not found in the list!!!\r\n" + Fore.RESET)
                                time.sleep(2)

                else:
                    disk_partitions.append(opc_3)
                    print(Fore.GREEN + "\r\nPartition added successfully :)" + Fore.RESET)
                    time.sleep(1)
                    subprocess.run("clear", shell=True)

            for partitions in disk_partitions:
                subprocess.run("echo '    rm /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img.bz2' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Generating backup in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    sudo dd if=/dev/" + partitions  + " of=/etc/veapysh/Backups/" + partitions  + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    bzip2 /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Backup generated successfully in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            
            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    sleep 1d' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s1/veapysh-generatorbackups /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorbackups defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh backups script activated on path /etc/init.d/veapysh-generatorbackups >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe backup script is ready!!!\r\n" + Fore.RESET)
            time.sleep(5)

            QA=False

# Option "c" - Per day ============================================================================================================================

        elif opc_1 == "c":

            print("")

            Qs=True
            while True:
                try:
                    opc_2 = int(input("Indicates the time of day in 24-hour format for the backup [0-23] "))

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
            
            command_a = 'echo \'TIME_PERIOD=\"' + Time_period + '\"\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups'
            subprocess.run(command_a, shell=True)
            subprocess.run("echo \"\" >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            subprocess.run("echo \'while [ \"$i\" = \"1\" ]; do\' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  case \"$TIMEDATA\" in' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  " + Time_period  +")' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
            time.sleep(2)

            Qsz = True
            disk_partitions = []
            while Qsz:
                subprocess.run("clear", shell=True)
                disk_partitions=list(set(disk_partitions))
                print(Fore.CYAN + "Carefully select partitions for backup, also note that you have")
                print("to type the partition name correctly.")
                print("Take into account the hard drive space you have.")
                print(Fore.YELLOW + "\r\nExample:" + Fore.RESET + " sda1")
                print(Fore.GREEN + "\r\nMore info:" + Fore.RESET + " https://tldp.org/LDP/sag/html/partitions.html \r\n")
                subprocess.run("df | head -1", shell=True)
                subprocess.run("df | grep sd; echo", shell=True)
                print("Added partitions:")

                for partitions in disk_partitions:
                    print("- " + Fore.GREEN + partitions + Fore.RESET)
                print()
                opc_3 = input("Place your partition for backup, press \"q\" to end and \"x\" to delete: ")

                if opc_3 == "q" or opc_3 == "Q":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        Qsz = False

                elif opc_3 == "x" or opc_3 == "X":
                    if len(disk_partitions) == 0:
                        print(Fore.RED + "\r\nHas not added any value yet!!!" + Fore.RESET)
                        time.sleep(2)
                        subprocess.run("clear", shell=True)
                    else:
                        while True:
                            try:
                                disk_partitions.remove(input("Type the partition to remove from the list: "))
                                subprocess.run("clear", shell=True)
                                break
                            except ValueError:
                                print(Fore.RED + "\r\nThe value is not found in the list!!!\r\n" + Fore.RESET)
                                time.sleep(2)

                else:
                    disk_partitions.append(opc_3)
                    print(Fore.GREEN + "\r\nPartition added successfully :)" + Fore.RESET)
                    time.sleep(1)
                    subprocess.run("clear", shell=True)

            for partitions in disk_partitions:
                subprocess.run("echo '    rm /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img.bz2' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Generating backup in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    sudo dd if=/dev/" + partitions  + " of=/etc/veapysh/Backups/" + partitions  + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
                subprocess.run("echo '    bzip2 /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups" , shell=True)
                subprocess.run("echo '    echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Backup generated successfully in /etc/veapysh/Backups/" + partitions + "backup_$TIMEDATA_DAY-$TIMEDATA_MONTH-$TIMEDATA_YEAR.img >> /var/log/veapysh.log' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)                
            
            subprocess.run("echo '    sleep 1h' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    ;;' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  *)' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '    sleep 1h' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo '  esac' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("echo 'done' >> /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)

            subprocess.run("sudo chown root:root /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo chmod u=rwx,g=rx,o=rx /etc/veapysh/Configuration/s1/veapysh-generatorbackups", shell=True)
            subprocess.run("sudo mv /etc/veapysh/Configuration/s1/veapysh-generatorbackups /etc/init.d/", shell=True)
            subprocess.run("sudo update-rc.d veapysh-generatorbackups defaults", shell=True)
            subprocess.run("echo `date +%b | tr \"a-z\" \"A-Z\" | cut -c1``date +%b | cut -c2-3` `date +%d` `date +%X` `whoami` `id -g -n`: Veapysh backups script activated on path /etc/init.d/veapysh-generatorbackups >> /var/log/veapysh.log", shell=True)

            print(Fore.GREEN + "\r\nThe backup script is ready!!!\r\n" + Fore.RESET)
            time.sleep(5)

            QA=False

        else:
            subprocess.run("clear", shell=True)

backup_script()
