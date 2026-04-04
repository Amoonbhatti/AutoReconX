# AutoReconX 🔍

**Automated Reconnaissance & Security Analysis Tool**

Developed by **Amoon Bhatti**
YouTube: **Technical Haroon**

---

## 🚀 Overview

AutoReconX is a modular and automated reconnaissance tool built for penetration testers, cybersecurity students, and researchers.

The goal of this tool is simple:
👉 **Collect → Analyze → Report**

Instead of running multiple tools manually, AutoReconX performs full reconnaissance in a structured and efficient way — and generates clean output (JSON + HTML report) that can be used for analysis or client delivery.

---

## ⚙️ Features

### 🔎 Reconnaissance

* WHOIS Lookup
* DNS Enumeration (A, MX, NS, TXT, etc.)
* Subdomain Enumeration

### 🌐 Target Analysis

* Live Host Detection
* SSL Certificate Inspection
* Port Scanning (Nmap integration)

### 📁 Content Discovery

* Directory Bruteforce (hidden paths discovery)

### 🧠 Smart Analysis

* Automated Findings Detection
* Basic vulnerability indicators

### 📊 Reporting

* Structured JSON output
* Clean HTML report (client-friendly)

---

## 📂 Project Structure

```
autoreconx/
│── main.py
│── config.py
│── requirements.txt
│── README.md
│
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   ├── port_scan.py
│   ├── dir_bruteforce.py
│   ├── live_check.py
│   ├── ssl_check.py
│   ├── findings.py
│
├── utils/
├── reports/
│   └── html_report.py
│
├── results/
```

---

## 🧪 Installation

Clone the repository:

```bash
git clone https://github.com/Amoonbhatti/AutoReconX.git
cd autoreconx
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure **Nmap is installed** on your system.

---

## ▶️ Usage

### 🔹 Basic Scan

```bash
python main.py -t example.com
```

---

### 🔹 Full Recon (default)

If no flags are provided, AutoReconX automatically runs a full scan.

---

### 🔹 Custom Scan

```bash
python main.py -t example.com --whois --dns --scan --dirb --ssl --live
```

---

## 📌 Available Flags

| Flag           | Description           |
| -------------- | --------------------- |
| `--whois`      | WHOIS lookup          |
| `--subdomains` | Subdomain enumeration |
| `--dns`        | DNS records           |
| `--scan`       | Port scan (Nmap)      |
| `--dirb`       | Directory brute force |
| `--live`       | Live host check       |
| `--ssl`        | SSL certificate check |
| `--findings`   | Analyze findings      |
| `--html`       | Generate HTML report  |

---

## 📊 Output

After running the tool:

```
results/
 └── example.com/
      ├── output.json
      ├── report.html
```

### JSON Output

Raw structured data for further processing.

### HTML Report

Clean, readable report for quick review or sharing.

---

## ⚠️ Disclaimer

This tool is developed for **educational and authorized testing purposes only**.

Do not use this tool against targets without proper permission.
The developer is not responsible for any misuse.

---

## 🧠 Future Improvements

* Parallel scanning (faster execution)
* Advanced subdomain enumeration (APIs)
* Technology detection
* Enhanced vulnerability analysis
* PDF reporting

---

## 👨‍💻 Author

**Amoon Bhatti**
Cybersecurity Researcher & Penetration Tester

📺 YouTube: *Technical Haroon*

---

## ⭐ Support

If you found this project useful:

* Star the repository ⭐
* Share it with others
* Follow for more cybersecurity content

---

**AutoReconX — Turning Recon into Intelligence**
