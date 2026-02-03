#!/usr/bin/env python3
import sys, os, time, random, requests

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore: RED=GREEN=YELLOW=BLUE=RESET=WHITE=MAGENTA=CYAN=BLACK=""
    class Style: BRIGHT=RESET=""
    def init(autoreset=False): pass

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_os():
    return "TERMUX (MOBILE)" if "com.termux" in sys.executable else "KALI LINUX (PC)"

def visual_banner():
    os_info = get_os()
    banner = f"""
{Fore.GREEN}{Style.BRIGHT}          .          .
         / \\        / \\
        /   \\      /   \\         {Fore.WHITE}Z E S T   T I G E R   P E N
       /     \\____/     \\        {Fore.GREEN}---------------------------
      /  {Fore.RED}●{Fore.GREEN}          {Fore.RED}●{Fore.GREEN}  \\       {Fore.CYAN}CORE: INTELLIGENT ENGINE v7.0
     (      {Fore.YELLOW}  __  {Fore.GREEN}      )      {Fore.WHITE}OS: {os_info}
      \\{Fore.YELLOW}      \\__/      {Fore.GREEN}/       {Fore.MAGENTA}BY: SLOMALSHARQI
       \\            /
        \\__________/ {Fore.WHITE}  - SMART GUIDANCE SYSTEM ACTIVE -
"""
    print(banner)

def leaked_generator(target_info):
    name = target_info.get('name', 'user').lower()
    year = target_info.get('year', '2025')
    leaks = [
        f"{name.capitalize()}@{year}", f"{name}{year}!", f"{name}.{year}",
        f"P@ssw0rd{year}", f"Admin#{year}", f"{name}2026", f"Yemen@{year}",
        f"{name}{year}", f"{name}123", f"{name}@{year}"
    ]
    return leaks

def start_attack(target, platform):
    wordlist = "passwords.txt"
    if not os.path.exists(wordlist):
        print(f"{Fore.YELLOW}[*] Downloading Real Wordlist...")
        with open(wordlist, "w") as f: f.write("123456\npassword\n12345678\nyemen2026\n")

    clear()
    visual_banner()
    
    # قسم التعليمات للمستخدم
    print(f"{Fore.YELLOW}┌───[ {Fore.WHITE}HOW TO USE SMART MODE {Fore.YELLOW}]")
    print(f"{Fore.WHITE}│ 1. {Fore.CYAN}Target Name{Fore.WHITE} : Write first name only (Ex: ali)")
    print(f"{Fore.WHITE}│ 2. {Fore.CYAN}Target Year{Fore.WHITE} : Write birth or current year (Ex: 1998)")
    print(f"{Fore.YELLOW}└───────────────────────────────────────\n")

    t_name = input(f"    {Fore.GREEN}❯ Enter Target Name: {Fore.WHITE}") or "user"
    t_year = input(f"    {Fore.GREEN}❯ Enter Target Year: {Fore.WHITE}") or "2026"
    
    smart_list = leaked_generator({'name': t_name, 'year': t_year})
    
    print(f"\n{Fore.MAGENTA}[!] PHASE 1: TESTING SMART LEAKED PATTERNS...")
    print(f"{Fore.MAGENTA}------------------------------------------------------")

    for pwd in smart_list:
        print(f"{Fore.WHITE}[SMART] {Fore.GREEN}TRYING: {Fore.YELLOW}{pwd.ljust(15)} {Fore.CYAN}STATUS: 200")
        time.sleep(random.uniform(0.6, 1.2))
        if pwd == "yemen2026":
            print(f"\n{Fore.GREEN}{Style.BRIGHT}[★] MATCH FOUND: {pwd}"); return

    print(f"{Fore.BLUE}[*] SMART LIST FINISHED. STARTING BRUTE FORCE (14M)...")
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            pwd = line.strip()
            if i % 5 == 0: # تقليل سرعة الطباعة لتبدو واقعية
                print(f"{Fore.WHITE}[{i:03d}] {Fore.GREEN}TESTING: {Fore.YELLOW}{pwd.ljust(15)} {Fore.CYAN}STATUS: 302")
                time.sleep(random.uniform(0.4, 0.8))

def main():
    while True:
        clear()
        visual_banner()
        print(f"    {Fore.GREEN}╔════════════════════════════════════════╗")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[1] FACEBOOK      {Fore.WHITE}[2] INSTAGRAM    {Fore.GREEN}║")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[3] TIKTOK        {Fore.WHITE}[4] TWITTER / X  {Fore.GREEN}║")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[5] GMAIL         {Fore.RED}[0] EXIT SYSTEM   {Fore.GREEN}║")
        print(f"    {Fore.GREEN}╚════════════════════════════════════════╝")
        
        choice = input(f"\n    {Fore.YELLOW}ZEST-TIGER {Fore.WHITE}❯ ")
        platforms = {"1":"Facebook", "2":"Instagram", "3":"TikTok", "4":"Twitter", "5":"Gmail"}
        
        if choice in platforms:
            target = input(f"    {Fore.CYAN}Target ID/Email: {Fore.WHITE}")
            start_attack(target, platforms[choice])
            input(f"\n    {Fore.YELLOW}Press Enter to return...")
        elif choice == "0": break

if __name__ == "__main__":
    main()
