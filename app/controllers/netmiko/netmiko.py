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


# Obtém a configuração detalhada de uma interface de um dispositivo Juniper
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


# Faz o set da configuração de uma interface unit
def set_interface_unit(hostname, username, password, unit, description,
                       bandwidth, ipv4_gw, ipv6_gw, ipv6_cli, inet6_48):
    router = {
        'device_type': 'juniper',
        'host': hostname,
        'username': username,
        'password': password,
    }
    ssh = ConnectHandler(**router)
    ssh.send_config_set(f'set interfaces ae0 unit {unit} description "{description}"                                                    ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} vlan-id {unit}                                                                 ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet filter output PROTECT-CLIENTES                                     ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet policer input {bandwidth}mb-filter output {bandwidth}mb-filter     ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet sampling input output                                              ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet address {ipv4_gw}/30                                               ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet6 policer input {bandwidth}mb-filter output {bandwidth}mb-filter    ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet6 sampling input output                                             ')  # noqa: E501
    ssh.send_config_set(f'set interfaces ae0 unit {unit} family inet6 address {ipv6_gw}/126                                             ')  # noqa: E501
    ssh.send_config_set(f'set routing-options rib inet6.0 static route {inet6_48}/48 next-hop {ipv6_cli}                                ')  # noqa: E501

    ssh.commit()  # not yet, but, soon

    output = ssh.send_command(f'run show configuration interfaces ae0 unit {unit}')  # noqa: E501
    # output = ssh.send_config_set(f'show configuration interfaces ae0 unit {unit}')

    # output = [
    #     ssh.send_config_set(f'run show configuration interfaces ae0 unit {unit}\n'),                                                        # noqa: E501
    #     ssh.send_command(f'run show configuration | display set | match {ipv6_cli}')                                                        # noqa: E501
    # ]

    ssh.disconnect()

    return output
