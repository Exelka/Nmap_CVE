import requests
import os.path

try:
    url = 'https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse'
    r = requests.get(url, allow_redirects=True)

    open('/usr/share/nmap/scripts/vulners.nse', 'wb').write(r.content)

    file_path = "usr/share/nmap/scripts/vulners.nse"
except PermissionError:
    print('run the script in sudo')

try:
    os.path.exists(file_path)
    if os.path.exists:
        print("Completed!")
    else:
        print("Critical Error")
except NameError:
    print('exit...')
        
