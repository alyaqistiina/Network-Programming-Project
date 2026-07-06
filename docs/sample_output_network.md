# Sample Output — Network Configuration Playbook

## Command
ansible-playbook -i ansible/network/inventory.yml ansible/network/configure_device.yml

## Output
```bash
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
```

## Command
docker exec -it ansible-control ansible-playbook -i /ansible/network/inventory.yml /ansible/network/retrieve_info.yml

## Output
```bash
PLAY [Retrieve Cisco IOS-XR Device Info via NETCONF] **************************************

TASK [Pull device running interface configurations] ***************************************
ok: [ios_xr]

TASK [Print retrieved device facts] *******************************************************
ok: [ios_xr] => {
    "xr_device_facts.stdout_lines": [
        "<data xmlns=\"urn:ietf:params:xml:ns:netconf:base:1.0\" xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">",
        "  <interface-configurations xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg\">",
        "   <interface-configuration>",
        "    <active>act</active>",
        "    <interface-name>Loopback0</interface-name>",
        "    <interface-virtual/>",
        "    <description>Modificado via NETCONF - Modelo YANG</description>",
        "    <ipv4-network xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg\">",
        "     <addresses>",
        "      <primary>",
        "       <address>1.1.1.1</address>",
        "       <netmask>255.255.255.255</netmask>",
        "      </primary>",
        "     </addresses>",
        "    </ipv4-network>",
        "   </interface-configuration>",
        "   <interface-configuration>",
        "    <active>act</active>",
        "    <interface-name>Loopback100</interface-name>",
        "    <interface-virtual/>",
        "    <description>Configurado con Ansible - Infraestructura como Codigo</description>",
        "    <ipv4-network xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg\">",
        "     <addresses>",
        "      <primary>",
        "       <address>10.99.99.1</address>",
        "       <netmask>255.255.255.255</netmask>",
        "      </primary>",
        "     </addresses>",
        "    </ipv4-network>",
        "    <shutdown/>",
        "   </interface-configuration>",
        "   <interface-configuration>",
        "    <active>act</active>",
        "    <interface-name>MgmtEth0/RP0/CPU0/0</interface-name>",
        "    <ipv4-network xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg\">",
        "     <addresses>",
        "      <primary>",
        "       <address>10.10.20.101</address>",
        "       <netmask>255.255.255.0</netmask>",
        "      </primary>",
        "     </addresses>",
        "    </ipv4-network>",
        "   </interface-configuration>",
        "   <interface-configuration>",
        "    <active>act</active>",
        "    <interface-name>GigabitEthernet0/0/0/0</interface-name>",
        "    <description>to xrd-2 Gi0/0/0/0</description>",
        "    <ipv4-network xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg\">",
        "     <addresses>",
        "      <primary>",
        "       <address>10.1.2.1</address>",
        "       <netmask>255.255.255.0</netmask>",
        "      </primary>",
        "     </addresses>",
        "    </ipv4-network>",
        "   </interface-configuration>",
        "   <interface-configuration>",
        "    <active>act</active>",
        "    <interface-name>GigabitEthernet0/0/0/1</interface-name>",
        "    <description>Configured by Ansible NETCONF - NetOps Team</description>",
        "    <ipv4-network xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg\">",
        "     <addresses>",
        "      <primary>",
        "       <address>192.168.100.1</address>",
        "       <netmask>255.255.255.0</netmask>",
        "      </primary>",
        "     </addresses>",
        "    </ipv4-network>",
        "   </interface-configuration>",
        "  </interface-configurations>",
        " </data>"
    ]
}

PLAY RECAP ********************************************************************************
ios_xr                     : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Notes
- Banner, interface description, IP address, and static route all applied successfully.
- User account task fails due to DevNet sandbox AAA restrictions (expected behaviour).
