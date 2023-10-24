def isleapyear(year):
    divisibleByFour = year % 4
    divisibleBy100 = year % 100
    divisibleBy400 = year % 400
    if (divisibleByFour == 0) and (divisibleBy100 != 0):
        return True
    elif (divisibleBy400 == 0):
        return True
    else:
        return False