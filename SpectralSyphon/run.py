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

import argparse
import os
import sys
import ipaddress
import textwrap
from colorama import Fore, Back, Style

# Importing from cfg.config
from cfg.config import *

# Importing offensive modules
from attack.arpspoofer import *
from attack.bruteforcer import *
from attack.deauthentication import *
from attack.dnsspoofer import *
from attack.ipspoofer import *
from attack.macspoofer import *
from attack.packetsniffer import *
from attack.synflooder import *

# Importing basic modules
from jobs.banner import *
from jobs.directorybuster import *
from jobs.fetchmac import *
from jobs.ifacemode import *
from jobs.ifconfig import *
from jobs.ping import *
from jobs.save import *
from jobs.scan import *
from jobs.servicename import *
from jobs.subdomenum import *
from jobs.traceroute import *
from jobs.vulnerabilityscanner import *
from jobs.whois import *

from automaticscanner import *

ap = argparse.ArgumentParser(
    description="Spectral Syphon - Packet sniffer",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent(
        """
Examples:
    >>> -ifconfig
    >>> -ping <HOST(s) IP/URL>
    >>> -traceroute <HOST(s) IP/URL>
    >>> -scan -host <HOST(s) IP/URL> -prange <START PORT> <END PORT>
    >>> -scanlan
    >>> -fetchmac -host <HOST(s) IP/URL>
    >>> -grab -host <HOST(s) IP/URL> -p <PORT(s)>
    >>> -servicename <HOST(s) IP/URL>
    >>> -whois <HOST(s) IP/URL>
    >>> -subdomenum <DOMAIN>
    >>> -subdomenum <DOMAIN> -wordlist <WORDLIST-PATH>
    >>> -directorybuster <HOST(s) IP/URL> -wordlist <WORDLIST-PATH>
    >>> -vulnerabilityscanner -host <HOST(s) IP/URL>
    >>> -sniff
    >>> -macspoofer -iface <INTERFACE> -source <SOURCE-MAC>
    >>> -ipspoofer -source <SOURCE-IP> <SOURCE-PORT> -target <TARGET-IP/URL> <TARGET-PORT>
    >>> -synflooder -source <SOURCE-PORT> -target <TARGET-IP/URL> <TARGET-PORT>
    >>> -deauthentication -iface <INTERFACE> -target <TARGET-MAC> -gateway <GATEWAY-MAC>
    >>> -bruteforcer <SERVICE> -target <TARGET-IP/URL> -user <USERNAME>
    >>> -bruteforcer <SERVICE> -target <TARGET-IP/URL> -user <USERNAME> -wordlist <WORDLIST-PATH>
    >>> -automaticscanner <HOST(s) IP/URL>
    >>> -mode <MODE> -iface <INTERFACE>
"""
    ),
)

ap.add_argument(
    "-ifconfig", 
    action="store_true", 
    help="Show the current network setup"
)

ap.add_argument(
    "-ping",
    type=str,
    nargs="+",
    help="Checking host availability by sending ICMP packets",
)

ap.add_argument(
    "-traceroute",
    nargs=1,
    help="Trace the route to the host and display network latency",
)

ap.add_argument(
    "-servicename",
    type=str,
    nargs="+",
    help="Get the domain name service and/or IP address of a host",
)

ap.add_argument(
    "-whois", 
    type=str, 
    nargs="+", 
    help="Get the whois information of a host"
)

ap.add_argument(
    "-subdomenum", 
    type=str, 
    nargs=1, 
    help="Enumerate subdomains of a domain"
)

ap.add_argument(
    "-directorybuster", 
    type=str, 
    nargs=1, 
    help="Busting directories of a host"
)

ap.add_argument(
    "-scantcp", 
    action="store_true", 
    help="Scan TCP ports"
)

ap.add_argument(
    '-scanudp',
    action = 'store_true',
    help = 'Scan UDP ports. Must be root'
)

ap.add_argument(
    '-scanack',
    action = 'store_true',
    help = 'Scan ACK ports'
)

ap.add_argument(
    '-scansyn',
    action = 'store_true',
    help = 'Scan SYN ports. Must be root'
)

ap.add_argument(
    '-scan',
    action = 'store_true',
    help = 'Scan all ports. Must be root'
)

ap.add_argument(
    '-scanlan',
    action = 'store_true',
    help = 'Scan all hosts in the LAN'
)

ap.add_argument(
    '-vulnerabilityscanner',
    action = 'store_true',
    help = 'Scan for vulnerabilities'
)

ap.add_argument(
    '-fetch',
    action = 'store_true',
    help = 'Fetch the banner of a service'
)

ap.add_argument(
    '-fetchmac',
    action = 'store_true',
    help = 'Fetch the MAC address of a host. Must be root'
)

ap.add_argument(
    '-macspoofer',
    action = 'store_true',
    help = 'Spoof the MAC address of a host. Must be root'
)

