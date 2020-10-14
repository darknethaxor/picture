import os
import sys
import random
import mechanize
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    lili = '\033[4m'
    wd = "\033[90;1m"  # dark
    GL = "\033[96;1m"  # Blue aqua
    BB = "\033[34;1m"  # Blue light
    YY = "\033[33;1m"  # Yellow light
    GG = "\033[32;1m"  # Green light
    WW = "\033[0;1m"  # White light
    Y = "\033[33;1m"  # Yellow
    G = "\033[32m"  # Green
    W = "\033[0;1m"  # White
    R = "\033[31;1m"  # Red
    C = "\033[36;1m"  # Cyan
    pur = "\033[35m"
    yel = "\033[93m"
    green = "\033[42m"
    orange = "\033[43m"
    orr = '\033[33m'
    OKCYAN = "\033[36m"
    lightblue = '\033[94m'
    CGREENBG2 = '\33[102m'
os.system('clear')
os.system('touch checkpoint.txt')
os.system('touch successfull.txt')
def digit():
    print(f"{bcolors.BOLD}{bcolors.OKGREEN}[1] 6 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.R}[2] 7 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.YY}[3] 8 digit{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.OKGREEN}[4] 11 digit{bcolors.ENDC}")
def logo():
    print(f"{bcolors.C}    _   ___       __    __        ____          {bcolors.ENDC}")
    print(f"{bcolors.C}   / | / (_)___ _/ /_  / /_      / __ \____ _____ ____   {bcolors.ENDC}")
    print(f"{bcolors.C}  /  |/ / / __ `/ __ \/ __/_____/ /_/ / __ `/ __ `/ _ \  {bcolors.ENDC}")
    print(f"{bcolors.C} / /|  / / /_/ / / / / /_/_____/ _, _/ /_/ / /_/ /  __/ {bcolors.ENDC}")
    print(f"{bcolors.C}/_/ |_/_/\__, /_/ /_/\__/     /_/ |_|\__,_/\__, /\___/  {bcolors.ENDC}")
    print(f"{bcolors.C}        /____/                            /____/        {bcolors.ENDC}")
    print(f"{bcolors.lightblue}{bcolors.lili}{bcolors.BOLD}--------------------------------------------------------------------------------------------------------------------------------------------------------------{bcolors.ENDC}\n")
    print(f"{bcolors.C}Authour        : DARKNETHAXOR{bcolors.ENDC}\n")
    print(f"{bcolors.C}Group Name     : Facebook.com/group/darknethaxor{bcolors.ENDC}\n")
    print(f"{bcolors.C}Facebook page  : Facebook.com/page/darknethaxor{bcolors.ENDC}\n")
    print(f"{bcolors.C}Youtube        : youtube.com/Darknethaxor {bcolors.ENDC}\n")
    print(f"{bcolors.C}Github         : github.com/darknethaxor {bcolors.ENDC}")
    print(f"{bcolors.lightblue}{bcolors.lili}{bcolors.BOLD}--------------------------------------------------------------------------------------------------------------------------------------------------------------{bcolors.ENDC}\n")
def select():
    print(f"{bcolors.BOLD}{bcolors.OKGREEN}Chose Digit: {bcolors.ENDC}",end="")
    digiin = input("")
logo()
digit()
print(f"{bcolors.BOLD}{bcolors.OKGREEN}Chose Digit: {bcolors.ENDC}",end="")
digiin = str(input(""))
if digiin== "1":
    os.system('clear')
    os.system('python rage6.py')
elif digiin== "2":
    os.system('clear')
    os.system('rage7.py')
elif digiin== "3":
    os.system('clear')
    os.system('rage8.py')
elif digiin== "4":
    os.system('clear')
    os.system('rage11.py')
else:
    print("wrong input")