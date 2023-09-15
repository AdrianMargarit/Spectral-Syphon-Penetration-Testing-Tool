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

import socket
import sys
import multiprocessing
from colorama import Fore, Back, Style


def banner_port(host, port):
    socket.setdefaulttimeout(3)
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Trying to connect to {Style.RESET_ALL}{Fore.CYAN}{host}:{port}{Style.RESET_ALL}"
        )
        sckt.connect((host, port))
        sckt.send("IdentifyYourself\r\n".encode())
        banner = sckt.recv(1024)

    except KeyboardInterrupt:
        print(f"{Fore.RED}[---] Exiting...{Style.RESET_ALL}")
        sys.exit("^C\n")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        sckt.close()
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Host: {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Port: {Style.RESET_ALL}{Fore.CYAN}{port}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Banner: {Style.RESET_ALL}{Fore.CYAN}{banner.decode()}{Style.RESET_ALL}\n"
        )
