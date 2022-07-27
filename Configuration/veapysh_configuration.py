#!/usr/bin/python3

# Veapysh is a terminal utility to manage basic scripts 
# in an easy and intuitive way for the user.

# Only modify the source code if you know what you are doing.

# Developed by: Angel Gabriel Mortera Gual.
# Github: https://github.com/TheWatcherMultiversal/Veapysh

import subprocess
import time

from colorama import Fore, init
init()

def app():

# This section belongs to the Veapysh options menu.

    question = True

    while question:

        subprocess.run("clear", shell=True)
        print(Fore.GREEN + "\r\nVeapysh" + Fore.CYAN + " is a terminal utility to manage your Linux system with automated scripts.\r\n")
        print(Fore.YELLOW +"Developed by:"  + Fore.RESET + " Angel Gabriel Mortera Gual.")
        print(Fore.YELLOW +"Project link:" + Fore.RESET + " link\r\n")

        print(Fore.RESET + "  a) System backup.")
        print("  b) System updater.")
        print("  c) View active scripts.")
        print("  d) Restore system with backup.")
        print("  e) More.")
        print("  f) Exit.")

        opc_0 = input("\r\nSelect an option [a/b/c/d/e/f] ")

        if opc_0 == "a":
            print(Fore.GREEN + "\r\nGenerate backup script...\r\n" + Fore.RESET)
            time.sleep(2)
            subprocess.run("sudo /etc/veapysh/Configuration/veapysh_backup.sh", shell=True)
            print("Finished process...")
            time.sleep(2)

        elif opc_0 == "b":
            print(Fore.GREEN + "\r\nGenerate upgrade script...\r\n" + Fore.RESET)
            time.sleep(2)
            subprocess.run("sudo /etc/veapysh/Configuration/veapysh_upgrade.sh", shell=True)
            print("Finished process...")
            time.sleep(2)

        elif opc_0 == "c":
            subprocess.run("sudo /etc/veapysh/Configuration/veapysh_viewprocess.sh", shell=True)
            print("Finished process...")
            time.sleep(2)

        elif opc_0 == "d":
            question_2 = True
            while question_2:
                subprocess.run("clear", shell=True)
                print(Fore.CYAN + "\r\nFirst choose the hard drive you want to restore. Press")
                print("\"q\" to cancel the process.\r\n")
                print(Fore.YELLOW +"Example:"  + Fore.RESET + " sda\r\n")
                print(Fore.GREEN + "More info:" + Fore.RESET + " https://tldp.org/LDP/sag/html/partitions.html \r\n")
                subprocess.run("df | head -1", shell=True)
                subprocess.run("df | grep sd; echo ''", shell=True)
                opc_0_a = input("Type the hard drive to restore: ")

                if opc_0_a == "q":
                    question_2 = False

                else:
                    print(Fore.GREEN + "\r\nSaving info :)" + Fore.RESET)
                    time.sleep(2)
                    question_2_1 = True
                    while question_2_1:
                        subprocess.run("clear", shell=True)
                        print(Fore.CYAN + "\r\nChoose the backup to restore the system. Press \"q\" to cancel process. ")
                        print("If you do not see any files, it is because a backup has not")
                        print("yet been generated\r\n")
                        print(Fore.YELLOW +"Example:"  + Fore.RESET + " sdabackup.img.bz2\r\n")
                        print(Fore.GREEN + "More info:" + Fore.RESET + " https://www.geeksforgeeks.org/dd-command-linux/")
                        subprocess.run("sudo /etc/veapysh/Configuration/s1/list_backups.sh", shell=True)
                        opc_0_b = input("Select backup file: ")

                        if opc_0_b == "q":
                            question_2_1 = False
                            
                        else:
                            print(Fore.GREEN + "\r\nRestoring the \"sda\" disk drive, do not turn off your device.\r\n" + Fore.RESET)
                            time.sleep(2)
                            command_bunzip2 = "sudo bunzip2 /etc/veapysh/Backups/" + opc_0_b
                            subprocess.run(command_bunzip2, shell=True)
                            file_restore = ""
                            num = len(opc_0_b) - 4

                            for i in range(0, num):
                                file_restore += opc_0_b[i]

                            command_restore = "dd if=/etc/veapysh/Backups/" + file_restore + " of=/dev/" + opc_0_a
                            subprocess.run(command_restore, shell=True)
                            command_bz2 = "sudo bzip2 /etc/veapysh/Backups/" + file_restore
                            subprocess.run(command_bz2, shell=True)
                            print(Fore.GREEN + "Process completed successfully" + Fore.RESET)
                            time.sleep(4)
                            question_2_1 = False

        elif opc_0 == "e":
            question_2 = True
            while question_2:

                subprocess.run("clear", shell=True)
                print(Fore.GREEN + "\r\nVeapysh" + Fore.CYAN + " is a terminal utility to manage your Linux system with automated scripts.\r\n")
                print(Fore.YELLOW +"Developed by:"  + Fore.RESET + " Angel Gabriel Mortera Gual.")
                print(Fore.YELLOW +"Project link:" + Fore.RESET + " link\r\n")

                print(Fore.RESET + "  a) About.")
                print("  b) Man page.")
                print("  c) <-- To return.")
                opc_0_1 = input("\r\nSelect an option [a/b/c] ")

                if opc_0_1 == "a":
       
                    subprocess.run("clear", shell=True)               
                    print(Fore.GREEN + "Veapysh" + Fore.CYAN + " is a terminal utility for managing automatic system scripts in an")
                    print("easy and end-user friendly way.\r\n")
                    time.sleep(3)
                    # Information about the project.
                    print(Fore.YELLOW +"License:" + Fore.RESET + " GNU General Public License v2.0")
                    time.sleep(3)
                    print(Fore.YELLOW +"Developed by:"  + Fore.RESET + " Angel Gabriel Mortera Gual")
                    time.sleep(3)
                    print(Fore.YELLOW +"My Github:"  + Fore.RESET + " https://github.com/TheWatcherMultiversal\r\n")
                    time.sleep(3)
                    print(Fore.YELLOW +"Contributors:"  + Fore.RESET)
                    # Here add your name if you are a contributor to the project :)
                    print("- Emir Pérez Martinez")
                    time.sleep(4)

                elif opc_0_1 == "b":
                    subprocess.run("man veapysh", shell=True)
                
                elif opc_0_1 == "c":
                    question_2 = False

                else:
                    print(Fore.RED + "\r\nWrong value!!!\r\n" + Fore.RESET)
                    time.sleep(1)

        elif opc_0 == "f":
            subprocess.run("clear", shell=True)
            question = False
            exit
        
        else:
            print(Fore.RED + "\r\nWrong value!!!\r\n" + Fore.RESET)
            time.sleep(1)

app()
