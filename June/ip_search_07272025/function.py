import re
from ip_text import show, re_all_list

def checkstatus():
    user_ip = input("Enter an IP to check status: ").strip()     # not finish 5
    if user_ip in re_all_list:
        print(re_all_list[2])
    ipin = 0
    for i in re_all_list:
        if user_ip == i[1]:
            print(i[2])
            ipin=1
    if ipin == 0:
        print("No IP found")
# checkstatus()
def showallinfo():
    template = "VLAN: {:>8}   IP: {:>15}   Status: {:>8}"
    for i in re_all_list:
        formatted = template.format(i[0], i[1], i[2])
        print(formatted)
# showallinfo()

def checkip():
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    valid = 0
    ipin = 0
    while True:
        user_ip = input("Enter an IP to check: ").strip()
        if not ip_pattern.match(user_ip):
            print("Invalid format. Please enter a valid IPv4 address (e.g., 192.168.1.2).")
            continue
        octets = user_ip.split('.')
        if all(0 <= int(o) <= 255 for o in octets):
            valid = 1
            break
        else:
            print("Each octet must be between 0 and 255. Try again.")
            continue
    if valid == 1:
        for i in re_all_list:
            if user_ip == i[1]:
                print(f"VLAN : {i[0]} , IP : {i[1]} , status : {i[2]}")
                ipin = 1
                break
    if ipin==0:
        print("IP address not found.")
# checkip()

def showvlan(vlan):
    count = 0                                     # finish 1
    for item in re_all_list:
        if item[0] == vlan:
            count=count+1
            print(f"{item[0]} IP: {item[1]}     status: {item[2]}")
    print(f"total of {count} {vlan}")
# showvlan('vlan100')

def checkstatusdown():
    count = 0                                         # finish 2
    for item in re_all_list:
        if item[2] == 'down':
            count=count+1
            print(f"{item[0]} IP: {item[1]}     status: {item[2]}    donest work")
    print(f"total of {count} down")
# checkstatusdown()

def checkvlanup(vlan):
    print(f"{vlan} status up as below")    # finish 4
    count = 0
    for item in re_all_list:
        if item[0] == vlan and item[2] == 'up':
            count=count+1
            print(f"{item[0]} IP: {item[1]}     status: {item[2]}")
    print(f"total of {count} {vlan} is up")
checkvlanup('vlan10')