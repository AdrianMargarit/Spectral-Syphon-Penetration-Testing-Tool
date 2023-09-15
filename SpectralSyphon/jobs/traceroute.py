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
from colorama import Fore, Back, Style


def tracert(host, maxhops=30, timeout=0.2):
    proto_icmp = socket.getprotobyname("icmp")
    proto_udp = socket.getprotobyname("udp")
    host_addr = socket.gethostbyname(host)
    port = 33434

    for ttl in range(1, maxhops):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx.settimeout(timeout)
        rx.bind(("", port))

        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto("".encode(), (host_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]

        except socket.error:
            curr_addr = None

        finally:
            rx.close()
            tx.close()

        yield curr_addr

        if curr_addr == host:
            break


def traceroute(host):
    try:
        host_addr = socket.gethostbyname(host)
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Tracing route to {Style.RESET_ALL}{Fore.CYAN}{host_addr} from {host} over a maximum of 30 hops..."
        )

        for i, j in enumerate(tracert(host_addr)):
            if j == None:
                print(
                    f"{Fore.GREEN}[{i+1}]{Style.RESET_ALL}{Fore.YELLOW}\t{j}{Style.RESET_ALL}"
                )

            else:
                try:
                    host = socket.gethostbyaddr(j)
                    print(
                        f"{Fore.GREEN}[{i+1}]{Style.RESET_ALL}{Fore.YELLOW}\t{j}{Style.RESET_ALL} {Fore.CYAN}({host[0]}){Style.RESET_ALL}"
                    )

                except Exception:
                    print(
                        f"{Fore.GREEN}[{i+1}]{Style.RESET_ALL}{Fore.YELLOW}\t{j}{Style.RESET_ALL}"
                    )

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        sys.exit("^C\n")
