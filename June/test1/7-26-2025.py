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


# pattern = r'(vlan\d+)\s+([\d\.]+)\s+YES\s+CONFIG\s+(up|down)'
# matches = re.findall(pattern, show)

re_all_list = re.findall(r'(vlan\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES\s+CONFIG\s+(up|down)\s+',show)
# print(re_all_list)
# user_ip = input("Enter an IP to check status: ").strip()     # not finish 5
# if user_ip in re_all_list:
#     print(re_all_list[2])
# ipin = 0
# for i in re_all_list:
#     if user_ip == i[1]:
#         print(i[2])
#         ipin=1
# if ipin == 0:
#     print("No IP found")

import re

ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

while True:
    user_ip = input("Enter an IP to check: ").strip()

    if not ip_pattern.match(user_ip):
        print("Invalid format. Please enter a valid IPv4 address (e.g., 192.168.1.2).")
        continue

    octets = user_ip.split('.')
    if all(0 <= int(o) <= 255 for o in octets):
        print(f"Valid IP entered: {user_ip}")
        break
    else:
        print("Each octet must be between 0 and 255. Try again.")

# count = 0                                     # finish 1
# for item in re_all_list:
#     if item[0] == 'vlan10':
#         count=count+1
#         print(f"{item[0]} IP: {item[1]}     status: {item[2]}")
# print(f"total of {count} vlan10")

# count = 0                                         # finish 2
# for item in re_all_list:
#     if item[2] == 'down':
#         count=count+1
#         print(f"{item[0]} IP: {item[1]}     status: {item[2]}    donest work")
# print(f"total of {count} down")


# print("vlan10 status up as below")              # finish 4
# count = 0
# for item in re_all_list:
#     if item[0] == 'vlan10' and item[2] == 'up':
#         count=count+1
#         print(f"{item[0]} IP: {item[1]}     status: {item[2]}")
# print(f"total of {count} vlan10 is up")

