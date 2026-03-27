from colorama import Fore


def info(message: str):
    print(Fore.CYAN + f"[+] {message}")


def success(message: str):
    print(Fore.GREEN + f"[+] {message}")


def warning(message: str):
    print(Fore.YELLOW + f"[!] {message}")


def error(message: str):
    print(Fore.RED + f"[ERROR] {message}")