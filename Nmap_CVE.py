
#===========================================================================
#!/usr/bin env python
import os
import sys
import time
import os.path
import requests
import subprocess
#============================SYSTEM_CHEK====================================
try:
    from termcolor import colored
except ModuleNotFoundError:
    print(colored('Error 01 - No library "termcolor" please run "pip install termcolor" ', 'red'))
    time.sleep(5)
    sys.exit(0)

if os.sys.platform == 'win32':
    print(colored(' Error 02 - This script only works on Linux!!!', 'red'))
    time.sleep(5)
    sys.exit(0)
else:
    os.system('clear')
    
try:
    from Modules.banner import banner
except ModuleNotFoundError:
    print(colored('Error 03 - No File "Modules/banner.py" ', 'red'))
    time.sleep(5)
    sys.exit(0) 
#================================CONFIG=====================================
file_path = "usr/share/nmap/scripts/vulners.nse"
#================================START======================================
if os.path.exists:
    banner()
    while True:
        print('[1] - run Nmap_CVE\n[2] - run Nmap\n[3] - info\n[4] - update')
        numb = input('#: ')

        if numb == '1':
            os.system('clear')
            banner()
            host_cve = input('Enter host: ')
            print()
            conf_cve = ['nmap','-Pn','-sV','--script','vulners.nse',host_cve]
            subprocess.call(conf_cve)
            print()

        elif numb == '2':
            os.system('clear')
            banner()
            host = input('Enter host: ')
            print()
            conf = ['nmap',host]   
            subprocess.call(conf)
        
        elif numb == '3':
            os.system('clear')
            banner()
            print('Wrote the code Extremmer781\nVK - vk.com/extremmer781\nTelegram - t.me/extremmer781')
        elif numb == '4':
            update = input('Update Nmap_CVE? (Yes/No): ')
            if update == 'Yes':
                os.system('clear')
                banner()
                print('The repository will download in ~/ or to your desktop\n(depending on your system)')
                print('The script will reload automatically...')
                print('Update will start in 10 seconds...')
                time.sleep(10)
                os.system('sh Nmap_update.sh')
                time.sleep(5)
                sys.exit(0)
            else:
                os.system('clear')
                banner()
                print('Update rejected')   
        else:
            os.system('clear')
            banner()
            print('Bad command')

else:
    print('Error 04 - No Nmap file "vulners.nse"')
    updateV = input('setup "vulners.nse"? (Yes/No): ')

    if updateV == 'Yes':
        os.system('sudo python3 Nmap_install.py')
    else:
        print('Exit...')
        sys.exit(0)
