def isPowerOfTwo(n: int) -> bool:
    for i in range(0,32):
        result = 2 ** i
        print(f'2**{i} result = {result}')
        if result == n:
            return True
    return False

print(isPowerOfTwo(1024))