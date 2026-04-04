import os

def run_dir_bruteforce(target):
    print(f"[+] Starting directory brute force on {target}")

    url = f"http://{target}"
    wordlist = "wordlist.txt"  # ya apni path

    output_path = f"results/{target}/directories.txt"

    # folder ensure karo
    os.makedirs(f"results/{target}", exist_ok=True)

    command = f"gobuster dir -u {url} -w {wordlist} -o {output_path}"

    os.system(command)

    print(f"[+] Directory scan saved to {output_path}")