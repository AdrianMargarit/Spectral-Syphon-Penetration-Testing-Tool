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

import random
import time
import subprocess
from colorama import Fore, Back, Style


# This function prints the splash screen of a ghost with the name of the application, the repository URL, the author, the version of the application and under what institution it what made
def splash_screen():
    print()
    print(f'{Fore.WHITE}                                     .▒▒░░░░▒▒─                                   {Style.RESET_ALL}')
    print(f'{Fore.WHITE}        ░                          ∩░░░░░░░░░░▒╫╖                                 {Style.RESET_ALL}')
    print(f'{Fore.WHITE} ░░░░░╓▄Q█▌ ░░░░░      ░░░░      ,▒░░░░░░░░░░░░░▓▄     ░░░░      ░░░ █▌▄╕   ░░░░░ {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ╒▄▓███▓▓                   ¿░░░▒░░░░░░░░░▒░░▓▓               Æ█▓███▄F        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}      ╚████▌                  .▒░░░░███W░░░▒▓██░░░▓Ç    ░,r▒▒─.    ,████▌         {Style.RESET_ALL}')
    print(f'{Fore.WHITE}        ╙▀███▌▄▄▒░░░░░▒─.   .▒░░░░░░███W░░░π███░░░▓▓gM▒░░░░░░░░▒▄▄███▀╙           {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ╙▀██████▌░░░░░▒─▒░░░░░░░░░▀░░░░░▒▀▀░░░░▓▓Ñ░░░░░░▒▄██████▀              {Style.RESET_ALL}')
    print(f'{Fore.WHITE}              ╢████▀░░░░░░░░░░░░░░░░░░▒▄▓▓▄▒░░░░░░▓▌░░░░░░░░█████▒                {Style.RESET_ALL}')
    print(f'{Fore.WHITE}             ┌▓▓▓▓▓░░░░░░░░░░░░░░░░░░░▓████░░░░░░░▐░░░░░░░░░▓▓▓▓▓░                {Style.RESET_ALL}')
    print(f'{Fore.WHITE}             ▓▓▓▓▓Ü░░░░░░░░░░░░░░░░░g█████▌▒░░░░░░░░░░░░░░░░▓▓▓▓▓░                {Style.RESET_ALL}')
    print(f'{Fore.WHITE}            ▐▓▓▓▓▓░░░░░░ƒ░░░░░░░░░░▐██████▌░░░░░░░░░░░░░░░░░▓▓▓▓▓░`               {Style.RESET_ALL}')
    print(f'{Fore.WHITE}            ▓▓▓▓▓▌░░░░░j▓░░░░░░░░░░▐██████▌░░░░░░░░░░░░░░░░░▓▓▓▓▓W`               {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ╟▓▓▓▓▓░░░░░░▓▓░░░░░░░░░░░░▀▀█▀▀░░░░░░░░░░░░░░░░░░▓▓▓▓▓▌░               {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ▓▓▓▓▓▓░░░▓░▐▓▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐▓▓▓▓▌░░              {Style.RESET_ALL}')
    print(f'{Fore.WHITE}          j▓▓▓▓▓▌░░▓▌]▓▓Ñ░¢░░░░░░░░░░░░░░░░░░░░░░░]░░░░░░░░░░▓▓▓▓▓░▒              {Style.RESET_ALL}')
    print(f'{Fore.WHITE}          ▐▓╩╙▓▓░░▓▓░▓▓▓░▓Ü░░░░░░░░░░░░░░░░░░░░░░░▓W░░░░░░░░░▓▓▓▓▓░▒              {Style.RESET_ALL}')
    print(f'{Fore.WHITE}       ░░     "▌░▓▓░╟▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░╖░░░░░▐▓▓▓▌░`   ░░░░       {Style.RESET_ALL}')
    print(f'{Fore.WHITE}               ░▐▓▌░▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░▐░░░░░╞`╙▀▒▒               {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                ⌠     ▐▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▒j▓░░░░░                    {Style.RESET_ALL}')
    print(f'{Fore.WHITE}       ░░░░      ░░░░ ▓▓Ñ░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▌ ` ░░░░      ░░░░       {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                      ▓▓Ü░░░░░░░░░░░░░░░░░░░▒░░░░░▓▓▓▓▓▓▓▓                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                      ▓▓Ü░░░░▐░░░░░░░╟░░░░░]▓░░░░░▓▓▓▓▓▓▓▓                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                     ]▓▓Ü░░░░▓Ü░░░░░░▓░░░░░▓▓░░░░░▓▓▓▓▓▓▓▓                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                     ]▓▓▌░░░▐▓▓░░░░░╫▓░░░░▓▓▓░░░░]▓▓▓▓▓▓▓▌                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                      ▓▓▓░░░▓▓▓░░▐@░▓▓░░░▐▓▓▓░░░░▐▓▓▓▓▓▓▓U                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                       "▀Ü░░▓▓▓▓░▓▓▐▓▓░░░▓▓▓▓░░░░▓▓▓▓▓▓▓▓⌐                        {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                           `▀▓▓▓▓▓▓▓▓▓▌░▐▓▓▓▓░░░░▓▓▓▓▓▓▀╙                         {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                                ███▓▓▓█▓█████▓▀                                   {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                                ████████▀▀▀╙.                                     {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                                ╙██████████▄                                      {Style.RESET_ALL}')
    print()
    print(f'{Fore.WHITE}       ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓     {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██▒     {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒██░     {Style.RESET_ALL}')
    print(f'{Fore.WHITE}       ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░     {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░██████▒ {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░ {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░ {Style.RESET_ALL}')
    print(f'{Fore.WHITE}     ░  ░  ░  ░░          ░   ░          ░        ░░   ░   ░   ▒     ░ ░    {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ░              ░  ░░ ░                  ░           ░  ░    ░  ░ {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                              ░                                             {Style.RESET_ALL}')
    print(f'{Fore.WHITE}             ██████▓██   ██▓ ██▓███   ██░ ██  ▒█████   ███▄    █            {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ▒██    ▒ ▒██  ██▒▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █            {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ░ ▓██▄    ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒           {Style.RESET_ALL}')
    print(f'{Fore.WHITE}             ▒   ██▒ ░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒           {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ▒██████▒▒ ░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░           {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ▒ ▒▓▒ ▒ ░  ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒            {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ░ ░▒  ░ ░▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░           {Style.RESET_ALL}')
    print(f'{Fore.WHITE}           ░  ░  ░  ▒ ▒ ░░  ░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░            {Style.RESET_ALL}')
    print(f'{Fore.WHITE}                 ░  ░ ░               ░  ░  ░    ░ ░           ░            {Style.RESET_ALL}')
    print()
    print(f'{Fore.LIGHTRED_EX}GitHub Repository:{Style.RESET_ALL}{Fore.CYAN} https://github.com/AdrianMargarit/SpectralSyphon{Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}Author:{Style.RESET_ALL}{Fore.CYAN} Ion-Margarit Adrian-Florin{Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}Licensed at:{Style.RESET_ALL}{Fore.CYAN} University of Bucharest{Style.RESET_ALL}')


# This function is used to display the splash screen
def greetings():
    introList = [splash_screen]
    subprocess.call(['clear'])
    random.choice(introList)()
    time.sleep(2.5)
    subprocess.call(['clear'])
