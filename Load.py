#tool created by Mantal Studio.  if you get the source code please write the source
#=====Mantal Studio=====#
__Author__ = "Mantal Studio"
__Version__ = "2.1"
__Github__ = "github.com/Mantalstudio"
#tool created by Mantal studio.  if you get the source code please write the source
#=====Error Module=====#
import os
try:
    import requests
except ImportError:
    print('\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m requests is not installed')
    print('\033[1;97m[\033[1;92m*\033[1;97m] Installing requests')
    os.system('pip install requests')
#tool created by Mantal studio.  if you get the source code please write the source
#=====Setting=====#
import os, sys, requests, time, json, datetime
def mkdir(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0001)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
#tool created by axeyed tran.  if you get the source code please write the source
#=====Logo & Support=====#

question = "\033[1;97m[\033[1;96m?\033[1;97m] "
eror = "\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m "
ok = "\033[1;97m[\033[1;92m✓\033[1;97m] "
wn = "\033[1;97m[\033[1;92m*\033[1;97m] "
logo = """\033[1;97m
===============================================================
        Tool to increase virtual shares for facebook v1.2
                Author: Mantal studio
                Version: 2.1
                Github: github.com/Mantalstudio
                License: Mantal studio
                Tool Coded By Mantal studio
===============================================================
"""
f= "\033[1;97m==============================================================="
#tool created by Mantal studio.  if you get the source code please write the source
#=====Main=====#
def main():
    clear()
    mkdir(logo)
    token = input(question+'Access_Token:')
    mkdir(wn+'Checking Token...')
    try:
        k = requests.get('https://graph.facebook.com/me?access_token='+token)
        kk = json.loads(k.text)
        name = kk['name']
        idfb = kk['id']
        mkdir(ok+'Login Sucessfully')
        time.sleep(3)
    except:
        mkdir(eror+'Invalid Token')
        os.sys.exit()
    clear()
    mkdir(logo)
    mkdir(ok+'Name: '+name)
    mkdir(ok+'ID: '+idfb)
    mkdir(f)
    idpost = input(question+'ID Post:')
    mkdir(f)
    time_delay = int(input(question+'Time Delay:'))
    clear()
    mkdir(logo)
    kha = 0
    kha = kha + 1
    #tool created by Mantal studio.  if you get the source code please write the source
    while True:
        requests.get('https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/'+str(idpost)+'&access_token='+str(token))
        print('\033[1;97m[\033[1;92m✓\033[1;97m]-----[\033[1;96mCongratulations\033[1;97m]-----[\033[1;93m'+str(idpost)+'\033[1;97m]')
        time.sleep(time_delay)
#tool created by Mantal studion.  if you get the source code please write the source
#=====RUN=====#
main()
#=====tool created by Mantal studio.  if you get the source code please write the source=====#
#tool created by Mantal studio.  if you get the source code please write the source
