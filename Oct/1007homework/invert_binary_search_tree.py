root = [4,2,7,1,3,6,9]

def ibst(lst):
    result = []
    for i in range(0,3):
        j = 2**i
        row = lst[(j-1):(j-1+j)]
        row.reverse()
        result.extend(row)
    print(result)
ibst(root)