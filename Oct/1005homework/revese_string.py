string = ['h','i']
def reverse(lst):
    result = []
    for i in lst:
        result.insert(0,i)
    print(result)
    return result

reverse(string)