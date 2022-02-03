import sys, urlib.request

try:
    rf_num = inst(sys.argv[1])
except (IndexError, ValueError):
    print('Please provide an RFS number as first argument e.g. in Terminal, type: python3 urllib.py RFC num')
    sys.exit(2)

source = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = source.format(____)
rfc_raw = urlib.request.urlopen(____).read()
rfc = rfc_raw.decode()
print(____)


