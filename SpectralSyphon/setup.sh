# Display available options

echo "1. Debian-based systems => Debian, Ubuntu, Kali, ParrotOS, Linux Mint, MX Linux, etc."
echo "2. Red Hat Enterprise Linux-based systems => Red Hat Enterprise Linux, Fedora, CentOS, Oracle Linux, ClearOS, etc."
echo "3. Arch-based systems => Arch, Black Arch, etc."

read -p "Enter your choice => [1/2/3]: " choice

if test "$choice" = "1"
then
    # Debian-based systems
    sudo apt-get install nmap
    sudo apt-get install python3-pip

elif test "$choice" = "2"
then
    # Red Hat Enterprise Linux-based systems
    sudo yum install nmap
    sudo yum install python3-pip

elif test "$choice" = "3"
then
    # Arch-based systems
    sudo pacman -S nmap
    sudo pacman -S python3-pip

else
    echo "Invalid choice!"
    exit
fi

# Install pip packages
sudo pip3 install readline
sudo pip3 install binascii
sudo pip3 install struct
sudo pip3 install textwrap
sudo pip3 install multiprocessing
sudo pip3 install subprocess
sudo pip3 install time
sudo pip3 install threading
sudo pip3 install queue
sudo pip3 install colorama
sudo pip3 install ipaddress
sudo pip3 install python-nmap
sudo pip3 install ipinfo
sudo pip3 install scapy
sudo pip3 install shodan
sudo pip3 install python-whois
sudo pip3 install paramiko
sudo pip3 install netfilterqueue

# Add main .py to the system path
# cp *.py /usr/bin
# cp methods/*.py /usr/bin
# cp usr/bin/spectralsyphon.py /usr/bin/spectralsyphon
# chmod 755 /usr/bin/spectralsyphon