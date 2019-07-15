#!/home/tfermendzin/VENV/py3_venv/bin/python3
 
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
	'host': 'cisco3.lasthop.io',
	'username': 'pyclass',
	'password': getpass(),
	'device_type': 'cisco_ios_ssh',
	'session_log': 'dev1_session.txt'
}

device2 = {
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': getpass(),
	'device_type': 'cisco_ios_ssh',
	'session_log': 'dev2_session.txt'
}

devices = [device1, device2]

for device in devices:
    print('~'*79)
    print('Connecting to {}'.format(device['host']))
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())