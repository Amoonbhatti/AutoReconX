import subprocess

def run_whois(target):
    try:
        result = subprocess.check_output(["whois", target], text=True)
        return result
    except Exception as e:
        return f"WHOIS failed: {str(e)}"