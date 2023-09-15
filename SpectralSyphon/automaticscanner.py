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

# Importing configuration module
from cfg.config import *

# Importing basic modules
from jobs.banner import *
from jobs.directorybuster import *
from jobs.scan import *
from jobs.servicename import *
from jobs.subdomenum import *
from jobs.vulnerabilityscanner import *
from jobs.whois import *


# Function defined for automatic scanning of a target (domain or IP)
def auto_scanner(target):
    try:
        print(
            f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Starting automatic scan for {Style.RESET_ALL}{Fore.CYAN}{target}{Style.RESET_ALL}{Fore.RED}...{Style.RESET_ALL}"
        )

        # Whois
        info_whois(target)

        # Service name
        service_name(target, IPINFO_API_KEY)

        # Subdomain enumeration
        subdomain_enumeration(target, SUBDOMAINS_WORDLIST)

        # Directory buster
        directory_bust(target, DIRECTORIES_WORDLIST)

        # Vulnerability scanner
        vulnerability_scanner(target, SHODAN_API_KEY)

    except KeyboardInterrupt:
        print(
            f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Stopping automatic scan for {Style.RESET_ALL}{Fore.CYAN}{target}{Style.RESET_ALL}{Fore.RED}...{Style.RESET_ALL}"
        )
        sys.exit()

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
