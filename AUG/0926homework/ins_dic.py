def ins_dic(dic, val):
    from collections import OrderedDict
    od = OrderedDict()
    index = len(dic)+1
    od[index] = val
    dic.update(dict(od))
    return dic

dic = {}
for i in range(10):
    newdic = ins_dic(dic, 'apple')
    dic.update(newdic)
print(dic)