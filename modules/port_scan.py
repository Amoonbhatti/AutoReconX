import subprocess

def run_nmap(target):
    try:
        result = subprocess.check_output(
            ["nmap", "-sV", "-F", target],
            text=True
        )
        return result
    except Exception as e:
        return f"Nmap scan failed: {str(e)}"