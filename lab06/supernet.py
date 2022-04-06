import sys
import math

addresses = []
print("Enter IP addresses:")
while True:
    ip = bin(int(input().split('/')[0].replace('.', '')))[2:].zfill(8)
    ip = input().split('/')[0].replace('.', '')
    print(ip)
    ip = int(ip)
    ip = bin(ip)[2:].zfill(8)
    if len(ip) < 2:
        break
    addresses.append(ip)

matches = 0
#while True:
#    for octet in range(len(addresses[0])):
#        for address in range(len(addresses)):
            

print(addresses)