ap.add_argument(
    '-ipspoofer',
    action = 'store_true',
    help = 'Spoof the IP address of a host. Must be root'
)

ap.add_argument(
    '-synflooder',
    action = 'store_true',
    help = 'Perform a SYN flood attack. Must be root'
)

ap.add_argument(
    '-sniff',
    action = 'store_true',
    help = 'Sniff packets. Must be root'
)

ap.add_argument(
    '-deauthentication',
    action = 'store_true',
    help = 'Perform a deauthentication attack. Must be root'
)

ap.add_argument(
    '-bruteforcer',
    nargs = 1,
    help = 'Perform a bruteforce attack'
)

ap.add_argument(
    '-automaticscanner',
    nargs = '+',
    help = 'Perform an automatic scan'
)

ap.add_argument(
    '-mode',
    '-m',
    type = str,
    nargs = 1,
    help = 'Set the interface mode. Must be root'
)

ap.add_argument(
    '-save',
    '-s',
    type = str,
    nargs = 1,
    help = 'Save the output to a file'
)

ap.add_argument(
    '-host',
    type = str,
    nargs = '+',
    help = 'Set the host/s'
)

ap.add_argument(
    '-iprange',
    type = str,
    nargs = 2,
    help = 'Set the IP range'
)

ap.add_argument(
    '-p',
    type = int,
    nargs = '+',
    help = 'Set the port/s'
)

ap.add_argument(
    '-portrange',
    type = int,
    default = [1-1000],
    nargs = 2,
    help = 'Set the port range'
)

ap.add_argument(
    '-source',
    '-src',
    type = str,
    nargs = '+',
    help = 'Set the source'
)

ap.add_argument(
    '-target',
    '-t',
    type = str,
    nargs = '+',
    help = 'Set the target/s'
)

ap.add_argument(
    '-gateway',
    '-g',
    type = str,
    nargs = '+',
    help = 'Set the gateway'
)

ap.add_argument(
    '-iface',
    '-i',
    type = str,
    nargs = 1,
    help = 'Set the interface'
)

ap.add_argument(
    '-user',
    '-u',
    type = str,
    nargs = 1,
    help = 'Set the username'
)

ap.add_argument(
    '-wordlist',
    '-w',
    type = str,
    nargs = 1,
    help = 'Set the wordlist'
)

args = vars(ap.parse_args())

# Handling the all of the scans
def scanHandler(scantype):
    if args['host']:
        # Scanning IP addresses
        if not args['p'] and not len(args['portrange']) == 2:
            for i in range (0, len(args['host'])):
                scan(servicename_conv(args['host'][i]), args['host'][i], 1, 1000, f'{scantype} scan')

        # Scanning ports and IP addresses
        elif args['p'] and not len(args['portrange']) == 2:
            for i in range (0, len(args['host'])):
                for j in range(0, len(args['p'])):
                    port_scan(servicename_conv(args['host'][i]), args['host'][i], args['p'][j], i, j, f'{scantype} scan')
                    
        # Scanning ports and IP addresses in a range
        elif len(args['portrange']) == 2 and not args['p']:
            for i in range (0, len(args['host'])):
                scan(servicename_conv(args['host'][i]), args['host'][i], args['portrange'][0], args['portrange'][1], f'{scantype} scan')
                
        else:
            print(f'{Fore.RED}[!!!] Error: Invalid arguments!{Style.RESET_ALL}')
            
    else:
        print(f'{Fore.RED}[!!!] Error: Invalid arguments!{Style.RESET_ALL}')
        
# Saving the results to a file
if args['save']:
    argsList = sys.argv[1:]
    filenameIndex = argsList.index('-s') + 1
    argsList.pop(filenameIndex)
    argsList.remove('-s')
    comm = ' '.join(argsList)
    save(f'{comm}', args['save'][0])
    
# Checking IP configuration
elif args['ifconfig']:
    ifconfig()
    
# Domain name service check/IP address checkx
elif args['servicename']:
    try:
        for i in range (0, len(args['servicename'])):
            service_name(args['servicename'][i], IPINFO_API_KEY)
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Whois information
elif args['whois']:
    try:
        for i in range (0, len(args['whois'])):
            info_whois(args['whois'][i])
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Subdomain enumeration
elif args['subdomenum']:
    try:
        if args['wordlist']:
            subdomain_enumeration(args['subdomenum'][0], args['wordlist'])
            
        else:
            subdomain_enumeration(args['subdomenum'][0], SUBDOMAINS_WORDLIST)
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Directory buster
elif args['directorybuster']:
    try:
        if args['wordlist']:
            directory_bust(args['directorybuster'][0], args['wordlist'])
            
        else:
            directory_bust(args['directorybuster'][0], DIRECTORIES_WORDLIST)
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Ping
elif args['ping']:
    try:
        for i in range (0, len(args['ping'])):
            ping(args['ping'][i], i)
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Traceroute
elif args['traceroute']:
    try:
        traceroute(args['traceroute'][0])
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Scans
# TCP scan
elif args['scantcp']:
    scanHandler('-stcp')
    
