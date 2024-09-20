valid_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def decimal_subtraction(num1, num2):
    if num1.startswith("-") and num2.startswith("-"):
        return subtraction(num2[1:], num1[1:])

    elif num1.startswith("-"):
        return "-" + str(decimal_addition(num1[1:], num2))

    elif num2.startswith("-"):
        return decimal_addition(num1, num2[1:])
    else :
        return subtraction(num1,num2)


def subtraction(num1, num2):
    truth_value = False
    if str_to_int(num2) > str_to_int(num1):
        num1, num2 = num2, num1
        truth_value = True
    
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    if len_num1 > len_num2:
        num2 = "0" * (len_num1 - len_num2) + num2
    elif len_num2 > len_num1:
        num1 = "0" * (len_num2 - len_num1) + num1
    borrow = 0
    result = ""
    for i in range (0,len(num1)) :
        a = str_to_int(num1[-1])
        b = str_to_int(num2[-1])
        diff = a - b - borrow
        if diff < 0 :
            diff += 10
            borrow = 1
        else :
            borrow = 0
        result = str(diff) + result
        num1 = num1[:-1]
        num2 = num2[:-1]

    return "-" + result if truth_value else result



def decimal_addition(num1, num2):
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    if len_num1 > len_num2:
        num2 = "0" * (len_num1 - len_num2) + num2
    elif len_num2 > len_num1:
        num1 = "0" * (len_num2 - len_num1) + num1
    
    carry = 0
    result = ""
    
    for i in range(0, len(num2)):
        sum = str_to_int(num1[-1]) + str_to_int(num2[-1]) + carry
        carry = 0
        
        if sum > 9:
            carry = 1
            sum -= 10
        
        result = str(sum) + result
        num1 = num1[:-1]
        num2 = num2[:-1]
    
    if carry == 1:
        result = "1" + result
    
    return str_to_int(result)


def str_to_int(text):
    if len(text) == 1:
        return valid_num.index(text)
    else:
        return str_to_int(text[:-1]) * 10 + valid_num.index(text[-1])


print(decimal_subtraction("-409", "1"))
