# Spectral Syphon - Penetration Testing Tool

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![Screenshot 2023-09-22 163440](https://github.com/AdrianMargarit/Spectral-Syphon-Penetration-Testing-Tool/assets/96662075/ae84ddf3-fded-411f-84f2-16cef1d7c5b1)

Spectral Syphon is a network and Penetration Testing Tool that I created as a cybersecurity research project for my university. It is solely made for educational purposes and to raise awareness. I am not responsible for the actions of other people.

The utility was made with the idea in mind that the users should only use a single application with the necessary features instead of multiple other applications. Through Spectral Syphon I encourage users to discover the numerous benefits of using an application that can respond to their needs.

In present, Spectral Syphon is capable of running a variety of complex tasks, like:

	- **ifconfig**;
	- **ping**;
	- **traceroute**;
	- **port scan** -> including SYN, TCP, UDP, ACK;
	- **comprehensive scan**;
	- **host discovery** -> scanning for multiple devices on a local network;
	- **MAC address detection**;
	- **banner grabbing**;
	- **DNS checks** -> with location information;
	- **whois**;
	- **subdomain enumeration**;
	- **vulnerability reconnaissance**;
	- **packet sniffing**;
	- **MAC spoofing**;
	- **IP spoofing**;
	- **SYN flooding**;
	- **deauthentication attack**;
	- **brute-force attack**;


## Table of contents

+ [How to install](#how-to-install)
  - [Linux](#linux)
+ [How to configure](#how-to-configure)
+ [How to use](#how-to-use)
  + Networking utilities
    - [ifconfig](#ifconfig)
    - [ping](#ping)
    - [traceroute](#traceroute)
  + Footprinting utilities
    - [Scanning Ports](#scanning-ports)
    - [Host discovery - scanning for multiple devices on a local network](#host-discovery)
    - [MAC address retrieval - fetching the MAC address of a host IP on a local network](#mac-address-retrieval)
    - [Banner grabbing - application version detection)](#banner-grabbing)
    - [DNS Queries - with location information)](#dns-queries)
    - [WHOIS Lookup](#whois-lookup)
    - [Subdomain enumeration](#subdomain-enumeration)
    - [Directory busting](#directory-busting)
    - [Probing for vulnerabilities](#probing-for-vulnerabilities)
  + Offensive utilities
    - [Sniffing packets](#sniffing-packets)
    - [MAC spoofing](#mac-spoofing)
    - [IP spoofing](#ip-spoofing)
    - [SYN flooding](#syn-flooding)
    - [Deauthentication attack](#deauth-attack)
    - [Brute-force attack](#brute-force-attack)
  + Other utilities
    - [Interface mode switch](#interface-mode-switch)
    - [Automated scans](#automated-scans)
+ [License](#license)

## Installation

#**Note**
**Spectral Syphon will run without any problems on Linux, but If you try to run it on Windows or macOS, it will run, but with errors.** 

Spectral Syphon has been tested on Kali Linux.

### Linux

For you to use Spectral Syphon without running into problems, you will have to install the necessary packages by running the `setup.sh` script using root privileges. 

The setup is compatible solely with distributions based on Debian, Red Hat, and Arch, which utilize the apt, DNF, and PacMan package systems respectively. This includes systems like ***Ubuntu***, ***Kali Linux***, ***Parrot OS***, ***Debian***, ***Pop!_OS***, ***Linux Mint***, ***Deepin***, ***Zorin OS***, ***MX Linux***, ***Elementary OS***, ***Fedora***, ***CentOS***, ***Red Hat Enterprise Linux***, ***Rocky Linux***, ***AlmaLinux***, ***Oracle Linux***, ***ClearOS***, ***Arch***, ***Black Arch***, ***Manjaro***, and similar ones.

To install Spectral Syphon, on most systems, simply run the following commands:
```
git clone https://github.com/AdrianMargarit/Spectral-Syphon-Penetration-Testing-Tool.git
cd SpectralSyphon
sudo sh setup.sh
```
After this, just simply follow the instructions provided.

**Note** Ignore any error messages that may appear during the installation process.

For any other distributions, other than Linux, you may need to install the packages manually using your distribution's package manager. 

After installing, in order to run the program, go to the project's root folder and run the `SpectralSyphon.py` file using Python as root user.
```
sudo python3 SpectralSyphon.py
```

## How to configure
If you want to configure Spectral Syphon differently than it is, navigate to `cfg/config.py` and edit it.


## How to use


### ifconfig
To show your system's current TCP/IP network configuration, use the following command:
`-ifconfig`


### ping
To check connectivity by sending ICMP packets to the desired host, use:
`-ping <HOST(s) IP/domain name>`


### traceroute
Measure transit delays and diagnose route paths by using:
`-traceroute <HOST IP/domain name>`


### Scanning Ports
By examining ports, we can spot possible security risks by pinpointing active hosts on the network and their running services.

There are various scanning methods available, such as TCP SYN (`-scansyn`) commonly termed as stealth scan, TCP Connect (`-scantcp`), UDP (`-scanudp`), TCP ACK (`-scanack`), and the all-inclusive scan (`-scan`).

`-scan -host <HOST(s) IP/domain name>`
`-scan -host <HOST(s) IP/domain name> -p <PORT(s)>`

For scanning a range of IPs and/or ports, consider the following commands:

`-scan -host <HOST(s) IP/domain name> -prange <START PORT> <END PORT>`
`-scan -iprange <START IP> <END IP> -p <PORT(s)>`
`-scan -iprange <START IP> <END IP> -prange <START PORT> <END PORT>`

Post-scan, it becomes evident that ports 22 (SSH) and 80 (HTTP) are active.

### Host discovery
To locate active devices within a specified network, input:
`-scanlan`

Next, specify the desired network for scanning.


### MAC Address Retrieval
To fetch the MAC address of one or several online hosts within the LAN, command:
`-getmac -host <HOST(s) IP>`


### Banner grabbing
Banner grabbing or version detection is an intelligence-gathering method that extracts software banner details. These banners often unveil crucial details about a network service, potentially revealing the software's name and version. Services like FTP, Web, SSH, and SMTP might disclose key details about their software in these banners.

Start with an enumeration scan to uncover open ports. Once a service is pinpointed, dispatch specific packets and analyze the returned data for desired details.

For banner grabbing, depending on the requirement, use:

`-grab -host <HOST(s) IP/domain name> -p <PORT(s)>`
`-grab -iprange <START IP> <END IP> -prange <START PORT> <END PORT>`
`-grab -host <HOST(s) IP/domain name> -prange <START PORT> <END PORT>`
`-grab -iprange <START IP> <END IP> -p <PORT(s)>`


### DNS Queries
This tool mirrors the functionality of the renowned `nslookup` command in UNIX systems. To execute a DNS check, enter:
`-ns <HOST(s) IP/domain name>`


**Note**: This feature leverages the IPinfo API. It's advised to replace the API key with your own IPinfo API key. For key replacement, navigate to `cfg/config.py`.

### WHOIS Lookup
WHOIS is a TCP-based protocol designed for querying contact and DNS details. To get the WHOIS data for one or multiple pages, input:
`-whois <HOST(s) IP/domain name>`


### Subdomain enumeration
Uncovering valid sub-domains for a domain or multiple domains is termed subdomain enumeration. This can bring to light many domains/sub-domains that could be within the scope of a security analysis, thereby amplifying the odds of spotting vulnerabilities.

To search for prevalent subdomains of a domain, just command:
`-sdenum <domain name>`

This command defaults to a standard wordlist for subdomain search. However, for a custom wordlist, input:
`-sdenum <domain name> -wordlist <WORDLIST PATH>`


### Directory busting
The aim of directory busting is to identify directories within a web server.

To execute this, enter:
`-dirbust <HOST IP/domain name>`

This command defaults to a typical wordlist for directory search. For a custom wordlist, use:
`-dirbust <HOST IP/domain name> -wordlist <WORDLIST PATH>`


### Probing for Vulnerabilities
To inspect one or multiple hosts for vulnerabilities, use:
`-vulnscan -host <HOST(s) IP/domain name>`


**Note**: This feature taps into the Shodan API. As above with the IPinfo API key, it's advised to replace the API key with your own Shodan API key. For key updates, head to `cfg/config.py`.


### Sniffing packets
To undertake packet sniffing, input:
`-sniff`


**Note**: To capture all data traversing a network, first set your wireless card or adapter to **monitor mode**.


### MAC spoofing
MAC spoofing entails generating frames with a MAC address differing from the transmitting NIC's address. To alter the MAC address of a given interface, command:
`-macspoof -source <SOURCE MAC> -iface <INTERFACE>`


### IP spoofing
The goal of IP spoofing is altering the authentic source IP address, ensuring the receiving system cannot accurately pinpoint the sender.

Remember, this command is effective only on machines with unpatched vulnerabilities. To execute IP spoofing targeting a specific port on a host, utilize:
`-ipspoof -source <SOURCE IP> <SOURCE PORT> -target <TARGET IP/domain name> <TARGET PORT>`

For random source IP, input:
`-ipspoof -source r <SOURCE PORT> -target <TARGET IP/domain name> <TARGET PORT>`

Random source port option is also available:
`-ipspoof -source <SOURCE IP> r -target <TARGET IP/domain name> <TARGET PORT>`


**Note**: Engage in these activities responsibly and solely on your devices.


### SYN flooding
SYN Flood is a DDoS type attack targeting the transport layer (layer 4) and indirectly impacting the application layer (layer 7).

To start SYN flooding, command:
`-synflood -source <SOURCE PORT> -target <TARGET IP/domain name> <TARGET PORT>`

For a random source port, use:
`-synflood -source r -target <TARGET IP/domain name> <TARGET PORT>`


**Note**: Ensure responsible usage, targeting only personal devices.


### Deauthentication attack
A deauthentication attack disrupts communication between a router and devices connected to it, effectively severing the target device's connection.

To execute, input:
`-deauth -target <TARGET MAC> -gateway <GATEWAY MAC> -iface <INTERFACE>`

For targeting all clients on a gateway:
`-deauth -target a -gateway <GATEWAY MAC> -iface <INTERFACE>`

For using the default wireless interface (set in `cfg/config.py`):
`-deauth -target <TARGET MAC> -gateway <GATEWAY MAC> -iface d`


**Note**: Ensure your wireless card or adapter supports **monitor mode** and is active prior to a deauthentication attack. Engage responsibly, targeting only personal devices.


### Brute-force attack
Brute-forcing is a strategy to decode a password or username. 

For launching brute-force to detect weak/common credentials:
`-bruteforce <SERVICE> -target <TARGET IP/domain name> -user <USERNAME>`

For custom wordlists:
`-bruteforce <SERVICE> -target <TARGET IP/domain name> -user <USERNAME> -wordlist <WORDLIST PATH>`

Currently, only the SSH service is compatible.

**Note**: Target servers might have defense mechanisms against such attacks. Ensure responsible usage.


### Automated scans
To automate several scan methods, type:
`-autoscan <HOST(s) IP/domain name>`


### Interface mode switch
Most wireless users interface their wireless cards as a station to an AP. In managed mode, the wireless card and driver rely on a local AP. Some cards also support monitor mode, where the card ceases data transmission and sniffs the currently configured channel, reporting packet contents to the host OS.

For monitor mode:
`-mode monitor -iface <INTERFACE>`

For default wireless interface (set in `cfg/config.py`):
`-mode monitor -iface d`

For managed mode:
`-mode managed -iface <INTERFACE>`

For default wireless interface:
`-mode managed -iface d`


## License

This repository is under the license of University of Bucharest, Romania.
