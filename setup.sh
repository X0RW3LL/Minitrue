#!/bin/bash

echo ""
echo "[!] Updating package index"
sudo apt update

echo ""
echo "[!] Downloading required dependencies"
echo ""
wget http://ftp.us.debian.org/debian/pool/main/i/icu/libicu63_63.1-6+deb10u3_amd64.deb
wget http://deb.debian.org/debian/pool/main/o/openssl/openssl_1.1.1w.orig.tar.gz

echo "[!] Building libssl1.1"
echo "[!] This might take some time..."
echo ""
tar xf openssl_1.1.1w.orig.tar.gz -C include/
cd include/openssl-1.1.1w
./config
make -j$(nproc)
cd ../..

echo ""
echo "[!] Installing required dependencies"
echo ""
sudo apt install -y ./libicu63_63.1-6+deb10u3_amd64.deb libgdiplus

echo ""
echo "[!] Installing required Python packages"
echo ""
python3 -m pip install -t packages/ -r requirements.txt

echo ""
echo "[!] Cleaning up"
rm libicu63_63.1-6+deb10u3_amd64.deb openssl_1.1.1w.orig.tar.gz

echo ""
echo "[+] Requirements satisfied. You can now execute ./minitrue"
echo ""
exit 0
