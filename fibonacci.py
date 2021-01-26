import time

def fibonacci_r(n):
    if n == 0 or n == 1:
        return 1
    return (fibonacci_r(n-1)+fibonacci_r(n-2))

# With memoization
def fibonacci_m(n, memo={}):
    if n == 0 or n == 1:
        return 1
    elif n in memo:
        return memo[n]
    result = fibonacci_m(n-1, memo)+fibonacci_m(n-2, memo)
    memo[n] = result
    return result


if __name__ == '__main__':
    rs  = time.time()
    r = fibonacci_r(30)
    re  = time.time()
    ms  = time.time()
    m = fibonacci_m(30)
    me  = time.time()
    print(r, 'in', re-rs)
    print(m, 'in', me-ms)