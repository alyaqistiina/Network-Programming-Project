# Sample Output — Network Configuration Playbook

## Command
ansible-playbook -i ansible/network/inventory.yml ansible/network/configure_device.yml

## Output
PLAY [Configure Cisco IOS-XR Device via NETCONF] ***************************
TASK [Configure banner login] **********************************************
ok: [ios_xr]
TASK [Create local user account] *******************************************
fatal: [ios_xr]: FAILED! => sandbox AAA restriction
...ignoring
TASK [Configure interface description] *************************************
ok: [ios_xr]
TASK [Configure interface IP address] **************************************
ok: [ios_xr]
TASK [Configure static route] **********************************************
changed: [ios_xr]
PLAY RECAP *****************************************************************
ios_xr : ok=5  changed=1  failed=0  skipped=0  rescued=0  ignored=1

## Notes
- Banner, interface description, IP address, and static route all applied successfully.
- User account task fails due to DevNet sandbox AAA restrictions (expected behaviour).