# UDP scan
elif args['scanudp']:
    scanHandler('-sudp')
    
# ACK scan
elif args['scanack']:
    scanHandler('-sack')
    
# SYN scan
elif args['scansyn']:
    scanHandler('-ssyn')
    
# All ports scan
elif args['scan']:
    scanHandler('-all')
    
# LAN scan
elif args['scanlan']:
    devices_scan()
    
# Vulnerability scanner
elif args['vulnerabilityscanner']:
    try:
        if args['host']:
            for i in range (0, len(args['host'])):
                vulnerability_scanner(args['host'][i], SHODAN_API_KEY)
                if len(args['host']) > 1:
                    print('\n')
                    
        elif args['iprange']:
            for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                vulnerability_scanner(ipaddress.IPv4Address(ip_int), SHODAN_API_KEY)
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
            
# Fetching the MAC address of a host
elif args['fetchmac']:
    try:
        for i in range (0, len(args['host'])):
            fetch_mac(args['host'][i], i)
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Fetching the banner of a service
elif args['fetch']:
    try:
        if args['host']:
            # Fetching the banner of a service on a specific port and IP address
            if args['p'] and not len(args['portrange']) == 2:
                for i in range (0, len(args['host'])):
                    for j in range(0, len(args['p'])):
                        banner_port(servicename_conv(args['host'][i]), args['p'][j])
                        
            # Fetching the banner of a service on a specific port range and IP address
            elif len(args['portrange']) == 2 and not args['p']:
                for i in range (0, len(args['host'])):
                    for j in range (args['portrange'][0], args['portrange'][1] + 1):
                        banner_port(servicename_conv(args['host'][i]), j)
                        
        elif args['iprange']:
            # Fetching the banner of a service on a specific port and IP address range
            if args['p'] and not len(args['portrange']) == 2:
                for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                    for j in range(0, len(args['p'])):
                        banner_port(ipaddress.IPv4Address(ip_int), args['p'][j])
                        
            # Fetching the banner of a service on a specific port range and IP address range
            elif len(args['portrange']) == 2 and not args['p']:
                for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                    for j in range (args['portrange'][0], args['portrange'][1] + 1):
                        banner_port(ipaddress.IPv4Address(ip_int), j)
                        
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Spoofing the MAC address of a host
elif args['macspoofer']:
    try:
        if args['iface'][0].lower() == 'd':
            mac_spoofer(args['source'][0], args['iface'][0], WIRELESS_INTERFACE_DEF)
            
        else:
            mac_spoofer(args['source'][0], args['iface'][0])
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')

# Spoofing the IP address of a host
elif args['ipspoofer']:
    try:
        ipspoofer(args['source'][0], args['source'][1], servicename_conv(args['target'][0]), int(args['target'][1]))
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# SYN flood attack
elif args['synflooder']:
    try:
        syn_flooder(args['source'][0], args['target'][0], args['target'][1])
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Sniffing packets
elif args['sniff']:
    packet_sniffer()
    
# Deauthentication attack
elif args['deauthentication']:
    try:
        if args['iface'][0].lower() == 'd':
            deauthentication(args['iface'][0], args['target'][0], args['gateway'][0], WIRELESS_INTERFACE_DEF)
            
        else:
            deauthentication(args['iface'][0], args['target'][0], args['gateway'][0])
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Bruteforce attack
elif args['bruteforcer']:
    try:
        if args['wordlist']:
            bruteforce(args['bruteforcer'][0], args['target'][0], args['user'][0], args['wordlist'][0])
            
        else:
            bruteforce(args['bruteforcer'][0], args['target'][0], args['user'][0], PASSWORDS_WORDLIST)
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Automatic scan
elif args['automaticscanner']:
    try:
        for i in range (0, len(args['automaticscanner'])):
            auto_scanner(args['automaticscanner'][i])
    
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
# Setting the interface mode
elif args['mode']:
    try:
        if args['mode'][0].lower() == 'monitor':
            if args['iface'][0].lower() == 'd':
                monitor_mode(args['iface'][0], WIRELESS_INTERFACE_DEF)
                
            else:
                monitor_mode(args['iface'][0])
                
        elif args['mode'][0].lower() == 'managed':
            if args['iface'][0].lower() == 'd':
                managed_mode(args['iface'][0], WIRELESS_INTERFACE_DEF)
                
            else:
                managed_mode(args['iface'][0])
            
        else:
            print(f'{Fore.RED}[!!!] Error: Interface mode can only be "monitor" or "managaed" at a single given time!{Style.RESET_ALL}')
            
    except Exception as e:
        print(f'{Fore.RED}[!!!] Error: Invalid argument!{Style.RESET_ALL}')
        
else:
    # If no arguments are given, print the help menu
    if len(sys.argv) > 1:
        print(f'{Fore.RED}[!!!] Error: Invalid arguments!{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}[***] Use -h or --help for help!{Style.RESET_ALL}')  