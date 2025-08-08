from lib.dic import employee_data, erp_data, game_data, school_data, logistics_data

def q1():
    a = employee_data.get('employees')[0].get('projects')[1].get('name')
    print(a)
#3

def q2():
    b = erp_data.get('orders')[0].get('products')[0]
    print(b)
    for k,v in b.items():
        print(k,v)
#3

def q3():
    l = game_data.get('level')
    armor = game_data.get('equipment').get('armor')
    armor_total = 0
    for k,v in armor.items():
        print(f"加之前的总和   {armor_total}")
        print(f"当前值   {v.get('def')}")
        armor_total=armor_total+v.get('def')
        print(f"加之后的总和   {armor_total}")
#3

def q4():
    students=school_data.get('students')
    for student in students:
        name=student.get('name')
        scores=student.get('scores')
        scores_total=0
        for k,v in scores.items():
            scores_total=scores_total+v
        print(f"name: {name} , scores: {scores_total}")
#3

def q5():
    a = logistics_data.get('cargo')[0]
    for a in logistics_data.get('cargo'):
        print(f'item: {a.get('item')} qty: {a.get('qty')}')

q5()