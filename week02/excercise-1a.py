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

output = net_connect.send_command_timing('ping', strip_prompt=False, strip_command=False)

# loop each line until prompt is returned
end = False
ignore_cmd = False
while not end:
    if ']:' in output:
        output += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
    # ignore this IF statement if already matched
    if 'Target IP address' in output and not ignore_cmd:
        output += net_connect.send_command_timing('192.168.158.101', strip_prompt=False, strip_command=False)
        ignore_cmd = True
    if '#' in output:
        end = True
    
net_connect.disconnect()

print()
print(output)
print()