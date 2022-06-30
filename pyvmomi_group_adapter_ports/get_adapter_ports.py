import atexit
import itertools

from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect, SmartConnectNoSSL


class VMWareClient:
    def __init__(self, host, user, password, port=443, insecure=True):
       if insecure:
           self._service_instance = SmartConnectNoSSL(host=host, user=user, pwd=password, port=port)
       else:
           self._service_instance = SmartConnect(host=host, user=user, pwd=password, port=port)
       self._host = host
       self._user = user
       self._password = password
       atexit.register(Disconnect, self._service_instance)
       self._content = self._service_instance.RetrieveContent()

    def get_pnics(self):
        host_view = self._content.viewManager.CreateContainerView(self._content.rootFolder, [vim.HostSystem], True)
        hosts = [host for host in host_view.view]
        host_view.Destroy() 
        host = hosts[0]
        pnics = []
        for pnic in host.config.network.pnic:
            pnic_details = {}
            pnic_device = pnic.device
            if pnic_device.startswith('vmnic'):
                if pnic.pci:
                    for pci_device in host.hardware.pciDevice:
                        if pci_device.id == pnic.pci:
                            vendor = pci_device.vendorName
                            device = pci_device.deviceName
                            driver = pnic.driver
                            mac = pnic.mac
                            device_id = pci_device.deviceId 
                            if pnic.linkSpeed:
                                status = 'Connected'
                            else:
                                status = 'Disconnected'
                            pnic_details['name'] = pnic_device
                            pnic_details['vendor'] = vendor
                            pnic_details['device'] = device
                            pnic_details['driver'] = driver
                            pnic_details['status'] = status
                            pnic_details['mac'] = mac
                            pnic_details['device_id'] = device_id
                            pnic_details['id'] = pci_device.id
                            pnics.append(pnic_details)
        return pnics

    def print_adapters_ports(self):
        pnics = self.get_pnics()
        print('Grouping ports by adapters based on MAC')
        pnics_by_mac = sorted(pnics, key=lambda x:x['mac'][:-3])
        for key, value in itertools.groupby(pnics_by_mac, key=lambda x:x['mac'][:-3]):
            print(key)
            for i in value:
                print(i.get('name'), i.get('mac'))
            print('\n')

        print('Grouping ports by adapters based on device id')
        pnics_by_device_id = sorted(pnics, key=lambda x:x['device_id'])
        for key, value in itertools.groupby(pnics_by_device_id, key=lambda x:x['device_id']):
            print(key)
            for i in value:
                print(i.get('name'), i.get('mac'))
            print('\n')

        print('Grouping ports by adapters based on bus+slot')
        pnics_by_bus_slot = sorted(pnics, key=lambda x:x['id'][5:10])
        for key, value in itertools.groupby(pnics_by_bus_slot, key=lambda x:x['id'][5:10]):
            print(key)
            for i in value:
                print(i.get('name'), i.get('mac'))
            print('\n')
