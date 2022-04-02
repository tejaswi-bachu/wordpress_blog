# Example to list PERC HBAs on a ESXi host

from get_perc_hbas import VMWareClient


esxi_host_ip = '192.168.10.10'
esxi_host_username = 'root'
esxi_host_password = 'esxipassword'
		
vmware_client = VMWareClient(esxi_host_ip, esxi_host_username, esxi_host_password)	
perc_hbas = vmware_client.get_perc_hbas()
print(perc_hbas)
