from netmiko import ConnectHandler
from getpass import getpass

vroute = {
    'device_type':'juniper',
    'password':getpass(f'senha: '),
    # 'port':'22',
    # 'secret':''
}

ssh = ConnectHandler(**vroute)

print(ssh.find_prompt())
print(ssh.send_command('show interfaces terse lo0 | match lo'))
ssh.disconnect()