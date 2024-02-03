#!/bin/bash

if [[ `id -u` -eq 0 ]]
then
	printf "\n[-] FATAL: This script MUST NOT be run as root\n[!] You will be prompted for the sudo password when required\n\n"
	exit 1
fi

printf "\n[!] Updating package index\n"
sudo apt update

printf "\n[!] Downloading required dependencies\n"
wget http://ftp.us.debian.org/debian/pool/main/i/icu/libicu63_63.1-6+deb10u3_amd64.deb
wget http://deb.debian.org/debian/pool/main/o/openssl/openssl_1.1.1w.orig.tar.gz

printf "\n[!] Building libssl1.1\n"
printf "\n[!] This might take some time...\n"
tar xf openssl_1.1.1w.orig.tar.gz -C include/
cd include/openssl-1.1.1w
./config
make -j$(nproc)
cd ../..

printf "\n[!] Installing required dependencies\n"
sudo apt install -y ./libicu63_63.1-6+deb10u3_amd64.deb libgdiplus

printf "\n[!] Installing required Python packages\n"
python3 -m pip install -t packages/ -r requirements.txt

printf "\n[!] Cleaning up\n"
rm libicu63_63.1-6+deb10u3_amd64.deb openssl_1.1.1w.orig.tar.gz

printf "\n[+] Requirements satisfied. You can now execute ./minitrue\n\n"
exit 0
