"""Function to rerun failed workflows"""

from fireworks.core.launchpad import Launchpad


def rerun_workflow(workflow_id):
    host = '127.0.0.1'
    port = '12345'
    db_name = 'hello'
    lpad = LaunchPad(host=host, port=port, name=db_name)
    wf = lpad.get_wf_summary_dict(workflow_id, mode='more')
    wf_states = wf['states']
    for wf_name,wf_state in wf_states.items():
        if wf_state == 'FIZZLED':
            fizzled_fw_id = wf_name.split('--')[-1]
            lpad.rerun_fw(int(fizzled_fw_id))
