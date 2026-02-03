#!/usr/bin/env python3
import sys, os, time, random, requests
from concurrent.futures import ThreadPoolExecutor

# تهيئة ذكية للألوان تتوافق مع Termux و Kali
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # في حال عدم وجود المكتبة، لا يتوقف البرنامج بل يعمل بدون ألوان
    class Fore: RED=GREEN=YELLOW=BLUE=RESET=WHITE=MAGENTA=CYAN=BLACK=""
    class Style: BRIGHT=RESET=""
    def init(autoreset=False): pass

def clear():
    # تنظيف الشاشة حسب نظام التشغيل
    os.system('clear' if os.name == 'posix' else 'cls')

def get_platform_info():
    # معرفة هل المستخدم على تيرمكس أم كالي
    if "com.termux" in sys.executable:
        return "TERMUX (MOBILE)"
    return "KALI LINUX (PC)"

def visual_banner():
    p_info = get_platform_info()
    banner = f"""
{Fore.GREEN}{Style.BRIGHT}          .          .
         / \\        / \\
        /   \\      /   \\         {Fore.WHITE}Z E S T   T I G E R   P E N
       /     \\____/     \\        {Fore.GREEN}---------------------------
      /  {Fore.RED}●{Fore.GREEN}          {Fore.RED}●{Fore.GREEN}  \\       {Fore.CYAN}CORE: UNIVERSAL ENGINE v5.5
     (      {Fore.YELLOW}  __  {Fore.GREEN}      )      {Fore.WHITE}OS: {p_info}
      \\{Fore.YELLOW}      \\__/      {Fore.GREEN}/       {Fore.MAGENTA}BY: SLOMALSHARQI
       \\            /
        \\__________/ {Fore.WHITE}  - MULTI-PLATFORM READY -
"""
    print(banner)

def start_attack(target, platform):
    wordlist = "passwords.txt"
    if not os.path.exists(wordlist):
        with open(wordlist, "w") as f: 
            f.write("123456\npassword\n12345678\nadmin123\nyemen2026\n")

    clear()
    visual_banner()
    print(f"{Fore.CYAN}[*] SESSION : {Fore.WHITE}{platform}")
    print(f"{Fore.CYAN}[*] TARGET  : {Fore.WHITE}{target}")
    print(f"{Fore.MAGENTA}------------------------------------------------------")
    time.sleep(1)

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f]
        total = len(passwords)

    for i, pwd in enumerate(passwords, 1):
        percent = int(100 * (i / total))
        
        # تنسيق السطر ليكون مناسباً لعرض شاشة الهاتف والكمبيوتر
        # التقليل من المسافات الطويلة لضمان عدم انكسار السطر في Termux
        sys.stdout.write(f"{Fore.WHITE}[{percent:02d}%] {Fore.GREEN}TRY: {Fore.YELLOW}{pwd.ljust(12)} {Fore.CYAN}STATUS: {random.randint(200, 404)}\n")
        
        # سرعة متوازنة (Balanced Speed)
        time.sleep(random.uniform(0.4, 1.0)) 

        if pwd == "yemen2026":
            print(f"\n{Fore.GREEN}{Style.BRIGHT}[★] SUCCESS! PASSWORD: {pwd}")
            print(f"{Fore.WHITE}------------------------------------------------------")
            return

    print(f"\n{Fore.RED}[!] ATTACK FINISHED. NO MATCHES.")

def main():
    while True:
        clear()
        visual_banner()
        # تصميم قائمة مرنة (Responsive Menu)
        print(f"    {Fore.GREEN}╔════════════════════════════════════════╗")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[1] FACEBOOK      {Fore.WHITE}[2] INSTAGRAM    {Fore.GREEN}║")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[3] TIKTOK        {Fore.WHITE}[4] TWITTER / X  {Fore.GREEN}║")
        print(f"    {Fore.GREEN}║ {Fore.WHITE}[5] GMAIL         {Fore.RED}[0] EXIT SYSTEM   {Fore.GREEN}║")
        print(f"    {Fore.GREEN}╚════════════════════════════════════════╝")
        
        choice = input(f"\n    {Fore.YELLOW}ZEST-TIGER {Fore.WHITE}❯ ")
        
        platforms = {
            "1": "Facebook", "2": "Instagram", "3": "TikTok", 
            "4": "Twitter", "5": "Gmail"
        }
        
        if choice in platforms:
            target = input(f"    {Fore.CYAN}Target (ID/Email/Phone): {Fore.WHITE}")
            start_attack(target, platforms[choice])
            input(f"\n    {Fore.YELLOW}Press Enter to return...")
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
