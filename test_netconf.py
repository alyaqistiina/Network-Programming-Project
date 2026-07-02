import socket
from ncclient import manager

hostname = 'sandbox-iosxr-1.cisco.com'
ip = socket.gethostbyname(hostname)
print('Resolved: ' + ip)
print('Connecting...')

try:
    m = manager.connect(
        host=ip,
        port=830,
        username='azzlkrmn',
        password='T-gB-2u4OW9JSPpb',
        hostkey_verify=False,
        look_for_keys=False,
        allow_agent=False,
        device_params={'name': 'default'}
    )
    print('SUCCESS! Session ID: ' + str(m.session_id))
    m.close_session()
except Exception as e:
    print('Error: ' + str(e))
