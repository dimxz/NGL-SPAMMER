import requests
import os
import time
import sys
from pystyle import Colors, Colorate
from datetime import datetime

def delay(amount):
   time.sleep(amount)
def ngl():
    
    R = '\033[31m'
    G = '\033[1;32m'
    W = '\033[0m'

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Vertical(Colors.red_to_green,"""


███╗░░██╗░██████╗░██╗░░░░░██████╗░██╗██████╗
████╗░██║██╔════╝░██║░░░░░██╔══██╗██║██╔══██╗
██╔██╗██║██║░░██╗░██║░░░░░██████╔╝██║██████╔╝
██║╚████║██║░░╚██╗██║░░░░░██╔══██╗██║██╔═══╝
██║░╚███║╚██████╔╝███████╗██║░░██║██║██║  By 
╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝  Dimxz
 
  Ngl - Rip is a tool that can be used to send lots of messages quickly to your friends' ngl.link ;) For educational purposes only.
    """))

    cosuser = input(Colorate.Color(Colors.orange,"[+] Custom UserAgent ? (y/n) : "))
    if cosuser == "y": 
      useragent = input(Colorate.Color(Colors.orange,"[+] Enter custom UserAgent : "))
    else: 
      useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
    nglusername = input(Colorate.Color(Colors.orange,"[+] Username : "))
    message = input(Colorate.Color(Colors.orange,"[+] Message : "))
    try:
        Count = int(input(Colorate.Color(Colors.orange, "[+] Count: ")))
    except ValueError:
        print(Colorate.Color(Colors.red, "[-] Error : Count must be a number"))
        delay(5)
        sys.exit(0)
    print(Colorate.Color(Colors.green,"\n[!] Spam on progress (Press Ctrl + C to stop)\n"))

    value = 0
    success = 0
    error = 0
    error404 = 0
    error429 = 0
    headers = {
              'Host': 'ngl.link',
              'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
              'accept': '*/*',
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'x-requested-with': 'XMLHttpRequest',
              'sec-ch-ua-mobile': '?0',
              'user-agent': useragent,
              'sec-ch-ua-platform': '"Windows"',
              'origin': 'https://ngl.link',
              'sec-fetch-site': 'same-origin',
              'sec-fetch-mode': 'cors',
              'sec-fetch-dest': 'empty',
              'referer': f'https://ngl.link/{nglusername}',
              'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
              }

    data = {
              'username': f'{nglusername}',
              'question': f'{message}',
              'deviceId': 'ea326443-ab1368-4a49-c590-bd8f96c294ee',
              'gameSlug': '',
              'referrer': '',
            }


    try:
      while value < Count:
        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)

        if response.status_code == 200:
            value += 1
            success += 1
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            print(Colorate.Color(Colors.green,"[{}]".format(time) + " [+] Success => {}".format(value)))
        elif response.status_code == 404:
            value += 1
            error += 1
            error404 += 1
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            print(Colorate.Color(Colors.red,"[{}]".format(time) + " [-] Error, Code => {}".format(response.status_code)))
        elif response.status_code == 429:
            value += 1
            error += 1
            error429 += 1
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            print(Colorate.Color(Colors.red,"[{}]".format(time) + " [-] Error, Code => {}".format(response.status_code)))
        else: 
            error += 1
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            print(Colorate.Color(Colors.red,"[{}]".format(time) + " [-] Error, Code => {}".format(response.status_code)))
            
    except KeyboardInterrupt:
        print(Colorate.Color(Colors.red,"[!] Ctrl + C pressed, script stopped."))
    except requests.exceptions.ConnectionError:
        print(Colorate.Color(Colors.red,"[!] You're offline / Unable to connect to NGL server."))
    except requests.exceptions.ReadTimeout:
        print(Colorate.Color(Colors.red,"[!] Unable to connect to NGL server."))
    finally:
        print(Colorate.Color(Colors.orange,"\n<========== DONE ==========>"))
        print(Colorate.Color(Colors.green,"Success => {}".format(success)))
        print(Colorate.Color(Colors.red,"Error => {}".format(error)))
        print(Colorate.Color(Colors.orange,"<==========================>"))
        if error > 0:
          print(Colorate.Color(Colors.red,"Error 404 (Not Found) => ") , Colorate.Color(Colors.white,str(error404)))
          print(Colorate.Color(Colors.red,"Error 429 (Too Many Request) => ") , Colorate.Color(Colors.white,str(error429)) , "\n\n")
ngl()