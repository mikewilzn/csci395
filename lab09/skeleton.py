import getopt
import socket
import sys
import time
from scapy.all import IP,ICMP,sr1,conf

# Attempts to look up a hostname given an IP address
# Returns a hostname or False if none was found
def getHostnameFromIP(ip):
    try:
        data = socket.gethostbyaddr(ip)
        host = repr(data[0])
        return host
    except socket.herror:
        return False

# Set scapy verbosity to 0 to reduce messages on the command line
conf.verb = 0

# Remove first argument from the list of command line arguments (this is the program name)
argumentList = sys.argv[1:]

# Set the options we support
options = "h:n:"

# Set the long options we support
longOptions = []

# Set default value for number of pings
numPings = 4

# Define IP address destination variable
destination = None

try:
    # Parse command line arguments
    arguments, values = getopt.getopt(argumentList, options, longOptions)

    # Extract the values from the arguments
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-n"):
            numPings = currentValue
        elif currentArgument in ("-h"):
            destination = currentValue 
except getopt.error as err:
    # Output error
    print(str(err))

if destination is None:
    print("Please provide an IP address")
    exit()

# Create a loop for the number of ping packets you're sending

# Set the layer 3 options for the packet
layer3 = IP()
layer3.dst = destination
layer3.tos = 0
layer3.id = 0
layer3.flags = 0
layer3.frag = 0
layer3.ttl = 64
layer3.proto = 1 # icmp

# Set the layer 4 options for the packet
layer4 = ICMP()
layer4.type = 8 # echo-request
layer4.code = 0
layer4.id = 0
layer4.seq = 1

# Generate the packet to send - scapy will fill in the details for the other layers
packet = layer3 / layer4

# Capture time before our traffic is sent
# NOTE: This is a quick and dirty timing method, don't use this in production code :)
start_time = time.time()

# Sends the packet and stores the response, timeout is the max time to wait for a response in seconds
for ping in range(len(numPings)):
    start_time = time.time()
    answer = sr1(packet, timeout=2)
    end_time = time.time()
    if answer:
        print(answer)
    else:
        print("Request timed out")

# Capture time after our traffic is returned
end_time = time.time()

# ADD YOUR CODE HERE TO PRINT THE RESULTS
if answer:
    print(answer)
else:
    print("Request timed out.")
