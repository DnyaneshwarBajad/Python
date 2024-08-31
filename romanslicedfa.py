def ends_with_a(text):
    return "Accepted" if q0(text) else "Rejected"


def q0(text):
    if (text[0]) == 'b':
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    elif (text[0]) == 'a':
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    else:
        return False


def q1(text):
    if (text[0]) == 'a':
        if len(text) == 1:
            return True
        else:
            return q1(text[1:])
    elif (text[0]) == 'b':
        if len(text) == 1:
            return False
        else:
            return q0(text[1:])
    else:
        return False


def base(text, text_base, output_base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    if not (2 <= text_base <= 36) and (2 <= output_base <= 36):
        print('Base must be between 2 and 36')

    dec = int(text, text_base)

    while dec > 0:
        rem = dec % output_base
        res = digits[rem] + res
        dec //= output_base

    return res


def slice_string(object, start, end, step):
    text = ""
    for i in range(start, end, step):
        text += object[i]
    return text


def con1(object, slicing_parameter):
    step = 1
    fist = 0
    last = len(object)
    return slice_string(object, fist, last, step)


def con2(object, slicing_parameter):
    step = slicing_parameter[2]
    first = slicing_parameter[0]
    last = slicing_parameter[1]
    return slice_string(object, first, last, step)

def intToRoman(num: int):
    Result = ""
    Values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    Symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    Number = len(Values) - 1
    while num:
        quotient = num // Values[Number]
        num %= Values[Number]
        while quotient:
            Result += Symbols[Number]
            quotient -= 1
        Number -= 1
    return Result


print(intToRoman(56))
print(con2("programming", [len("programming") - 1, -1, -1]))
print(base('1100', 2, 16))
print(ends_with_a("babaabbaba"))
