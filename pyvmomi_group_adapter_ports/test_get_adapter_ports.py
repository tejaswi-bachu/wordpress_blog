# Example to group adapter ports on a ESXi host

from get_adapter_ports import VMWareClient


esxi_host_ip = '192.168.10.10'
esxi_host_username = 'root'
esxi_host_password = 'esxipassword'
		
vmware_client = VMWareClient(esxi_host_ip, esxi_host_username, esxi_host_password)	
vmware_client.print_adapters_ports()
