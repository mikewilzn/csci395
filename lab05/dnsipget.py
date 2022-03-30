import dns
from dns import resolver
import sys

# Checks to make sure user entered exactly one domain
if len(sys.argv) != 2:
    sys.exit("Usage: python3 " + sys.argv[0] + " <domain name>")

domain = sys.argv[1]

# Handles invalid domains
try:
    ip = dns.resolver.resolve(domain, 'A')[0]
except Exception:
    print("Failed to resolve", domain)
    sys.exit()


print("ip of", domain, "is", ip)