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

def is_valid_vlan():
    pattern = r'^vlan(?:[1-9]|[1-9]\d{1,2}|[1-3]\d{3}|40[0-8][0-9]|409[0-6])$'
    while True:
        vlan = input('Enter an vlan to check: ').strip()
        if re.match(pattern, vlan):
            break
    return vlan
# print(is_valid_vlan())

def is_valid_ip():
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    while True:
        user_ip = input("Enter an ip address: ").strip()
        if not ip_pattern.match(user_ip):
            print('Invalid format. Please enter a valid IPv4 address (e.g., 192.168.1.2).')
            continue
        octets = user_ip.split('.')
        if all(0 <= int(o) <= 255 for o in octets):
            valid = 1
            break
        else:
            print('Each octet must be between 0 and 255. Try again.')
            continue
    return user_ip
# print(is_valid_ip())

def checkstatus():
    user_ip = is_valid_ip()
    if user_ip in re_all_list:
        print(re_all_list)
    ipin = 0
    for i in re_all_list:
        if user_ip == i[1]:
            print(i[2])
            ipin = 1
    if ipin == 0:
        print('NO IP found')
# checkstatus()

def showallinfo():
    template = 'VLAN: {:>8} IP: {:>15} Status: {:>8}'
    for i in re_all_list:
        formatted = template.format(i[0], i[1], i[2])
        print(formatted)
# showallinfo()

def checkip():
    ipin = 0
    user_ip = is_valid_ip()
    for i in re_all_list:
        if user_ip == i[1]:
            print(f'VLAN {i[0]} IP {i[1]} Status: {i[2]}')
            ipin = 1
            break
    if ipin == 0:
        print('NO IP found')
# checkip()

def showvlan():
    vlan = is_valid_vlan()
    count = 0
    for item in re_all_list:
        if item[0] == vlan:
            count += 1
            print(f'VLAN {item[0]} IP {item[1]} Status: {item[2]}')
    print(f'total of {count} {vlan}')
# showvlan()

def checkstatusdown():
    ip = is_valid_ip()
    count = 0
    for item in re_all_list:
        if item[2] == 'down':
            count += 1
            print(f'VLAN {item[0]} IP {item[1]} Status: {item[2]}')
    print(f'total of {count} {ip}')
# checkstatusdown()

def checkvlanup():
    vlan = is_valid_vlan()
    count = 0
    for item in re_all_list:
        if item[0] == vlan and item[2] == 'up':
            count += 1
            print(f'VLAN {item[0]} IP {item[1]} Status: {item[2]}')
    print(f'total of {count} {vlan} is up')
# checkstatus()