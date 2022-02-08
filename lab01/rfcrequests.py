import sys, requests

try:
    rf_num = int(sys.argv[1])
except (IndexError, ValueError):
    print('Please provide an RFS number as first argument e.g. in Terminal, type: python3 urllib.py RFC num')
    sys.exit(2)

source = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = source.format(rf_num)
rfc_raw = requests.get(url)
rfc = rfc_raw.text
print(rfc)


