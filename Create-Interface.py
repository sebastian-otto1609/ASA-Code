import ipaddress as ip

#Variables
'''
-VLAN ID
-Networkaddress
-Subnetmask
'''

netinfo =[
    {
        "vlanid":2487,
        "netaddr":ip.ip_address('21.196.134.0'),
        "smask":ip.ip_address('255.255.255.192'),
        "context":'bimaserverbn-ent'
    },
    {
        "vlanid":2488,
        "netaddr":ip.ip_address('21.196.134.64'),
        "smask":ip.ip_address('255.255.255.192'),
        "context":'bimaserverbn-test'
    },
    {
        "vlanid":2489,
        "netaddr":ip.ip_address('21.196.134.128'),
        "smask":ip.ip_address('255.255.255.192'),
        "context":'bimaserverbn-prod'
    }
]

for net in netinfo:
    ID = str(net['vlanid'])
    IP1 = str(ip.ip_address(net['netaddr']+1))
    IP2 = str(ip.ip_address(net['netaddr']+2))
    MASK = str(net['smask'])
    CONT = net['context']
    print("change context system")
    print("configure terminal")
    print("interface Port-channelXX." + ID)
    print(" description XXX")
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