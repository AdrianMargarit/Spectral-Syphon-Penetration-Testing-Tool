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

import requests
import sys
from threading import Thread, Lock
from queue import Queue
from colorama import Fore, Back, Style

q = Queue()
list_lock = Lock()
domains_found = []


# Function to scan the subdomains
def subdomain_discovery(domain):
    global q
    while True:
        try:
            # Fetch the subdomain from the queue
            subdomain = q.get()

            # Scan the subdomain
            url = f"http://{subdomain}.{domain}"
            requests.get(url)

        except requests.ConnectionError:
            pass

        except KeyboardInterrupt:
            sys.exit("^C")

        except Exception as e:
            print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

        else:
            print(
                f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Subdomain found: {Style.RESET_ALL}{Fore.CYAN}{url}{Style.RESET_ALL}"
            )

            # Add the newly found subdomain to the global list
            with list_lock:
                domains_found.append(url)

        # Mark the task as done
        q.task_done()


# Function to create the queue and the worker threads
def main(domain, threads, subdomains):
    global q
    print(
        f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Enumerating subdomains on {Style.RESET_ALL}{Fore.CYAN}{domain}{Style.RESET_ALL}{Fore.RED}!\nIf you want to cancel, press CTRL+C.\nStandby, this might take some time. Scanning for subdomains in {Style.RESET_ALL}{Fore.CYAN}{domain}{Style.RESET_ALL}{Fore.RED}...{Style.RESET_ALL}"
    )

    # Use the subdomains to create the queue
    try:
        for subdomain in subdomains:
            q.put(subdomain)

            for thread in range(threads):
                # Create the worker threads
                worker = Thread(target=subdomain_discovery, args=(domain,))

                # Daemonize the worker threads
                worker.daemon = True
                worker.start()

    except KeyboardInterrupt:
        sys.exit("^C")

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")


# Function to enumerate subdomains
def subdomain_enumeration(domain, wordlist):
    threads = 8

    try:
        main(
            domain=domain,
            threads=threads,
            subdomains=open(wordlist).read().splitlines(),
        )
        q.join()

        # Print the results
        if len(domains_found) > 0:
            if len(domains_found) == 1:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Found {Style.RESET_ALL}{Fore.CYAN}{len(domains_found)}{Style.RESET_ALL}{Fore.RED} subdomain!{Style.RESET_ALL}\n"
                )

            else:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Found {Style.RESET_ALL}{Fore.CYAN}{len(domains_found)}{Style.RESET_ALL}{Fore.RED} subdomains!{Style.RESET_ALL}\n"
                )

        else:
            print(
                f"{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED} No subdomains found!{Style.RESET_ALL}\n"
            )

    except KeyboardInterrupt:
        sys.exit("^C")

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
