def math_avage(n):
    total = 0
    for i in range(1,n+1):
        total = total+i
    avg = total/n
    return avg

print(math_avage(100))
