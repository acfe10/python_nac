#!/home/tfermendzin/VENV/py3_venv/bin/python3

from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter Username: ')
password = getpass()

device1 = {
	'host': 'cisco3.lasthop.io',
	'username': username,
	'password': password,
	'device_type': 'cisco_ios_ssh',
	'session_log': 'dev1_session.txt'
}

device2 = {
	'host': 'cisco4.lasthop.io',
	'username': username,
	'password': password,
	'device_type': 'cisco_ios_ssh',
	'session_log': 'dev2_session.txt'
}

devices = [device1, device2]

for device in devices:
    print('~'*79)
    print('Connecting to {}'.format(device['host']))
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show version')
    outputFileName = device['host'] + '.showver.output.txt'
    with open(outputFileName, 'w') as write_file:
        write_file.write(output)
