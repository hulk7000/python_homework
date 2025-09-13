nested_list = [1,[2,3,[4,5]],6]               #[1, 2, 3, 4, 5, 6]

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
# print(flatten(nested_list))

fruit = ['apple', 'banana']
fruit.extend(['orange', 'grape'])
print(f'extend : {fruit}')

fruits = ['apple', 'banana']
fruits.append(['grape', 'melon'])
print(f'append : {fruits}')
