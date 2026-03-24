def romantoInt(romanInput):

    roman = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

    resultInteger = 0

    for i in range(0, len(romanInput)):
        if i > 0 and roman[romanInput[i]] > roman[romanInput[i - 1]]:
            resultInteger += roman[romanInput[i]] - 2 * roman[romanInput[i - 1]]
        else:
            resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]

roman = input("Enter a Roman numeral: ")

print("Integer equivalant : ",romantoInt(roman))