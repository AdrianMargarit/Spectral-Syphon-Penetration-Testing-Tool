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
import struct
import binascii
import sys
import os
from colorama import Fore, Back, Style


def packet_sniffer():
    # Check if the user is running the script as root/sudo, and if not exit
    if not "SUDO_UID" in os.environ.keys():
        print(
            f"{Fore.RED}[!!!] You need to be root or sudo to run this script!{Style.RESET_ALL}"
        )
        sys.exit()

    try:
        raw_socket = socket.socket(
            socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800)
        )

    except socket.error as e:
        print(f"{Fore.RED}[!!!] Error: {e[1]}{Style.RESET_ALL}")
        sys.exit()

    except KeyboardInterrupt:
        print(f"{Fore.RED}[!!!] User interrupted the script!{Style.RESET_ALL}")
        sys.exit()

    else:
        while True:
            try:
                packet = raw_socket.recvfrom(2048)
                ethernet_header = packet[0][0:14]
                eth_header = struct.unpack("!6s6s2s", ethernet_header)
                print(
                    f'\nDestination MAC: {binascii.hexlify(eth_header[0]).upper().decode("utf-8")}, Source MAC: {binascii.hexlify(eth_header[1]).upper().decode("utf-8")}, Protocol: {binascii.hexlify(eth_header[2]).upper().decode("utf-8")}'
                )
                ip_header = packet[0][14:34]
                ip_hdr = struct.unpack("!12s4s4s", ip_header)
                print(
                    f"Source IP: {socket.inet_ntoa(ip_hdr[1])}, Destination IP: {socket.inet_ntoa(ip_hdr[2])}"
                )

            except KeyboardInterrupt:
                print(f"{Fore.RED}[!!!] User interrupted the script!{Style.RESET_ALL}")
                sys.exit("\n")

            except Exception as e:
                print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
                sys.exit()
