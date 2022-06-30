# Example to set templates with ids 10, 20 as default templates to OS with id 1 

from os_set_default_templates import ForemanClient

FOREMAN_URL = 'https://192.168.10.20/api'
FOREMAN_CREDENTIALS = ('admin', 'foreman')

os_id = 1
template_ids = (10, 20)

foreman_client = ForemanClient(FOREMAN_URL, FOREMAN_CREDENTIALS)
foreman_client.set_os_default_templates(os_id, template_ids)