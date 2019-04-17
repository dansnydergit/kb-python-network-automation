from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

username = input('Username: ')
password = getpass()

sw1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.158.101',
    'username': username,
    'password': password
}

net_connect = ConnectHandler(**sw1)
commands = ['show version', 'show cdp neighbors']

for command in commands:
    output = net_connect.send_command(command, use_textfsm=True)
    print('*' * 25)
    print(command + '\n')
    pprint(output)
    print('*' * 25)
    print()

    if command == 'show cdp neighbors':
        print('CDP Data Type: {}'.format(type(output)))
        print('SW1 is connected to SW3 via port: {}\n'.format(output[0]['neighbor_interface']))

net_connect.disconnect()