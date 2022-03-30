import dns
from dns import resolver
import sys

def main():
    # Checks to make sure user entered exactly one domain
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 " + sys.argv[0] + " <domain name>")

    domain = sys.argv[1]

    record_types = {'A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT'}
    for type in record_types:
        resolve(domain, type)

def resolve(domain, type):
    try:
        records = dns.resolver.resolve(domain, type)
    except Exception:
        print("Failed to resolved", type, "records for", domain)
        return
    for record in records:
        print(domain, "\t", type, "\t", record)

if __name__=="__main__":
    main()