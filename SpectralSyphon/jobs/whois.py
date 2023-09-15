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

import whois
import sys
from colorama import Fore, Back, Style


# Check if the whois information is a list or not
def info_whois(host):
    try:
        print(
            f"{Fore.GREEN}[***]{Style.RESET_ALL}{Fore.RED} Whois information for {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}"
        )
        who_is = whois.whois(host)

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        # Checking for the domain name
        if isinstance(who_is.domain_name, str):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Domain name: {Style.RESET_ALL}{Fore.CYAN}{who_is.domain_name}{Style.RESET_ALL}"
            )

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Domain names: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.domain_name)

        # Checking for the registrar
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Registrar: {Style.RESET_ALL}{Fore.CYAN}{who_is.registrar}{Style.RESET_ALL}"
        )

        # Checking for the whois server
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Whois server: {Style.RESET_ALL}{Fore.CYAN}{who_is.whois_server}{Style.RESET_ALL}"
        )

        # Checking for the name servers
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Servers names:{Style.RESET_ALL}"
        )
        check_whois(host, who_is.name_servers)

        # Checking for the creation date
        if isinstance(who_is.creation_date, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Creation date: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.creation_date)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Creation date: {Style.RESET_ALL}{Fore.CYAN}{who_is.creation_date}{Style.RESET_ALL}"
            )

        # Checking for the updated date
        if isinstance(who_is.updated_date, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Updated date: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.updated_date)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Updated date: {Style.RESET_ALL}{Fore.CYAN}{who_is.updated_date}{Style.RESET_ALL}"
            )

        # Checking for the expiration date
        if isinstance(who_is.expiration_date, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Expiration date: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.expiration_date)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Expiration date: {Style.RESET_ALL}{Fore.CYAN}{who_is.expiration_date}{Style.RESET_ALL}"
            )

        # Checking for the status
        print(f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Status: {Style.RESET_ALL}")
        check_whois(host, who_is.status)

        # Checking for the emails
        if isinstance(who_is.emails, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Emails: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.emails)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Emails: {Style.RESET_ALL}{Fore.CYAN}{who_is.emails}{Style.RESET_ALL}"
            )

        # Checking for the organization
        if isinstance(who_is.org, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Organization: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.org)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Organization: {Style.RESET_ALL}{Fore.CYAN}{who_is.org}{Style.RESET_ALL}"
            )

        # Checking for the address
        if isinstance(who_is.address, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Address: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.address)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Address: {Style.RESET_ALL}{Fore.CYAN}{who_is.address}{Style.RESET_ALL}"
            )

        # Checking for the city
        if isinstance(who_is.city, list):
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} City: {Style.RESET_ALL}"
            )
            check_whois(host, who_is.city)

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} City: {Style.RESET_ALL}{Fore.CYAN}{who_is.city}{Style.RESET_ALL}"
            )

        # Checking for the state
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} State: {Style.RESET_ALL}{Fore.CYAN}{who_is.state}{Style.RESET_ALL}"
        )

        # Checking for the zipcode
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Zip code: {Style.RESET_ALL}{Fore.CYAN}{who_is.zipcode}{Style.RESET_ALL}"
        )

        # Checking for the country
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Country: {Style.RESET_ALL}{Fore.CYAN}{who_is.country}{Style.RESET_ALL}"
        )


# Function to check if the value is a list or not
def check_whois(host, dictionary):
    try:
        length = len(dictionary)

    except:
        print(
            f"\t{Fore.GREEN}[+++]{Style.RESET_ALL} {Fore.CYAN}{dictionary}{Style.RESET_ALL}"
        )

    else:
        for value in dictionary:
            print(
                f"\t{Fore.GREEN}[+++]{Style.RESET_ALL} {Fore.CYAN}{value}{Style.RESET_ALL}"
            )
