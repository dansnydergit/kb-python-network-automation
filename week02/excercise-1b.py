from netmiko import ConnectHandler
from getpass import getpass


username = input('Username: ')
password = getpass()

sw1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.158.101',
    'username': username,
    'password': password
}

net_connect = ConnectHandler(**sw1)

output = net_connect.send_command('ping', expect_string=r'Protocol')
output = net_connect.send_command("\n", expect_string=r'Target IP address', strip_prompt=False, strip_command=False)
output += net_connect.send_command("192.168.158.101", expect_string=r'Repeat count', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Datagram size', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Timeout in seconds', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Extended commands', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'Sweep range of sizes', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'#', strip_prompt=False, strip_command=False)
 
net_connect.disconnect()

print()
print(output)
print()