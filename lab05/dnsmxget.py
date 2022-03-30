import dns
from dns import resolver
import sys

# Checks to make sure user entered exactly one domain
if len(sys.argv) != 2:
    sys.exit("Usage: python3 " + sys.argv[0] + " <domain name>")

domain = sys.argv[1]

# Handles invalid domains
try:
    results = dns.resolver.resolve(domain, 'MX')
except Exception:
    print("Failed to resolve", domain)
    sys.exit()

# 'MX' object contains both the record and the preference number
for record in results:
    print("MX Record:\t", record)