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
import requests
import ipinfo
from colorama import Fore, Back, Style


def service_name(host, api_key):
    try:
        print(
            f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Getting service name for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}"
        )
        api_key = api_key
        handler = ipinfo.getHandler(api_key)
        addr = socket.gethostbyname(host)
        name = socket.gethostbyaddr(host)
        details = handler.getDetails(addr)

    except Exception as e:
        e = sys.exc_info()[1]
        print(
            f"{Fore.RED}[!!!]{Style.RESET_ALL}{Fore.RED} Error: {Style.RESET_ALL}{Fore.CYAN}{e}{Style.RESET_ALL}"
        )

    else:
        try:
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Service name for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{name[0]}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} IP address for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{addr}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Country for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.country_name}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} City for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.city}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Postal code for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.postal}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Organization for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.org}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Location for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.loc}{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Timezone for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.RED} is {Style.RESET_ALL}{Fore.CYAN}{details.timezone}{Style.RESET_ALL}"
            )

        except Exception as e:
            pass


# This function will return the IP address of an URL
def servicename_conv(host):
    try:
        return socket.gethostbyname(host)

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] Exiting...{Style.RESET_ALL}")
        sys.exit("^C\n")


# This function will return the URL of an IP address
def servicename_convurl(host):
    try:
        return socket.gethostbyaddr(host)

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] Exiting...{Style.RESET_ALL}")
        sys.exit("^C\n")
