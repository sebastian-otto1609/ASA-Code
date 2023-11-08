import ipaddress as ip
import csv

'''
Hilfe um Interfaces auf einer Cisco ASA
im Multi Context Mode anzulegen.
Die Daten der Interfaces werden in einer
CSV Datei "newint.csv" an das Programm
übergeben.
'''
#Variables for csv
'''
-VLAN ID = vlanid
-Networkaddress = netaddr
-Subnetmask = smask
-Context = context
-Portchannel Interface ID = Portchannel
-Description = Description
'''
#einlesen der CSV
csvfile = open(
    'newint.csv',
     'r'
    )
reader = csv.DictReader(csvfile)
list_net = list()

#Überführen der CSV in ein Liste
for row in reader:
    list_net.append(row)

#Anpassung der IP Parameter in mit dem ipaddress Modul
for row in list_net:
    row['netaddr']=ip.ip_address(row['netaddr'])
    row['smask']=ip.ip_address(row['smask'])

#Übernahme der aktuellen Liste in eine andere Liste
netinfo = list_net

#Ausgabe der CLI Commands
print("change context system")
print("configure terminal")
for net in netinfo:
    ID = str(net['vlanid'])
    PoI = str(net['Portchannel'])
    DSC = net['Description']
    print("interface Port-channel" + PoI + "." + ID)
    print(" description " + DSC)
    print(" vlan "+ ID)
print("exit")
for net in netinfo:
    CONT = net['context']
    PoI = str(net['Portchannel'])
    ID = str(net['vlanid'])
    print("context " + CONT)
    print(" allocate-interface Port-channel" + PoI + "." + ID + " inside_" + ID)
print("exit")
print("!")
ContCheck = ""
for net in netinfo:
    ID = str(net['vlanid'])
    IP1 = str(ip.ip_address(net['netaddr']+1))
    IP2 = str(ip.ip_address(net['netaddr']+2))
    MASK = str(net['smask'])
    CONT = net['context']
    if ContCheck == CONT:
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
    else:
        print("write memory")
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
    ContCheck = CONT
print("write memory")
