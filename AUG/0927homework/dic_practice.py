students = [
    {"name": "Alice", "score":  [80,90,70]},
    {'name': 'Bob', 'score':  [85,75,95]},
]

def average_scores():
    name = input('please input name:')
    for student in students:
        if student['name'] == name:
            scores = student.get('score')
            avg = sum(scores) / len(scores)
            print(f'{name}: {avg}')
            return
    print('no name found')

# average_scores()

products = [
    {'name': 'candy', 'price': 2},
    {'name': 'toy', 'price': 5},
]

def find_price():
    name = input('please input item name:')
    for product in products:
        if product['name'] == name:
            print('item found')
            return
    print('item not found')

find_price()