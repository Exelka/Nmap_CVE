import os.path
import os

if os.sys.platform == 'win32':
    print(' Error [1] - This script only works on Linux!!!')
    time.sleep(5)
    sys.exit(0)

else:
    os.system('clear')

system = input('''
--------------------
|   Who are you ?  |
|------------------|
| [1] Linux OS     |
| [2] Termux       |
|                  |
| Enter the 1/2:   |
-------------------- Answer: ''')

if system == '1':

    try:
        os.system('sudo apt install nmap -y')
        print('download nmap')
        os.system('clear')
        print('successfully donwload nmap')
        print('download lib')

    except PermissionError:
        print('Error [2] - run the script in sudo')


    try:
        os.system('pip install colored')
        os.system('pip install termcolor')
        os.system('pip install requests')
        os.system('clear')
        print('successfully donwload lib')
        print('download nmap files')

    except PermissionError:
        print('Error [3] - run the script in sudo')


    try:
        try:
            import requests 
            url = 'https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse'
            r = requests.get(url, allow_redirects=True)

            open('/usr/share/nmap/scripts/vulners.nse', 'wb').write(r.content)
            file_path = "usr/share/nmap/scripts/vulners.nse"
            print('successfully donwload nmap files')

        except PermissionError:
            print('Error [4] - run the script in sudo')

    except FileNotFoundError:
        print('Critical Error [1]')


    try:
        os.path.exists(file_path)

        if os.path.exists:
            os.system('clear')
            print("Completed!")

        else:
            print("Critical Error [2]")

    except NameError:
        print('exit...')


elif system == '2':
    try:
        os.system('apt install nmap -y')
        print('download nmap')
        os.system('clear')
        print('successfully donwload nmap')
        print('download lib')

    except PermissionError:
        print('Error [2]')


    try:
        os.system('pip install colored')
        os.system('pip install termcolor')
        os.system('pip install requests')
        os.system('clear')
        print('successfully donwload lib')
        print('download nmap files')

    except PermissionError:
        print('Error [3]')


    try:
        try:
            import requests 
            url = 'https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse'
            r = requests.get(url, allow_redirects=True)

            open('/data/data/com.termux/files/usr/share/nmap/scripts/vulners.nse', 'wb').write(r.content)
            file_path = "/data/data/com.termux/files/usr/share/nmap/scripts/vulners.nse"
            print('successfully donwload nmap files')

        except PermissionError:
            print('Error [4]')

    except FileNotFoundError:
        print('Critical Error [1]')


    try:
        os.path.exists(file_path)

        if os.path.exists:
            os.system('clear')
            print("Completed!")

        else:
            print("Critical Error [2]")

    except NameError:
        print('exit...')
else:
    print('exit...')
