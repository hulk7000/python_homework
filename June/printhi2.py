def printhi(content,num):
    with open('test.txt','w') as f:
        for i in range(num):
            line = f'{i+1}. {content}\n'
            f.write(line)

def readfile(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = f.read()
        print(data)

import os

def list_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            readfile(file_path)
target_folder = 'F:\PyCharm 2025.1\PycharmProjects\project1\homework\April'
list_files(target_folder)
#1
# import os
# print("current list:",os.getcwd())
