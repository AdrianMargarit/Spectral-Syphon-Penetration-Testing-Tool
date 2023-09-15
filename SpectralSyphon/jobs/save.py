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
import sys
import subprocess
from colorama import Fore, Back, Style


def save(cmd, filename):
    # Save the output of the command to a file in the 'saves' folder in the project directory
    path = "./SpectralSyphon/saves/"

    # Check if the 'saves' folder exists
    os.makedirs(path, exist_ok=True)

    # Create the complete path to the file
    file_path = os.path.join(path, filename)

    try:
        os.system(f"python3 run.py {cmd} > {file_path}")

    except Exception as e:
        e = sys.exc_info()[1]
        print(f"{Fore.RED}[!!!] Error: {e}{Style.RESET_ALL}")

    else:
        print(
            f"{Fore.GREEN}[+++]{Style.RESET_ALL}{Fore.RED} File saved successfully as {Style.RESET_ALL}{Fore.CYAN}{filename}!{Style.RESET_ALL}"
        )
