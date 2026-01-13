import time

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)

# print(factorial(5))

def factorial_expression(n):
    if n == 1:
        return "1"
    return f"{n} x " + factorial_expression(n - 1)
#
# print(factorial_expression(3))

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

# print(gcd(15,20))

def climb_stairs(total_stairs, step_size, current=0):
    # Base case: reached or passed the top
    if current >= total_stairs:
        print(f"Finished climbing! Total stairs climbed: {current}")
        return
    # Recursive step
    print(f"Climbing {step_size} stairs... now at stair {current + step_size}")
    time.sleep(1)
    climb_stairs(total_stairs, step_size, current + step_size)

total_stairs = 9
step_size = 1

climb_stairs(total_stairs, step_size)