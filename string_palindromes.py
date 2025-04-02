def isPalindrome(string):
    if string ==" ":
        return False

    reversed_string = string[::-1]

    if reversed_string == string:
        return True
    else:
        return False
    