import requests

def scan_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "' OR '1'='2"]
    for payload in sql_payloads:
        full_url = f"{url}?id={payload}"
        response = requests.get(full_url)
        if response.status_code == 200 and "error" in response.text.lower():
            print(f"SQL Injection vulnerability found with payload: {payload}")
            return True
    return False

def scan_xss(url):
    xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    for payload in xss_payloads:
        full_url = f"{url}?q={payload}"
        response = requests.get(full_url)
        if response.status_code == 200 and payload in response.text:
            print(f"XSS vulnerability found with payload: {payload}")
            return True
    return False

def main(url):
    print(f"Scanning {url} for vulnerabilities...")
    if scan_sql_injection(url):
        print("SQL Injection vulnerability detected!")
    else:
        print("No SQL Injection vulnerability detected.")

    if scan_xss(url):
        print("XSS vulnerability detected!")
    else:
        print("No XSS vulnerability detected.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        
        target_url = "https://www.exploit-db.com/"
    else:
        target_url = sys.argv[1]
    main(target_url)
