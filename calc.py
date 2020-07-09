def calcTwoNumbers(num1, num2, op):
    result = 0
    if op == 'sum':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    return result
