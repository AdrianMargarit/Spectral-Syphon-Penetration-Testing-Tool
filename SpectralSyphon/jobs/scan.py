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

import nmap
import sys
import os
import multiprocessing
import socket
from colorama import Fore, Back, Style

scanner = nmap.PortScanner()


def status_scan(host, inputted):
    try:
        scanner.scan(host, "1", "-v -sT")

    except KeyboardInterrupt:
        sys.exit("\n^C\n")

    except Exception as e:
        e = sys.exc_info()
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

    else:
        if scanner[host].state() == "up":
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.RED}is {scanner[host].state()}{Style.RESET_ALL}"
            )

        else:
            print(
                f"{Fore.RED}[---]{Style.RESET_ALL}{Fore.CYAN} {host} {Style.RESET_ALL}{Fore.RED}is {scanner[host].state()}{Style.RESET_ALL}"
            )
            sys.exit()


def scan(host, inputted, portstart, portend, scantype):
    status_scan(host, inputted)
    print("Scan commencing. To cancel scan press Ctrl+C.")

    try:
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Scan started at {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.YELLOW}, at {Style.RESET_ALL}{Fore.CYAN}{scantype}{Style.RESET_ALL}{Fore.YELLOW} scan type, on ports {Style.RESET_ALL}{Fore.CYAN}{portstart}-{portend}{Style.RESET_ALL}{Fore.YELLOW}. To cancel scan press Ctrl+C.{Style.RESET_ALL}"
        )
        scanner.scan(host, f"{portstart}-{portend}", f"-v {scantype}")

    except KeyboardInterrupt:
        sys.exit("\n^C\n")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        if len(scanner[host].all_protocols()) == 0:
            print(f"{Fore.RED}[!!!] No ports were found open.{Style.RESET_ALL}")

        else:
            for protocol in scanner[host].all_protocols():
                if scanner[host][protocol].keys():
                    print(f"\nProtocol: {protocol.upper()}")
                    print(
                        f"\n {Fore.GREEN}PORT{Style.RESET_ALL}    \t\t{Fore.CYAN}STATE{Style.RESET_ALL}    \t\t{Fore.YELLOW}SERVICE{Style.RESET_ALL}"
                    )
                    for port in scanner[host][protocol].keys():
                        print(
                            f' {Fore.GREEN}{port}{Style.RESET_ALL}    \t\t{Fore.CYAN}{scanner[host][protocol][port]["state"]}{Style.RESET_ALL}    \t\t{Fore.YELLOW}{scanner[host][protocol][port]["name"]}{Style.RESET_ALL}'
                        )


def port_scan(host, inputted, int, i, j, scantype):
    try:
        if j == 0:
            status_scan(host, inputted)
            print("Scan commencing. To cancel scan press Ctrl+C.")
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Scan started at {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}"
            )

        scanner.scan(host, f"{int}", f"-v {scantype}")

    except KeyboardInterrupt:
        sys.exit("\n^C\n")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        for protocol in scanner[host].all_protocols():
            if scanner[host][protocol].key():
                if j == 0:
                    print(f"\nProtocol: {protocol.upper()}")
                    print(
                        f"\n {Fore.GREEN}PORT{Style.RESET_ALL}    \t\t{Fore.CYAN}STATE{Style.RESET_ALL}    \t\t{Fore.YELLOW}SERVICE{Style.RESET_ALL}"
                    )

                for port in scanner[host][protocol].keys():
                    print(
                        f' {Fore.GREEN}{port}{Style.RESET_ALL}    \t\t{Fore.CYAN}{scanner[host][protocol][port]["state"]}{Style.RESET_ALL}    \t\t{Fore.YELLOW}{scanner[host][protocol][port]["name"]}{Style.RESET_ALL}'
                    )


def devices_scan():
    network = input("Enter the network address: ")
    print(f"The network address is {network}")

    try:
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Scan started for devices on network {Style.RESET_ALL}{Fore.CYAN}{network}{Style.RESET_ALL}"
        )
        scanner.scan(hosts=network, arguments="-v -sn")

    except KeyboardInterrupt:
        sys.exit("\n^C\n")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        for host in scanner.all_hosts():
            if scanner[host]["status"]["state"] == "up":
                try:
                    if len(scanner[host]["vendor"]) == 0:
                        try:
                            print(
                                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host}{Style.RESET_ALL}    \t {Fore.YELLOW}{socket.gethostbyaddr(host)[0]}{Style.RESET_ALL}"
                            )

                        except:
                            print(
                                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host}{Style.RESET_ALL}"
                            )

                    else:
                        try:
                            print(
                                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host}{Style.RESET_ALL}    \t {Fore.RED}{scanner[host]["vendor"]}{Style.RESET_ALL}    \t {Fore.YELLOW}{socket.gethostbyaddr(host)[0]}{Style.RESET_ALL}'
                            )

                        except:
                            print(
                                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host}{Style.RESET_ALL}    \t {Fore.RED}{scanner[host]["vendor"]}{Style.RESET_ALL}'
                            )

                except:
                    print(
                        f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.CYAN} {host}{Style.RESET_ALL}    \t {Fore.RED}{scanner[host]["vendor"]}{Style.RESET_ALL}'
                    )
