null = None
root = [1,'null',2,3,4,5,6]
root1 =[1,2,3,4,5,null,8,null,null,6,7,9]
def plst(lst):
    for i in root1:
        if i == null:
            continue
        print(i)
plst(root1)
