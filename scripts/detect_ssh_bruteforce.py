import re

log_file = "/var/log/auth.log"
ip_count = {}

with open(log_file) as f:
    for line in f:
        if "Failed password" in line:
            ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
            if ip:
                ip = ip[0]
                ip_count[ip] = ip_count.get(ip, 0) + 1

for ip, count in ip_count.items():
    if count >= 5:
        print(f"[SOC ALERT] SSH brute-force from {ip} ({count} attempts)")
