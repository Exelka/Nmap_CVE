#!/bin/bash
rm -rf Modules/
rm -rf Nmap_install.py
rm -rf Nmap_update.sh
rm -rf Nmap_CVE.py
rm -rf README.MD
cd ..
rm -rf Nmap_CVE/
git clone https://github.com/Exelka/Nmap_CVE
ls
cd Nmap_CVE/
python3 Nmap_CVE.py
