import os

# os.mkdir('test1')
# os.chdir('test1')
# qytang1 = open('qytang1', 'w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
# qytang2 = open('qytang2', 'w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
# qytang3 = open('qytang3', 'w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
# os.mkdir('qytang4')
# os.mkdir('qytang5')

keyword = 'qytang'
target_dir = 'test1'
matched_files = []

for name in os.listdir(target_dir):
    file_path = os.path.join(target_dir, name)
    if os.path.isfile(name):
        with open(name, 'r',encoding='utf-8') as f:
            content = f.read()
            if keyword in content:
                matched_files.append(name)
print(matched_files,'file find qytang')