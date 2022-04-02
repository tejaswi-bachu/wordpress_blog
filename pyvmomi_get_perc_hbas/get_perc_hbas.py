import atexit

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

    def get_hosts(self):
        host_view = self._content.viewManager.CreateContainerView(self._content.rootFolder, [vim.HostSystem], True)
        hosts = [host for host in host_view.view]
        host_view.Destroy()
        return hosts

    def get_hbas(self, host=None):
        if host is None:
            host = self.get_hosts()[0]
        host_st_system = host.configManager.storageSystem
        device_info = host_st_system.storageDeviceInfo
        hbas = []
        for hba in device_info.hostBusAdapter:
            hba_details = {}
            hba_details['name'] = hba.device
            hba_details['model'] = hba.model
            hba_details['driver'] = hba.driver
            hbas.append(hba_details)
        return hbas

    def get_perc_hbas(self):
        return list(filter(lambda x:'PERC' in x['model'] or 'HBA' in x['model'], self.get_hbas()))
