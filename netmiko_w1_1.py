#!/home/tfermendzin/VENV/py3_venv/bin/python3
 
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
	'host': 'cisco3.lasthop.io',
	'username': 'pyclass',
	'password': getpass(),
	'device_type': 'cisco_ios_ssh',
	'session_log': 'my_session.txt'
}

net_connect = ConnectHandler(**device1)

print(net_connect.find_prompt())