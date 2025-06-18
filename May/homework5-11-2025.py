scores={
    "Tom": [100, 98, 79],
    "Alice": [85, 90, 88],
    "Bob": [75, 80, 72],
    "Lucy": [95, 92, 89],
    "John": [60, 70, 65]
}
def Printscore(namescore, return_list=[]):
    for k in namescore:
        name = k
        math = namescore.get(k)[0]
        english = namescore.get(k)[1]
        science = namescore.get(k)[2]
        # print(f"xingming:{k}")
        # print(f"math:    {namescore.get(k)[0]}")
        # print(f"enlish:  {namescore.get(k)[1]}")
        # print(f"science: {namescore.get(k)[2]}")
        return_list.append((name, math, english, science))
    return return_list

def avgscore(scorelist):
    for k in scorelist:
        name = k[0]
        scores = k[1:]
        average = sum(scores) / len(scores)
        print(f"name: {name} \naverage: {average:.2f}\n")


print(Printscore(scores))








