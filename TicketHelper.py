from netmiko import Netmiko
from netmiko import ConnectHandler

#Variables Ticket
ASAIP = "ASAIP"
ASAUser = "ASAUsername"
ASAPass = "ASAPassword"
ContextName = "ContextName"
SourceIP = "SourceIP"
DestinationIP = "DestinationIP"
DestinationPort = "DestinationPort"

#Variables to find
SourceInterface = "SourceInterface"
SourceACL = "SourceACL"

#Variables for searching
sh_routeIP = "show route "+ SourceIP + " | include directly"
sh_routeDefault = "show route 0.0.0.0 | exclude Known|Rout"
sh_ACLfromInterface = "show running-config access-group | include " + SourceInterface
sh_ACLforDestinationIP = "show access-list " + SourceACL + " | include " + DestinationIP
sh_ACLforDestinationIPandDestinationPort = "show access-list " + SourceACL + " | include " + DestinationIP + ".*" + DestinationPort
sh_ACLforSourceIP = "show access-list " + SourceACL + " | include " + SourceIP
sh_ACLforSourceIPandDestinationPort = "show access-list " + SourceACL + " | include " + SourceIP + ".*" + DestinationPort

#Device
ASA = {
    "host": ASAIP,
    "username": ASAUser,
    "password": ASAPass,
    "device_type": "cisco_asa"
}

#ssh_connection = ConnectHandler(**ASA)

#print(sh_routeIP)

'''
variable = " * directly connected, via wspap"
spl_word ="via"
spl_string = variable.split(spl_word, 1)
SourceInterface = spl_string[1]
print(SourceInterface)
'''


#get SourceInterface
#output_sh_routeIP = ssh_connection.send_command(sh_routeIP, use_textfsm=True)
output_sh_routeIP = "* directly connected, via inside_3338"
if "via" in output_sh_routeIP:
   spl_word_output_sh_routeIP ="via"
   spl_string_output_sh_routeIP = output_sh_routeIP.split(spl_word_output_sh_routeIP, 1)
   SourceInterface = spl_string_output_sh_routeIP[1]
else:
   #output_sh_routeDefault = ssh_connection.send_command(sh_routeDefault, use_textfsm=True)
   output_sh_routeDefault = "* 10.172.64.65, via outside"
   spl_word_output_sh_routeDefault ="via"
   spl_string_output_sh_routeDefault = output_sh_routeDefault.split(spl_word_output_sh_routeDefault, 1)
   SourceInterface = spl_string_output_sh_routeDefault[1]

print(SourceInterface)
#get SourceACL
#output_sh_ACLfromInterface = ssh_connection.send_command(sh_ACLfromInterface, use_textfsm=True)
output_sh_ACLfromInterface = "access-group inside_3338_acl in interface inside_3338"
spl_word_begin_output_sh_ACLfromInterface ="access-group"
spl_word_end_output_sh_ACLfromInterface ="in interface"
SourceACL = output_sh_ACLfromInterface.split(spl_word_begin_output_sh_ACLfromInterface)[1].split(spl_word_end_output_sh_ACLfromInterface)[0]

print(SourceACL)

#find similar ACLs
#output_sh_ACLforDestinationIP = ssh_connection.send_command(sh_ACLforDestinationIP, use_textfsm=True)
#output_sh_ACLforDestinationIPandDestinationPort = ssh_connection.send_command(sh_ACLforDestinationIPandDestinationPort, use_textfsm=True)
#output_sh_ACLforSourceIP = ssh_connection.send_command(sh_ACLforSourceIP, use_textfsm=True)
#output_sh_ACLforSourceIPandDestinationPort = ssh_connection.send_command(sh_ACLforSourceIPandDestinationPort, use_textfsm=True)
output_sh_ACLforDestinationIP = """
   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 443
   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 80
"""
output_sh_ACLforDestinationIPandDestinationPort = """
   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 443
"""
#output_sh_ACLforSourceIP = """
#   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 object-group DM_INLINE_NETWORK_123 object-group DM_INLINE_TCP_12
#    access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 443
#    access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 80
#    access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.2 eq 443
#    access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.2 eq 80
#"""
output_sh_ACLforSourceIP = ""
output_sh_ACLforSourceIPandDestinationPort = """
   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.1 eq 443
   access-list inside_3338_acl line 5 extended permit tcp 10.218.3.0 255.255.255.0 11.209.4.2 eq 443
"""
print(len(output_sh_ACLforSourceIP))

len_of_output_sh_ACLforDestinationIP = len(output_sh_ACLforDestinationIP)
len_of_output_sh_ACLforDestinationIPandDestinationPort = len(output_sh_ACLforDestinationIPandDestinationPort)
len_of_output_sh_ACLforSourceIP = len(output_sh_ACLforSourceIP)
len_of_output_sh_ACLforSourceIPandDestinationPort = len(output_sh_ACLforSourceIPandDestinationPort)