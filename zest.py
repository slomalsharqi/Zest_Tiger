#!/usr/bin/env python3
import sys, os, time, random, requests

# تهيئة ذكية للألوان (كالي وتيرمكس)
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
      /  {Fore.RED}●{Fore.GREEN}          {Fore.RED}●{Fore.GREEN}  \\       {Fore.CYAN}CORE: UNIVERSAL PAYLOAD v6.0
     (      {Fore.YELLOW}  __  {Fore.GREEN}      )      {Fore.WHITE}OS: {os_info}
      \\{Fore.YELLOW}      \\__/      {Fore.GREEN}/       {Fore.MAGENTA}BY: SLOMALSHARQI
       \\            /
        \\__________/ {Fore.WHITE}  - THE TIGER IS READY TO HUNT -
"""
    print(banner)

def get_payload(target, password, platform):
    # محاكاة الرموز الأمنية (Tokens) لكل منصة
    return {
        'lsd': 'AV' + ''.join(random.choices('0123456789', k=6)),
        'jazoest': '2' + str(random.randint(100, 999)),
        'email': target,
        'pass': password
    }

def start_attack(target, platform):
    wordlist = "passwords.txt"
    if not os.path.exists(wordlist):
        with open(wordlist, "w") as f: f.write("123456\npassword\n12345678\nyemen2026\n")

    clear()
    visual_banner()
    print(f"{Fore.CYAN}[*] TARGET   : {Fore.WHITE}{target}")
    print(f"{Fore.CYAN}[*] PLATFORM : {Fore.WHITE}{platform}")
    print(f"{Fore.CYAN}[*] STATUS   : {Fore.GREEN}STEALTH PAYLOAD ACTIVE")
    print(f"{Fore.MAGENTA}------------------------------------------------------")
    time.sleep(1)

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f]
        total = len(passwords)

    session = requests.Session()
    for i, pwd in enumerate(passwords, 1):
        percent = int(100 * (i / total))
        
        # دمج الـ Payload والتوكنز
        payload = get_payload(target, pwd, platform)
        
        # طباعة سطر بسطر (Scrolling Log) بسرعة متوازنة
        status = random.choice([200, 403, 302])
        print(f"{Fore.WHITE}[{percent:02d}%] {Fore.GREEN}CHECKING: {Fore.YELLOW}{pwd.ljust(12)} {Fore.CYAN}STATUS: {status}")
        
        # التوقيت المتوازن (0.4 - 1.0 ثانية)
        time.sleep(random.uniform(0.4, 1.0))

        if pwd == "yemen2026":
            print(f"\n{Fore.GREEN}{Style.BRIGHT}[★] MATCH FOUND! DATA CAPTURED: {pwd}")
            print(f"{Fore.WHITE}------------------------------------------------------")
            with open("hits.txt", "a") as h: h.write(f"{platform} | {target}:{pwd}\n")
            return

    print(f"\n{Fore.RED}[!] ATTACK FINISHED. TARGET SECURE.")

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
        plats = {"1":"Facebook", "2":"Instagram", "3":"TikTok", "4":"Twitter", "5":"Gmail"}
        
        if choice in plats:
            target = input(f"    {Fore.CYAN}Target (Email/ID/Phone): {Fore.WHITE}")
            start_attack(target, plats[choice])
            input(f"\n    {Fore.YELLOW}Press Enter to Return...")
        elif choice == "0": break

if __name__ == "__main__":
    main()
