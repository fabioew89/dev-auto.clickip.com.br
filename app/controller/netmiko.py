from netmiko import ConnectHandler

def sh_int_terse(host, username, password):
    vroute = {
        'device_type':'juniper',''
        'host': host,
        'username': username,
        'password': password,
    }

    ssh = ConnectHandler(**vroute)

    # hostname = ssh.find_prompt()
    output = ssh.send_command('show interfaces terse lo0 | match lo')
    ssh.disconnect()

    return output

def sh_config_int_unit(host, username, password, unit):
    vroute = {
        'device_type':'juniper',''
        'host': host,
        'username': username,
        'password': password,
    }

    ssh = ConnectHandler(**vroute)

    # hostname = ssh.find_prompt()
    output = ssh.send_command(f'show configuration interfaces ae0 unit { unit }')
    ssh.disconnect()

    return output
