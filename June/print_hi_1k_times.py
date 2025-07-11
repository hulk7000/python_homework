def readfile(filename):
    with open(filename,'r',encoding='utf') as f:
        data = f.readline()
        print(data)

import os

def list_files():
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            readfile(filename)
list_files()
#19
# import os
# print("current list:",os.getcwd())     #search your current folder