lists = [-3,9,8,-700,4,60,1]
dic1= {"k1":100,"k2":15,"k3":31,"k4":16,"k5":16,"k6":17,"k7":18,"k8":91,"k9":51,}
def findbiggest(lists):
    maxnum = lists[0]
    for i in lists:
        if i > maxnum:
            maxnum = i
    return maxnum

def findsmallest(lists):
    minnum = lists[0]
    for i in lists:
        if i < minnum:
            minnum = i
    return minnum

def dicfindbiggest(dic1):
    max_key = None
    max_val = float('-inf')
    for k, v in dic1.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key

def dicfindsmallest(dic1):
    min_key = None
    min_val = float('inf')
    for k, v in dic1.items():
        if v < min_val:
            min_val = v
            min_key = k
    return min_key

print(dicfindsmallest(dic1))

