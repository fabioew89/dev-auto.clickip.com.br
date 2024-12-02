from netmiko import ConnectHandler


# Obtém o resumo das interfaces de um dispositivo Juniper
def get_interface_summary(host, username, password):
    vroute = {
        'device_type': 'juniper',
        'host': host,
        'username': username,
        'password': password,
    }

    ssh = ConnectHandler(**vroute)

    output = ssh.send_command('show interfaces terse lo0 | match lo')
    ssh.disconnect()

    return output


# Obtém a configuração detalhada de uma interface de um dispositivo Juniper
def get_interface_configuration(host, username, password, unit):
    vroute = {
        'device_type': 'juniper',
        'host': host,
        'username': username,
        'password': password,
    }

    ssh = ConnectHandler(**vroute)

    output = ssh.send_command(f'show configuration interfaces ae0 unit {unit}')
    ssh.disconnect()

    return output
