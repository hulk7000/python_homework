import re

# show = "GigabitEthernet1       172.16.12.1     YES NVRAM up        up"
#
# result = re.match('([A-Z][a-zA-Z]+\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES NVRAM\s+(\w+)\s+up' , show).groups()
# print(f"interface name : {result[0]}")

# arp = "Internet  172.16.12.1            -  0001.0001.0001  ARPA   GigabitEthernet1"
#  a = re.match('Internet\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*', arp)
# result_arp = re.match('Internet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[0-9\-]+\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+.*', arp).groups()
# print(result_arp)

show = """Interface       IPAddress      OK       Method    Status        
vlan10   192.168.189.254     YES      CONFIG    up
vlan20   172.16.1.2     YES      CONFIG    down
vlan10   10.16.5.254     YES      CONFIG    up
vlan20   192.168.4.254     YES      CONFIG    down   
vlan10   192.168.5.254     YES      CONFIG    up
"""
a = re.match("Interface", show)
print(a)

# a = re.split('---', 'aaa---bbb---ccc')
# print(a)

# b = re.sub('[-=]+', '...', 'aaa-------bbb---======ccc')
# print(b)