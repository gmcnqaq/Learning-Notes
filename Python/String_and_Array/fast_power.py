def fast_pow(base, power):
    res = 1
    if power < 0:
        base = 1 / base
        power = -power
    while power:
        if power & 1:
            res *= base
        power >>= 1
        base *= base
    return res


if __name__ == '__main__':
    base = 4
    power = -2
    print(fast_pow(base, power))
    print(pow(base, power))
