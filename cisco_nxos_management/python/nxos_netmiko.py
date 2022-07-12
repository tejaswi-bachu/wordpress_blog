from netmiko import ConnectHandler

cisco_nxos_switch = {
    'device_type': 'cisco_nxos',
    'host':   '192.168.20.100',
    'username': 'admin',
    'password': 'password',
}

net_connect = ConnectHandler(**cisco_nxos_switch)


def configure_interface_ip(interface, ip_addr):
    commands = [f"interface {interface}", "no switchport", 
            f"ip address {ip_addr}", "no shutdown", "exit"]
    output = net_connect.send_config_set(commands)
    print(output)

def remove_interface_ip(interface, ip_addr):
    commands = [f"interface {interface}", f"no ip address {ip_addr}", 
            "switchport", "shutdown", "exit"]
    output = net_connect.send_config_set(commands)
    print(output)


"""
Example function calls

interface = "Eth1/20"
ip_addr = "172.168.10.20/24"

configure_interface_ip(interface, ip_addr)
remove_interface_ip(interface, ip_addr)
"""
