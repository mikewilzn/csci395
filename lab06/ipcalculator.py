import sys
import math

def main():
    (address, prefix) = sys.argv[1].split('/')
    prefix = int(prefix)
    octets = address.split('.')
    
    for index in range(len(octets)):
        octets[index] = int(octets[index])
        if octets[index] > 255:
            print("Octets cannot be larger than 255")
            exit()

    if prefix < 1 or prefix > 32:
        print("CIDR prefix must be between 1 and 32 inclusive")
        exit()

    subnet_mask = [0, 0, 0, 0]

    for bit in range(prefix):
        subnet_mask[bit // 8] += (1 << (7 - bit % 8))

    network_id = [0, 0, 0, 0]
    for octet in range(len(octets)):
        network_id[octet] = int(octets[octet] & subnet_mask[octet])


    broadcast_address = [0, 0, 0, 0]
    for index in range(len(broadcast_address)):
        broadcast_address[index] = octets[index] | (0xff & ~subnet_mask[index])

    total_hosts = int(math.pow(2, (32 - prefix)))
    
    hosts_range_min = network_id
    hosts_range_min[-1] += 1

    hosts_range_max = broadcast_address
    hosts_range_max[-1] -= 1

    print("Network ID:", ip_format(network_id))
    print("Subnet mask:", ip_format(subnet_mask))
    print("Broadcast address:", ip_format(broadcast_address))
    print("Total hosts:", total_hosts)
    print("Usable hosts:", total_hosts - 2)
    print("Host range:", ip_format(hosts_range_min), "-", ip_format(hosts_range_max))

def ip_format(ip):
    return "{0}.{1}.{2}.{3}".format(ip[0], ip[1], ip[2], ip[3])

if __name__ == '__main__':
    main()
