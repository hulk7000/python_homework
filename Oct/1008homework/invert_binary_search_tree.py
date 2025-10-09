root = [4,2,7,1,3,6,9]

def ibst(lst):
    result = []
    for i in range(len(lst)):
        j = 2**i
        # print(i,j)
        row = lst[(j-1):(j-1+j)]
        row.reverse()
        result.extend(row)
    print(result)
ibst(root)