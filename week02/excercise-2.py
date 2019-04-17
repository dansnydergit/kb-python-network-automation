"""
Using IOS device and 'show cdp neighbors' instead of nx-os device and 'show lldp neighbors'
"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

username = input('Username: ')
password = getpass()

sw1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.158.101',
    'username': username,
    'password': password,
    'global_delay_factor': 2
}

sw2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.158.102',
    'username': username,
    'password': password
}

cmd = 'show cdp neighbors'

# global_delay_factor = 2
start_time = datetime.now()
net_connect = ConnectHandler(**sw1)
output = net_connect.send_command(cmd)
end_time = datetime.now()
print('*' * 25)
print("Execution Time: {}\n".format(end_time-start_time))
print(output)
print('*' * 25)
print()

# delay_factor = 8
start_time = datetime.now()
net_connect = ConnectHandler(**sw1)
output = net_connect.send_command(cmd, delay_factor=8)
end_time = datetime.now()
print('*' * 25)
print("Execution Time: {}\n".format(end_time-start_time))
print(output)
print('*' * 25)
print()

net_connect.disconnect()