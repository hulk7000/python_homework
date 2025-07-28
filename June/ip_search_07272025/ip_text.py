import re

show = """vlan10   192.168.189.254     YES      CONFIG    up
vlan20   172.16.1.2     YES      CONFIG    down
vlan10   10.16.5.254     YES      CONFIG    up
vlan20   88.168.4.254     YES      CONFIG    down   
vlan10   77.168.5.254     YES      CONFIG    up
vlan1   22.16.1.2     YES      CONFIG    down
vlan100   33.16.5.254     YES      CONFIG    up
vlan20   44.168.4.254     YES      CONFIG    down   
vlan10   55.168.5.254     YES      CONFIG    down
vlan10   110.16.5.254     YES      CONFIG    down
vlan20   188.168.4.254     YES      CONFIG    down   
vlan10   177.168.5.254     YES      CONFIG    down
vlan1   221.16.1.2     YES      CONFIG    down
vlan100   233.16.5.254     YES      CONFIG    up
vlan20   14.168.4.254     YES      CONFIG    down   
vlan10   155.168.5.254     YES      CONFIG    down
"""

re_all_list = re.findall(r'(vlan\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(up|down)\s+',show)
