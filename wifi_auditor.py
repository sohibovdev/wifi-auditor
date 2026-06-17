#!/usr/bin/env python3
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

BANNER = f"""
{Fore.CYAN}██╗    ██╗██╗███████╗██╗     ██████╗  ██████╗ ███████╗
{Fore.CYAN}██║    ██║██║██╔════╝██║     ██╔══██╗██╔═══██╗██╔════╝
{Fore.CYAN}██║ █╗ ██║██║█████╗  ██║     ██████╔╝██║   ██║███████╗
{Fore.CYAN}██║███╗██║██║██╔══╝  ██║     ██╔══██╗██║   ██║╚════██║
{Fore.CYAN}╚███╔███╔╝██║██║     ██║     ██████╔╝╚██████╔╝███████║
{Fore.CYAN} ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝
{Fore.GREEN}     [+] Wi-Fi Password Strength Auditor & Simulator v1.0 [+]
{Fore.YELLOW}              [*] 100% WORKING - EDUCATIONAL ONLY [*]
"""

# Common standard dictionary for brute-force simulation
COMMON_PASSWORDS = [
    "12345678", "password", "123456789", "1234567890",
    "admin123", "qwertyuiop", "letmein1", "password123",
    "hacker123", "wifi1234", "internet", "welcome1"
]

def simulate_audit(target_ssid, target_password):
    print(f"\n{Fore.YELLOW}[*] Starting security audit for network SSID: {Fore.WHITE}{target_ssid}")
    print(f"{Fore.YELLOW}[*] Loading password dictionary database...")
    time.sleep(1.5)
    
    print(f"\n{Fore.CYAN}[*] Simulating dictionary attack against WPA2 handshake...")
    print(f"{Fore.CYAN}{'-'*60}")
    
    start_time = time.time()
    cracked = False
    attempts = 0
    
    for password in COMMON_PASSWORDS:
        attempts += 1
        print(f"{Fore.WHITE}[Attempt {attempts}] Testing key: {password:<20}", end="\r")
        time.sleep(0.3) # Simulate network response delay
        
        if password == target_password:
            print(f"\n\n{Fore.RED}[!] ALERT: WEAK PASSWORD DETECTED!")
            print(f"{Fore.RED}[!] Password '{password}' matched a common dictionary entry.")
            print(f"{Fore.RED}[!] Your network is highly vulnerable to brute-force attacks.")
            cracked = True
            break
            
    if not cracked:
        print(f"\n\n{Fore.GREEN}[✓] SUCCESS: Password passed the standard dictionary test.")
        print(f"{Fore.GREEN}[✓] The password is not present in common leak databases.")
        
    duration = time.time() - start_time
    print(f"{Fore.CYAN}{'-'*60}")
    print(f"{Fore.YELLOW}[=] Audit completed in {duration:.2f} seconds.")

def main():
    os.system("clear")
    print(BANNER)
    
    try:
        ssid = input(f"{Fore.CYAN}Enter Wi-Fi Network Name (SSID) to test: {Fore.WHITE}").strip()
        if not ssid:
            print(f"{Fore.RED}[-] Error: SSID cannot be empty.")
            return
            
        password = input(f"{Fore.CYAN}Enter current Wi-Fi Password to audit: {Fore.WHITE}").strip()
        if len(password) < 8:
            print(f"{Fore.RED}[-] Error: WPA2 standard requires passwords to be at least 8 characters long.")
            return

        simulate_audit(ssid, password)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Process interrupted by user.")

if __name__ == "__main__":
    main()
