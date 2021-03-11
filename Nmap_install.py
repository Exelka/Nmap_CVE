import requests
import os.path
import os

try:
    os.system('sudo apt install nmap -y')
    print('download nmap')
    os.system('clear')
    print('successfully donwload nmap')
    print('download lib')
except PermissionError:
    print('Error [1] - run the script in sudo')

try:
    os.system('pip install termcolor')
    os.system('clear')
    print('successfully donwload lib')
    print('download nmap files')
except PermissionError:
    print('Error [2] - run the script in sudo')

try: 
    url = 'https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse'
    r = requests.get(url, allow_redirects=True)

    open('/usr/share/nmap/scripts/vulners.nse', 'wb').write(r.content)
    file_path = "usr/share/nmap/scripts/vulners.nse"
    print('successfully donwload nmap files')

except PermissionError:
    print('Error [3] - run the script in sudo')


try:
    os.path.exists(file_path)

    if os.path.exists:
        os.system('clear')
        print("Completed!")

    else:
        print("Critical Error")

except NameError:
    print('exit...')
        
