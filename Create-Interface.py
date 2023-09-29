import ipaddress as ip
import csv

#Variables
'''
-VLAN ID
-Networkaddress
-Subnetmask
-Portchannel Interface ID
-Description
'''
csvfile = open('newint.csv', 'r')
reader = csv.DictReader(csvfile)
list_net = list()

for row in reader:
    list_net.append(row)

print(list_net)

for row in list_net:
    row['netaddr']=ip.ip_address(row['netaddr'])
    row['smask']=ip.ip_address(row['smask'])

netinfo = list_net

for net in netinfo:
    ID = str(net['vlanid'])
    IP1 = str(ip.ip_address(net['netaddr']+1))
    IP2 = str(ip.ip_address(net['netaddr']+2))
    MASK = str(net['smask'])
    CONT = net['context']
    PoI = str(net['Portchannel'])
    DSC = net['Description']
    print("change context system")
    print("configure terminal")
    print("interface Port-channel" + PoI + "." + ID)
    print(" description " + DSC)
    print(" vlan "+ ID)
    print("exit")
    print("write memory")
    print("!")
    print("change context " + CONT)
    print("interface inside_" + ID)
    print(" nameif inside_" + ID)
    print(" security-level 100")
    print(" ip address " + IP1 + " " + MASK + " standby " + IP2)
    print(" exit")
    print("!")
    print("access-list inside_" + ID + "_acl extended deny icmp any4 any4 redirect")
    print("access-list inside_" + ID + "_acl extended permit icmp any4 any4")
    print("access-list inside_" + ID + "_acl remark initial rule, please delete it as soon as possible!")
    print("access-list inside_" + ID + "_acl extended permit ip any4 any4")
    print("access-list inside_" + ID + "_acl extended deny ip any4 any4")
    print("access-group inside_" + ID + "_acl in interface inside_" + ID)
    print("!")
    print("monitor-interface inside_" + ID)
    print("!")
    print("write memory")
