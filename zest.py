#!/usr/bin/env python3
import requests, time, os, sys, shutil, random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('clear')

def get_w():
    return shutil.get_terminal_size().columns

def visual_banner():
    clear()
    w = get_w()
    line = f"{Fore.CYAN}━" * w
    header = f"{Fore.WHITE}[ {Fore.RED}ZEST-TIGER V3.0 {Fore.WHITE} ] {Fore.MAGENTA}● {Fore.WHITE}FILE: {Fore.GREEN}AUTO-SAVE {Fore.MAGENTA}● {Fore.WHITE}GMAIL: {Fore.GREEN}READY"
    print(line)
    print(header.center(w + 35))
    print(line)
    
    menu = [
        (f"{Fore.YELLOW}  01  {Fore.CYAN}│ {Fore.WHITE}FACEBOOK"),
        (f"{Fore.YELLOW}  02  {Fore.CYAN}│ {Fore.WHITE}INSTAGRAM"),
        (f"{Fore.YELLOW}  03  {Fore.CYAN}│ {Fore.WHITE}SNAPCHAT"),
        (f"{Fore.YELLOW}  04  {Fore.CYAN}│ {Fore.WHITE}GMAIL/GOOGLE"),
        (f"{Fore.RED}  00  {Fore.CYAN}│ {Fore.WHITE}EXIT SYSTEM")
    ]
    for item in menu: print(item)
    print(f"\n{Fore.CYAN}" + "━" * w)

def save_result(platform, target, password):
    # دالة حفظ النتائج الناجحة
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("cracked.txt", "a") as f:
        f.write(f"[{now}] PLATFORM: {platform} | TARGET: {target} | PASSWORD: {password}\n")

def fast_engine(target, platform, f_type):
    if not os.path.exists("passwords.txt"):
        print(f"{Fore.RED}[!] Database Missing."); return

    with open("passwords.txt", "r", encoding='latin-1') as f:
        passwords = [p.strip() for p in f.readlines() if len(p.strip()) >= 6]

    total = len(passwords)
    print(f"\n{Fore.RED}⚡ {Fore.WHITE}TARGET: {Fore.YELLOW}{target} {Fore.WHITE}| {Fore.CYAN}{total} KEYS LOADED")

    for i, pwd in enumerate(passwords, 1):
        percent = (i / total) * 100
        bar = f"{Fore.RED}━" * int(25 * i // total) + f"{Fore.WHITE}─" * (25 - int(25 * i // total))
        sys.stdout.write(f"\r {Fore.WHITE}[{bar}{Fore.WHITE}] {percent:.1f}% {Fore.CYAN}KEY: {Fore.YELLOW}{pwd[:10]:<10}")
        sys.stdout.flush()
        
        # محاكاة النجاح (للتجربة) - هنا تضع محرك الـ API الحقيقي
        if pwd == "SUCCESS_CODE_99": 
            print(f"\n\n{Fore.GREEN}[!!!] CRACKED! PASSWORD FOUND: {pwd}")
            save_result(platform, target, pwd)
            return

        if platform == "GMAIL/GOOGLE": time.sleep(random.uniform(1.0, 2.0))
        else:
            if i % 100 == 0: time.sleep(0.01)

def main():
    while True:
        visual_banner()
        choice = input(f"{Fore.GREEN}zest{Fore.WHITE}@{Fore.RED}tiger{Fore.WHITE}:~# ").strip()
        if choice in ['0', '00']: break
        names = {"1":"FACEBOOK", "2":"INSTAGRAM", "3":"SNAPCHAT", "4":"GMAIL/GOOGLE"}
        if choice in names:
            platform = names[choice]
            target = input(f"{Fore.CYAN}  ENTER TARGET > {Fore.WHITE}")
            fast_engine(target, platform, "DATA")
            input(f"\n{Fore.WHITE}[ PRESS ENTER ]")

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print(f"\n{Fore.RED}[!] DISCONNECTED.")
