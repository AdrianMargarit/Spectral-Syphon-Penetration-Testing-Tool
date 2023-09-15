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

###########################################################################

# This file contains the configuration for the program

###########################################################################


# API keys for the services used by the program
IPINFO_API_KEY = 'b86dabc2a55151'
SHODAN_API_KEY = 'xcahippZkG235ZoyGe9fA0q8aIYKxkcN'

# Wordlists for the bruteforce attack, subdomains and directories
PASSWORDS_WORDLIST = 'dict/Top-10000-Passwords.txt'
SUBDOMAINS_WORDLIST = 'dict/Top-100-Subdomains.txt'
DIRECTORIES_WORDLIST = 'dict/Top-200000-Directories.txt'

# Wireless interface - Default
WIRELESS_INTERFACE_DEF = ''

# Dictionary for DNS mapping
DNS_MAPPING = {
    'www.google.com.': '192.168.1.100',
    'google.com.': '192.168.1.100',
    'facebook.com.': '172.217.19.142'
}
