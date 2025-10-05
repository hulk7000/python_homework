def ins_dic(dic,val):
    from collections import OrderedDict
    od = OrderedDict()
    index = len(dic)+1
    od[index] = val
    dic.update(dict(od))
    return dic

# lst1=["a","b","c","d","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple",]
dic = {}

for i in range(10):
    newdic = ins_dic(dic, "apple")
    dic.update(newdic)
print(dic)



# from collections import deque
#
# dq = deque([1,2,3])
# dq.append(4)
# dq.appendleft(0)
# dq.pop()
# dq.popleft()
# print(dq)