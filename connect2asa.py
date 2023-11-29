from netmiko import ConnectHandler as sshto

ip = input("Bitte IP der ASA eingeben: ")
username = input("Bitte Benutzernamen eingeben: ")
password = input("Bitte Passwort eingeben: ")

def asa (ip, username, password):
    device = {
        'device_type': 'cisco_asa',
        'host': ip,
        'username': username,
        'password': password
    }
    return device

def ssh(device):
    connection = sshto(**device)
    return connection

output = ssh.send_command('show version')