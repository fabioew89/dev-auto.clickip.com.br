from netmiko import ConnectHandler


def get_interface_configuration(host, username, password, unit):
    router = {
        'device_type': 'juniper',
        'host': host,
        'username': username,
        'password': password,
    }
    ssh = ConnectHandler(**router)
    output = ssh.send_command(f'show configuration interfaces ae0 unit {unit}')
    ssh.disconnect()
    return output
