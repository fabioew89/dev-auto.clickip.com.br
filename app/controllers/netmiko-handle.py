from netmiko import ConnectHandler
from getpass import getpass

vroute = {
    'device_type':'juniper',''
    'host':input(f'host: '),
    'username': input(f'username: '),
    'password': getpass(f'senha: '),
    # 'port':'22',
    # 'secret':''
}

ssh = ConnectHandler(**vroute)

print()
print(ssh.find_prompt())
print(ssh.send_command('show interfaces terse lo0 | match lo'))
ssh.disconnect()