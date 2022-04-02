from add_esxi_to_vcenter import VMWareClient


# Example to add an ESXi host to VCenter
vcenter_ip = '192.168.10.20'
vcenter_username = 'administrator@vsphere.local'
vcenter_password = 'vcenterpassword'

esxi_host_ip = '192.168.10.10'
esxi_host_username = 'root'
esxi_host_password = 'esxipassword'

datacenter_name = 'esxi_dc'
cluster_name = 'esxi_cluster'

vmware_client = VMWareClient(vcenter_ip, vcenter_username, vcenter_password)
vmware_client.add_host_to_vc(esxi_host_ip, esxi_host_username, esxi_host_password, datacenter_name, cluster_name)
