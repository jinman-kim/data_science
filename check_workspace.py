import os
# print(os.getcwd())

dir_path = 'C:/Users/진만킴/Desktop/ManPy/data_science/encore_labor'
male_income, female_income = 0,0

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if int(file.split('_')[2][0]) % 2 == 1: #남자
            f = open(os.path.join(root,file),'r')
            line = f.readline()
            male_income += int(line)
        if int(file.split('_')[2][0]) % 2 == 0: #여자
            f = open(os.path.join(root,file),'r')
            line = f.readline()
            female_income += int(line)

print(f'남성 월급:{male_income}')
print(f'여성 월급:{female_income}')