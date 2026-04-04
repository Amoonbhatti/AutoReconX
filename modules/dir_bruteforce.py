def run_dir_bruteforce(target, wordlist):
    import subprocess
    import os

    print(f"[+] Starting directory brute force on {target}")

    cmd = f"gobuster dir -u http://{target} -w {wordlist} -q"

    result = subprocess.getoutput(cmd)

    os.makedirs(f"results/{target}", exist_ok=True)

    with open(f"results/{target}/directories.txt", "w") as f:
        f.write(result)

    return result