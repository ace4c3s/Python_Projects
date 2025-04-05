
def romanToInteger(string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(string) - 1):
        if roman_dict[string[i]] < roman_dict[string[i+1]]:
            total -= roman_dict[string[i]]
        else:
            total += roman_dict[string[i]]
    return total + roman_dict[string[-1]]


print(romanToInteger("CM"))


