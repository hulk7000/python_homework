def math_avage(n):
    total = 0
    for i in range(1,n+1):
        total = total+i
    avg = total/n
    return avg

# print(math_avage(100))

def math_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

# print(math_even(100))

def math(n):
    count = 0
    for i in range(1,n+1):
        if i%2 == 0 and i%3 == 0:
            count+=1
    return count

print(math(100))