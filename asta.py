import warnings
import urllib3
import requests
import whois
import nmap
import dns.resolver
import os
import subprocess
import importlib.util
from termcolor import cprint
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pyfiglet

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Banner
def banner():
    ascii_banner = pyfiglet.figlet_format("AstaScannerV1")
    cprint(ascii_banner, 'cyan')
    cprint("Created by Madriztra", 'cyan')

# Information Gathering (WHOIS)
def whois_info(domain, proxies=None):
    cprint(f"\n[INFO] WHOIS Information for {domain}:", 'yellow')
    w = whois.whois(domain)
    cprint(w, 'green')

# DNS Lookup
def dns_lookup(domain):
    cprint(f"\n[INFO] DNS Lookup for {domain}:", 'yellow')
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            cprint(f"IP: {rdata}", 'green')
    except Exception as e:
        cprint(f"[!] DNS Error: {e}", 'red')

# Detect CMS/Framework
def detect_framework(url):
    cprint(f"\n[INFO] Detecting CMS/Framework for {url}:", 'yellow')
    try:
        session = requests.Session()
        res = session.get(url, verify=False)  # Set verify=True for better security
        text = res.text
        cms_name = None
        if 'wp-content' in text:
            cms_name = 'wordpress'
            cprint("[+] Detected: WordPress", 'green')
        elif 'Joomla!' in text:
            cms_name = 'joomla'
            cprint("[+] Detected: Joomla", 'green')
        elif 'Drupal' in text:
            cms_name = 'drupal'
            cprint("[+] Detected: Drupal", 'green')
        elif 'Laravel' in text:
            cms_name = 'laravel'
            cprint("[+] Detected: Laravel", 'green')
        elif 'Next.js' in text:
            cms_name = 'nextjs'
            cprint("[+] Detected: Next.js", 'green')
        elif 'CodeIgniter' in text:
            cms_name = 'codeigniter'
            cprint("[+] Detected: CodeIgniter", 'green')
        else:
            cprint("[!] CMS/Framework tidak terdeteksi.", 'yellow')

        # Auto exploit langsung
        auto_exploit(url, cms_name)

    except requests.exceptions.SSLError as e:
        cprint(f"[!] SSL Error: {e}", 'red')
    except Exception as e:
        cprint(f"[!] CMS detection error: {e}", 'red')

# Admin Panel Finder
def find_admin_panels(base_url):
    cprint(f"\n[INFO] Mencari admin panel di {base_url}", 'yellow')
    
    # List of possible admin panel paths (including .php and no extensions)
    paths = [
        'admin', 'administrator', 'wp-admin', 'admin/login', 'login', 'cpanel', 
        'adminpanel', 'login.php', 'admin.php', 'panel.php', 'dashboard.php', 'adminpanel.php',
        'cpanel.php', 'login', 'admin/', 'administrator/', 'admin.php', 'adminpanel/', 'controlpanel', 
        'panel', 'adminlogin', 'dashboard', 'manage', 'admin_control'
    ]
    
    for path in paths:
        url = urljoin(base_url, path)
        try:
            # Disable SSL certificate verification by setting verify=False
            res = requests.get(url, verify=False)
            
            # Check for 200 OK status code
            if res.status_code == 200:
                cprint(f"[+] Admin Panel ditemukan: {url}", 'green')
            elif res.status_code == 403:  # Forbidden, sometimes it's valid but restricted
                cprint(f"[!] Admin Panel ditemukan, tapi akses ditolak: {url}", 'yellow')
        except requests.RequestException as e:
            cprint(f"[!] Error scanning {url}: {str(e)}", 'red')


# Nmap - only important ports
def nmap_scan(domain):
    cprint(f"\n[INFO] Nmap scan untuk {domain}", 'yellow')
    important_ports = '21,22,23,25,53,80,110,143,443,3306,8080'
    try:
        nm = nmap.PortScanner()
        nm.scan(domain, important_ports)
        for host in nm.all_hosts():
            cprint(f"[+] Host: {host} ({nm[host].hostname()})", 'green')
            for proto in nm[host].all_protocols():
                for port in nm[host][proto].keys():
                    state = nm[host][proto][port]['state']
                    cprint(f" - Port {port}/{proto}: {state}", 'cyan')
    except Exception as e:
        cprint(f"[!] Nmap error: {e}", 'red')

# Nuclei scan
def run_nuclei_scan(url):
    cprint(f"\n[INFO] Menjalankan nuclei scan untuk {url}", 'yellow')
    try:
        subprocess.run(["nuclei", "-u", url], check=True)
    except Exception as e:
        cprint(f"[!] Nuclei error: {e}", 'red')

# Auto exploit stub (can integrate exploit-db or custom scripts)
def auto_exploit(url, cms_name=None):
    cprint(f"\n[INFO] Menjalankan auto exploit untuk {url}", 'yellow')
    if not cms_name:
        cprint("[!] CMS tidak diketahui, lewati exploit otomatis", 'red')
        return
    try:
        exploit_path = f"exploit/{cms_name.lower()}.py"
        if not os.path.isfile(exploit_path):
            cprint(f"[!] Belum ada exploit untuk CMS {cms_name}", 'magenta')
            return

        spec = importlib.util.spec_from_file_location("exploit_module", exploit_path)
        exploit_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(exploit_module)

        exploit_module.run(url)

    except Exception as e:
        cprint(f"[!] Auto exploit error: {e}", 'red')

# Main
def main():
    banner()
    target = input("[?] Domain/IP target: ").strip()
    base_url = input("[?] Pilih protokol (http/https): ").strip() + "://" + target + "/"

    whois_info(target)
    dns_lookup(target)
    detect_framework(base_url)
    find_admin_panels(base_url)
    nmap_scan(target)
    run_nuclei_scan(base_url)
    auto_exploit(base_url)

if __name__ == "__main__":
    main()

