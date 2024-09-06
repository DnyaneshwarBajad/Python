def dectobin(num):
    rem, ans = 0, 0
    mul = 1
    while num > 0:
        rem = num % 2
        num = num // 2
        ans = ans + mul * rem
        mul = mul * 10
    return ans

def bintodect(num):
    ans = 0
    rem = 0
    mul = 1
    while num > 0:
        rem = num % 10
        num = num // 10
        ans = ans + rem * mul
        mul = 2 * mul
    return ans

def subt(a, b):
    return dectobin(a - b)

if __name__ == "__main__":
    print(dectobin(13))
    print(bintodect(1101))
    print(subt(18, 11))
