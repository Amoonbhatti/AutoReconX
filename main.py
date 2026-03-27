import argparse
import os
import json
from colorama import Fore, init

from modules.whois_lookup import run_whois
from modules.subdomain_enum import find_subdomains
from modules.dns_enum import get_dns_records
from modules.port_scan import run_nmap
from modules.dir_bruteforce import run_dir_bruteforce
from modules.live_check import run_live_check
from modules.ssl_check import check_ssl
from modules.findings import analyze_findings
from reports.html_report import generate_html_report
from utils.banner import show_banner

init(autoreset=True)


def main():
    show_banner()

    parser = argparse.ArgumentParser(description="AutoReconX - Automated Recon Tool")
    parser.add_argument("-t", "--target", help="Target domain or IP")   # ✅ FIXED

    # FLAGS
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--dns", action="store_true")
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--dirb", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--ssl", action="store_true")
    parser.add_argument("--findings", action="store_true")
    parser.add_argument("--html", action="store_true")

    args = parser.parse_args()

    # 🔥 USER INPUT SYSTEM
    if not args.target:
        target = input(Fore.YELLOW + "[?] Enter Target (domain/IP): ").strip()
        if not target:
            print(Fore.RED + "[-] Invalid target. Exiting...")
            exit()
    else:
        target = args.target

    print(Fore.YELLOW + f"[+] Target: {target}")

    # FULL SCAN
    if not any(vars(args).values()):
        print(Fore.CYAN + "[+] Running FULL recon")
        args.whois = args.subdomains = args.dns = args.scan = True
        args.dirb = args.live = args.ssl = args.findings = args.html = True

    results = {}
    target_dir = f"results/{target}"
    os.makedirs(target_dir, exist_ok=True)

    # LIVE
    if args.live:
        print(Fore.CYAN + "[+] Live Check...")
        results["live"] = run_live_check(target)

    # SSL
    if args.ssl:
        print(Fore.CYAN + "[+] SSL Check...")
        results["ssl"] = check_ssl(target)

    # WHOIS
    if args.whois:
        print(Fore.CYAN + "[+] WHOIS...")
        results["whois"] = run_whois(target)

    # SUBDOMAIN
    if args.subdomains:
        print(Fore.CYAN + "[+] Subdomains...")
        results["subdomains"] = find_subdomains(target)

    # DNS
    if args.dns:
        print(Fore.CYAN + "[+] DNS...")
        results["dns"] = get_dns_records(target)

    # PORT SCAN
    if args.scan:
        print(Fore.CYAN + "[+] Nmap Scan...")
        results["nmap"] = run_nmap(target)

    # DIR BRUTE
    if args.dirb:
        print(Fore.CYAN + "[+] Directory Bruteforce...")
        results["dir_bruteforce"] = run_dir_bruteforce(target)

    # FINDINGS
    if args.findings:
        print(Fore.CYAN + "[+] Analyzing Findings...")
        findings = analyze_findings(results)
        results["findings"] = findings
        for f in findings:
            print(Fore.RED + f)

    # SAVE JSON
    json_path = f"{target_dir}/output.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=4)

    print(Fore.GREEN + f"[+] JSON saved: {json_path}")

    # HTML REPORT
    if args.html:
        print(Fore.CYAN + "[+] Generating HTML Report...")
        html_path = f"{target_dir}/report.html"
        generate_html_report(target, results, html_path)
        print(Fore.GREEN + f"[+] HTML Report saved: {html_path}")


if __name__ == "__main__":
    main()