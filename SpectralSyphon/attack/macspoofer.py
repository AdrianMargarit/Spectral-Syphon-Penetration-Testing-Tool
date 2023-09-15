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


def mac_spoofer(mac, iface, default_iface=""):
    # Check if user is root/sudo or not, if not exit
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        if default_iface != "":
            iface = default_iface
            subprocess.call(["sudo", "ifconfig", iface, "down"])
            subprocess.call(["sudo", "ifconfig", iface, "hw", "ether", mac])
            subprocess.call(["sudo", "ifconfig", iface, "up"])

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        output = str(
            subprocess.check_output(
                [
                    "ifconfig",
                    iface,
                ]
            )
        )

        if f"{mac}" in output:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} MAC address changed to {Style.RESET_ALL}{Fore.CYAN}{mac}{Style.RESET_ALL}{Fore.RED} on {Style.RESET_ALL}{Fore.CYAN}{iface}{Style.RESET_ALL}"
            )
        else:
            print(
                f"{Fore.RED}[!!!] Error: MAC address could not be changed{Style.RESET_ALL}"
            )
