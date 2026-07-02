Member 3 (Adriana Zulaikha) - NETCONF Connection Notes:
- Sandbox: IOS XR Always-On (sandbox-iosxr-1.cisco.com)
- Port 830: confirmed reachable via nc test
- Issue: SSH handshake failure due to Python 3.8/paramiko 
  incompatibility with IOS XR SSH algorithms on labvm
- Resolution: Will test inside Docker container (Day 3/Fri)
- Playbook (configure_device.yml) written and ready for testing
