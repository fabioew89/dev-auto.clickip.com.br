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
