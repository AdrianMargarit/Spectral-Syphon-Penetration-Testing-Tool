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
from colorama import Fore, Back, Style


def fetch_mac(host_ip, host_count):
    # Checking to see if user has root/sudo privileges
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        if host_count > 6:
            print(
                f"\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Trying to fetch the MAC address of {Style.RESET_ALL}{Fore.CYAN}{host_ip}{Style.RESET_ALL}{Fore.YELLOW} hosts...{Style.RESET_ALL}"
            )
        else:
            print(
                f"\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Trying to fetch the MAC address of {Style.RESET_ALL}{Fore.CYAN}{host_ip}{Style.RESET_ALL}{Fore.YELLOW} host...{Style.RESET_ALL}"
            )

        # Continue from here
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op="who-has", pdst=host_ip)
        resp, _ = srp(packet, timeout=2, retry=10, verbose=False)

        if resp:
            for _, r in resp:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} MAC address of {Style.RESET_ALL}{Fore.CYAN}{host_ip}{Style.RESET_ALL}{Fore.YELLOW} is {Style.RESET_ALL}{Fore.CYAN}{r[Ether].src.upper()}{Style.RESET_ALL}"
                )
        else:
            print(
                f"{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.YELLOW} No response from {Style.RESET_ALL}{Fore.CYAN}{host_ip}{Style.RESET_ALL}"
            )

    except Exception as e:
        print(f"{Fore.RED}[!!!] An error occured: {e}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] User interrupted the script!{Style.RESET_ALL}")
        sys.exit("^C\n")
