import timeit
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(x*y)

def karatsuba(x, y):
    n_x = len(str(x))
    n_y = len(str(y))
    n = max(n_x, n_y)
    m = n//2

    a, b = divmod(x, 10 ** m)
    c, d = divmod(y, 10 ** m)
    if x < 10 or y < 10:
        return x * y
    else: 
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        sum = karatsuba(a+b, c+d)
        ad_bc = sum - ac- bd
        result = ac * 10**(2*m) + ad_bc * 10**m + bd
    return result

print(karatsuba(x, y))


t_native = timeit.timeit(lambda: x * y, number=10)
t_karat  = timeit.timeit(lambda: karatsuba(x, y), number=10000)

print(f"native:    {t_native:.4f} s for 10000 runs  ({t_native/10000*1e6:.2f} µs each)")
print(f"karatsuba: {t_karat:.4f}  s for 10000 runs  ({t_karat /10000*1e6:.2f} µs each)")