import ipaddress

def verifyPrefix(ip, ip_prefix):
    if ipaddress.ip_address(ip) in ipaddress.ip_network(ip_prefix):
        print(f"IP {ip} está presente no prefixo {ip_prefix}")
    else:
        print(f"IP {ip} não está presente no prefixo {ip_prefix}")

ip = "192.168.1.5"
ip_prefix = "192.168.1.0/24"

verifyPrefix(ip, ip_prefix)