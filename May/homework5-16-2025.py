scores={
    "Tom": [100, 98, 79],
    "Alice": [85, 90, 88],
    "Bob": [75, 80, 72],
    "Lucy": [95, 92, 89],
    "John": [60, 70, 65]
}

def Printscore(namescores, return_list=[]):
    for k in namescores:
        name = k
        math = namescores.get(k)[0]
        english =namescores.get(k)[1]
        science = namescores.get(k)[2]
        return [name, math, english, science]
    return return_list

def avgscore(namescores, return_list=[]):
    for k in namescores:
        name = k
        scores = namescores.get(k)
        avgerage = sum(scores) / len(scores)
        print(f'name: {name} \navgrtage: {avgerage:.2f}\n')


print(Printscore(scores))
()