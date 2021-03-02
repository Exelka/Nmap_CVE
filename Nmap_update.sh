#!/bin/bash
rm -rf Modules/
rm -rf Nmap_install.sh
rm -rf Nmap_update.sh
rm -rf Nmap_CVE.py
cd ..
rm -rf Nmap_CVE/
git clone https://github.com/Extremmer/Nmap_CVE
ls
cd Nmap_CVE/
python3 nmap_cve.py
