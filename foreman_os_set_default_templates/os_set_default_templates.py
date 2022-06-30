import requests
requests.packages.urllib3.disable_warnings()

HEADERS = {'content-type': 'application/json'}


class ForemanClient:
    def __init__(self, url, credentials):
	    self.url = url
		self.credentials = credentials
		
    def get_template_by_id(self, template_id):
        url = '{}/{}/{}'.format(self.url, "config_templates", template_id)
        template = requests.get(url, auth=self.credentials, verify=False)
        return template.json()

    def set_os_default_templates(self, os_id, template_ids):
        for template_id in template_ids:
            template = get_template_by_id(template_id)
            url = '{}/{}/{}/{}'.format(self.url, "operatingsystems", os_id, "os_default_templates")
            payload = {"os_default_template": {"config_template_id": str(template_id), "template_kind_name":template['template_kind_name']}}
            requests.post(url, headers=HEADERS, auth=self.credentials, json=payload, verify=False)
