import argparse
from modules.whois_lookup import run_whois
from modules.subdomain_enum import find_subdomains
from colorama import Fore, Style, init
from modules.dns_enum import get_dns_records
init(autoreset=True)
def banner():
    print(Fore.MAGENTA + """
========================================
        AutoReconX - Recon Tool
========================================
Developed by: Amoon Bhatti
YouTube: Technical Haroon
========================================
""")

def main():
    banner()

    parser = argparse.ArgumentParser(description="AutoReconX - Automated Recon Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP")

    args = parser.parse_args()
    target = args.target

    print(f"[+] Target set: {target}")

    # WHOIS
    print("\n[+] Running WHOIS...")
    whois_data = run_whois(target)

    print("\n----- WHOIS INFO -----")
    print(whois_data[:500])

    # SUBDOMAIN
    print("\n[+] Finding Subdomains...")
    subdomains = find_subdomains(target)

    print("\n----- SUBDOMAINS FOUND -----")

    if subdomains:
        for sub, ip in subdomains:
            print(f"- {sub} [{ip}]")
    else:
        print("No subdomains found")
        
print(Fore.CYAN + "\n[+] Gathering DNS Records...")

dns_data = get_dns_records(target)

print(Fore.YELLOW + "\n----- DNS RECORDS -----")

for rtype, values in dns_data.items():
    print(Fore.GREEN + f"\n{rtype} Records:")
    if values:
        for v in values:
            print(f"- {v}")
    else:
        print("No records found")

if __name__ == "__main__":
    main()