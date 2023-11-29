import ipaddress as ip
import csv
from datetime import datetime

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

#User Abfrage
q_IP =""
matches = ['high', 'low']
while not any(x in q_IP for x in matches):
    q_IP = input("Highest or lowest IP for Interface? Type high or low: ").lower()

filename_conf= datetime.now().strftime("%Y_%m_%d-") + "commands.txt"
command_list = []

'''
with open(filename_conf, 'w') as file:
    file.write("\n change context system")
    file.write("\n configure terminal")
    for net in netinfo:
        ID = str(net['vlanid'])
        PoI = str(net['Portchannel'])
        DSC = net['Description']
        file.write("\n interface Port-channel" + PoI + "." + ID)
        file.write("\n  description " + DSC)
        file.write("\n  vlan "+ ID)
    file.write("\n exit")
    for net in netinfo:
        CONT = net['context']
        PoI = str(net['Portchannel'])
        ID = str(net['vlanid'])
        file.write("\n context " + CONT)
        file.write("\n  allocate-interface Port-channel" + PoI + "." + ID + " inside_" + ID)
    file.write("\n exit")
    file.write("\n !")
    ContCheck = ""
    for net in netinfo:
        ID = str(net['vlanid'])
        getnet = str(net['netaddr']) + "/" + str(net['smask'])
        IP0 = ip.ip_network(getnet)
        l_IP0 = list(IP0.hosts())
        if q_IP =="low":
            IP1 = str(l_IP0[0])
            IP2 = str(l_IP0[1])
        elif q_IP == "high":
            IP1 = str(l_IP0[-1])
            IP2 = str(l_IP0[-2])
        MASK = str(net['smask'])
        CONT = net['context']
        if ContCheck == CONT:
            file.write("\n interface inside_" + ID)
            file.write("\n  nameif inside_" + ID)
            file.write("\n  security-level 100")
            file.write("\n  ip address " + IP1 + " " + MASK + " standby " + IP2)
            file.write("\n  exit")
            file.write("\n !")
            file.write("\n access-list inside_" + ID + "_acl extended deny icmp any4 any4 redirect")
            file.write("\n access-list inside_" + ID + "_acl extended permit icmp any4 any4")
            file.write("\n access-list inside_" + ID + "_acl remark initial rule, please delete it as soon as possible!")
            file.write("\n access-list inside_" + ID + "_acl extended permit ip any4 any4")
            file.write("\n access-list inside_" + ID + "_acl extended deny ip any4 any4")
            file.write("\n access-group inside_" + ID + "_acl in interface inside_" + ID)
            file.write("\n !")
            file.write("\n monitor-interface inside_" + ID)
            file.write("\n !")
        else:
            file.write("\n write memory")
            file.write("\n change context " + CONT)
            file.write("\n interface inside_" + ID)
            file.write("\n  nameif inside_" + ID)
            file.write("\n  security-level 100")
            file.write("\n  ip address " + IP1 + " " + MASK + " standby " + IP2)
            file.write("\n  exit")
            file.write("\n !")
            file.write("\n access-list inside_" + ID + "_acl extended deny icmp any4 any4 redirect")
            file.write("\n access-list inside_" + ID + "_acl extended permit icmp any4 any4")
            file.write("\n access-list inside_" + ID + "_acl remark initial rule, please delete it as soon as possible!")
            file.write("\n access-list inside_" + ID + "_acl extended permit ip any4 any4")
            file.write("\n access-list inside_" + ID + "_acl extended deny ip any4 any4")
            file.write("\n access-group inside_" + ID + "_acl in interface inside_" + ID)
            file.write("\n !")
            file.write("\n monitor-interface inside_" + ID)
            file.write("\n !")
        ContCheck = CONT
    file.write("\n write memory")
'''

command_list.append("change context system")
command_list.append("configure terminal")
for net in netinfo:
    ID = str(net['vlanid'])
    PoI = str(net['Portchannel'])
    DSC = net['Description']
    command_list.append("interface Port-channel" + PoI + "." + ID)
    command_list.append(" description " + DSC)
    command_list.append(" vlan "+ ID)
command_list.append("exit")
for net in netinfo:
    CONT = net['context']
    PoI = str(net['Portchannel'])
    ID = str(net['vlanid'])
    command_list.append("context " + CONT)
    command_list.append(" allocate-interface Port-channel" + PoI + "." + ID + " inside_" + ID)
command_list.append("exit")
command_list.append("!")
ContCheck = ""
for net in netinfo:
    ID = str(net['vlanid'])
    getnet = str(net['netaddr']) + "/" + str(net['smask'])
    IP0 = ip.ip_network(getnet)
    l_IP0 = list(IP0.hosts())
    if q_IP =="low":
        IP1 = str(l_IP0[0])
        IP2 = str(l_IP0[1])
    elif q_IP == "high":
        IP1 = str(l_IP0[-1])
        IP2 = str(l_IP0[-2])
    MASK = str(net['smask'])
    CONT = net['context']
    if ContCheck == CONT:
        command_list.append("interface inside_" + ID)
        command_list.append(" nameif inside_" + ID)
        command_list.append(" security-level 100")
        command_list.append(" ip address " + IP1 + " " + MASK + " standby " + IP2)
        command_list.append(" exit")
        command_list.append("!")
        command_list.append("access-list inside_" + ID + "_acl extended deny icmp any4 any4 redirect")
        command_list.append("access-list inside_" + ID + "_acl extended permit icmp any4 any4")
        command_list.append("access-list inside_" + ID + "_acl remark initial rule, please delete it as soon as possible!")
        command_list.append("access-list inside_" + ID + "_acl extended permit ip any4 any4")
        command_list.append("access-list inside_" + ID + "_acl extended deny ip any4 any4")
        command_list.append("access-group inside_" + ID + "_acl in interface inside_" + ID)
        command_list.append("!")
        command_list.append("monitor-interface inside_" + ID)
        command_list.append("!")
    else:
        command_list.append("write memory")
        command_list.append("change context " + CONT)
        command_list.append("interface inside_" + ID)
        command_list.append(" nameif inside_" + ID)
        command_list.append(" security-level 100")
        command_list.append(" ip address " + IP1 + " " + MASK + " standby " + IP2)
        command_list.append(" exit")
        command_list.append("!")
        command_list.append("access-list inside_" + ID + "_acl extended deny icmp any4 any4 redirect")
        command_list.append("access-list inside_" + ID + "_acl extended permit icmp any4 any4")
        command_list.append("access-list inside_" + ID + "_acl remark initial rule, please delete it as soon as possible!")
        command_list.append("access-list inside_" + ID + "_acl extended permit ip any4 any4")
        command_list.append("access-list inside_" + ID + "_acl extended deny ip any4 any4")
        command_list.append("access-group inside_" + ID + "_acl in interface inside_" + ID)
        command_list.append("!")
        command_list.append("monitor-interface inside_" + ID)
        command_list.append("!")
    ContCheck = CONT
command_list.append("write memory")

with open(filename_conf, 'w') as file:
	file.write('\n'.join(command_list))