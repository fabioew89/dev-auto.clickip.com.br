from netmiko import ConnectHandler


# Obtém o resumo das interfaces de um dispositivo Juniper
def get_interface_summary(host, username, password):
    router = {
        'device_type': 'juniper',
        'host': host,
        'username': username,
        'password': password,
    }
    ssh = ConnectHandler(**router)
    output = ssh.send_command('show interfaces terse lo0 | match lo')
    ssh.disconnect()
    return output
