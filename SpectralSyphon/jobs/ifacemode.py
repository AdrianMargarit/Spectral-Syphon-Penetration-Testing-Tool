###########################################################################
###########################################################################
###########################################################################
###########                                                     ###########
###########                  SPECTRAL SYPHON                    ###########
###########                   Packet sniffer                    ###########
###########                    Version 1.0                      ###########
###########                                                     ###########
###########               PROIECT DE DISERTATIE                 ###########
###########         Author: Ion-Margarit Adrian-Florin          ###########
###########       Facultatea de Matematica si Informatica       ###########
###########             Universitatea din Bucuresti             ###########
###########                                                     ###########
###########################################################################
###########################################################################
###########################################################################

import subprocess
import os
import sys
from colorama import Fore, Back, Style


# Function to check if the interface is in monitor mode
def monitor_mode(iface, default_iface=""):
    # Checking to see if user has root/sudo privileges
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    # Checking to see if the interface is already in monitor mode
    if default_iface != "":
        iface = default_iface

        try:
            subprocess.call(["sudo", "systemctl", "stop", "NetworkManager"])
            subprocess.call(["sudo", "ifconfig", iface, "down"])
            subprocess.call(["sudo", "iwconfig", iface, "mode", "monitor"])
            subprocess.call(["sudo", "ifconfig", iface, "up"])

        except Exception as e:
            print(f"{Fore.RED}[!!!] An error occured: {e}{Style.RESET_ALL}")

        else:
            output = str(subprocess.check_output(["iwconfig", iface]))

            # Checking to see if the interface is in monitor mode
            if "Monitor" in output:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Interface {Style.RESET_ALL}{Fore.CYAN}{iface}{Style.RESET_ALL}{Fore.YELLOW} is now in monitor mode!{Style.RESET_ALL}"
                )

            else:
                print(
                    f"{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.YELLOW} Interface {Style.RESET_ALL}{Fore.CYAN}{iface}{Style.RESET_ALL}{Fore.YELLOW} is not in monitor mode!{Style.RESET_ALL}"
                )


# Function to check if the interface is in managed mode
def managed_mode(iface, default_iface=""):
    # Checking to see if user has root/sudo privileges
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    # Checking to see if the interface is already in managed mode
    if default_iface != "":
        iface = default_iface

        try:
            subprocess.call(["sudo", "ifconfig", iface, "down"])
            subprocess.call(["sudo", "iwconfig", iface, "mode", "managed"])
            subprocess.call(["sudo", "ifconfig", iface, "up"])
            subprocess.call(["sudo", "systemctl", "restart", "NetworkManager"])

        except Exception as e:
            print(f"{Fore.RED}[!!!] An error occured: {e}{Style.RESET_ALL}")

        else:
            output = str(subprocess.check_output(["iwconfig", iface]))

            # Checking to see if the interface is in managed mode
            if "Managed" in output:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Interface {Style.RESET_ALL}{Fore.CYAN}{iface}{Style.RESET_ALL}{Fore.YELLOW} is now in managed mode!{Style.RESET_ALL}"
                )

            else:
                print(
                    f"{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.YELLOW} Interface {Style.RESET_ALL}{Fore.CYAN}{iface}{Style.RESET_ALL}{Fore.YELLOW} is not in managed mode!{Style.RESET_ALL}"
                )
