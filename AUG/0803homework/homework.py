#1. 找到研发部韩梅梅 status为“已完成” 的项目，并打印name
#2.找到"sku": "P001" 的价格和数量，并打印出来
#3. 找到 "冰封骑士"的level，他的盔甲防御总和多少
#4. 找到两个学生的分数总和，打印出，name 和分数总和
#5 分别打印，库存的商品item 和数量
from dic import *

def q1():
    a = employee_data.get('employees')[0].get('projects')[1].get('name')
    print(a)

def q2():
    b = erp_data.get('orders')[0].get('products')[0]
    print(b)
    for k,v in b.items():
        print(k,v)

def q3():
    l = game_data.get('level')
    # h = game_data.get('equipment').get('armor').get('helmet').get('def')
    # c = game_data.get('equipment').get('armor').get('chest').get('def')
    armor=game_data.get('equipment').get('armor')
    armor_total=0
    for k,v in armor.items():
        print(f"加之前的总和   {armor_total}")
        print(f"当前值   {v.get('def')}")
        armor_total=armor_total+v.get('def')
        print(f"加之后的总和   {armor_total}")

    # print(f'level : {l}, total armor : {h+c}')

def q4():
    # s = school_data.get('students')[0].get('scores')
    # c = school_data.get('students')[1].get('scores')
    # print(f'林佳 total score is {s.get('math')+s.get('english')+s.get('physics')}\n'
    #       f'陈涛 total score is {c.get('math')+c.get('english')+c.get('physics')}')
    students=school_data.get('students')
    for student in students:
        name=student.get('name')
        scores=student.get('scores')
        scores_total=0
        for k,v in scores.items():
            scores_total=scores_total+v
        print(f"name: {name} , scores: {scores_total}")




def q5():
    a = logistics_data.get('cargo')[0].get('item')
    b = logistics_data.get('cargo')[1].get('item')
    c = logistics_data.get('cargo')[0].get('qty')
    d = logistics_data.get('cargo')[1].get('qty')
    print(f'{a} : {c} \n{b} : {d}')

q4()