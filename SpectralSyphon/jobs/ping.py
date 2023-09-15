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
from scapy.all import *
from colorama import Fore, Back, Style
from jobs.servicename import servicename_conv


def ping(host, host_count):
    try:
        print(
            f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Pinging {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}"
        )
        ip = servicename_conv(host)
        icmp = IP(dst=ip) / ICMP()
        resp = sr1(icmp, timeout=10, verbose=False)

        if resp == None:
            if host_count > 0:
                print(
                    f"\n{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.RED}is down{Style.RESET_ALL}"
                )

            else:
                print(
                    f"{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.RED}is down{Style.RESET_ALL}"
                )

        else:
            if host_count > 0:
                print(
                    f"\n{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.GREEN}is up{Style.RESET_ALL}"
                )

            else:
                print(
                    f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.GREEN}is up{Style.RESET_ALL}"
                )

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] User aborted{Style.RESET_ALL}")
        sys.exit("^C\n")
