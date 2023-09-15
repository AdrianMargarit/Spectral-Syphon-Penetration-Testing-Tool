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
directories_found = []


def directory_scanner(host):
    global q
    while True:
        try:
            # Fetch the next directory from the queue
            directory = q.get()

            # Start scanning the directory
            url = f"http://{host}/{directory}"
            requests.get(url)

        except requests.ConnectionError:
            pass

        except KeyboardInterrupt:
            print(f"{Fore.RED}[---] Exiting...{Style.RESET_ALL}")
            sys.exit("^C\n")

        except Exception as e:
            print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

        else:
            if requests.get(url).status_code != 404:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} Found directory: {Style.RESET_ALL}{Fore.CYAN}{url}{Style.RESET_ALL}"
                )

                # Adding the directory to the list of found directories
                with list_lock:
                    directories_found.append(url)

        # Mark the task as done
        q.task_done()


def main(host, threads, directories):
    global q
    print(
        f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Starting directory busting on {Style.RESET_ALL}{Fore.CYAN}{host}{Style.RESET_ALL}{Fore.YELLOW}...\nThis might take a while...\nIf you wish to abort, press CTRL+C to exit...{Style.RESET_ALL}"
    )

    # Fill the queue with directories
    try:
        for directory in directories:
            q.put(directory)

        for thread in range(threads):
            # Starting the threads
            worker = Thread(target=directory_scanner, args=(host,))

            # Daemonize the threads
            worker.daemon = True
            worker.start()

    except KeyboardInterrupt:
        print(f"{Fore.RED}[---] Exiting...{Style.RESET_ALL}")
        sys.exit("^C\n")

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")


def directory_bust(host, wordlist):
    threads = 8

    try:
        main(host=host, threads=threads, directories=open(wordlist).read().splitlines())
        q.join()

        if len(directories_found) > 0:
            if len(directories_found) == 1:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Found {Style.RESET_ALL}{Fore.CYAN}{len(directories_found)}{Style.RESET_ALL}{Fore.YELLOW} directory!{Style.RESET_ALL}"
                )
            else:
                print(
                    f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.YELLOW} Found {Style.RESET_ALL}{Fore.CYAN}{len(directories_found)}{Style.RESET_ALL}{Fore.YELLOW} directories!{Style.RESET_ALL}"
                )
        else:
            print(
                f"{Fore.RED}[---]{Style.RESET_ALL}{Fore.YELLOW} No directories found!{Style.RESET_ALL}"
            )

    except KeyboardInterrupt:
        print(f"{Fore.RED}[---] Exiting...{Style.RESET_ALL}")
        sys.exit("^C\n")

    except Exception as e:
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")
