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

import os
import subprocess
import sys
import readline
from run import *
from startscreen import greetings
from colorama import Fore, Back, Style

hist_list = []
comm = ''

# Starting to read the commands


def commands_handler():
    global hist_list
    global comm
    while True:
        try:
            comm = input(f'\nSpectral_Siphon> ')
            if comm != 'history':
                hist_list.append(comm.strip())
            elif comm.strip() == 'clear':
                subprocess.call("clear", shell=True)
            if comm.strip() == 'history':
                if len(hist_list) > 0:
                    print('These were the last commands: ')
                    for i in range(0, len(hist_list)):
                        print(hist_list[i])
                else:
                    print('No commands in found history...')
            else:
                os.system(f'python3 run.py {comm}')
        except KeyboardInterrupt:
            sys.exit('\n^C\n')

# Main function


def main():
    # Running the welcoming function, in the case of missing arguments
    if len(sys.argv) == 1:
        greetings()

    # Checking if the user is root
    if not 'SUDO_UID' in os.environ.keys():
        print(
            f'\nAttention: {Fore.RED}You must run this script as root!{Style.RESET_ALL}\n')

    # Running the commands_handler function
    commands_handler()


if __name__ == '__main__':
    main()
