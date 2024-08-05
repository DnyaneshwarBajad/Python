def modulus(dividend, divisor):

    quotient = dividend // divisor  
    reminder = dividend - (quotient * divisor)
    return reminder
    
m = modulus(5,3)
print(m)
