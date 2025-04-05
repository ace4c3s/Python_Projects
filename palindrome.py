# This program checks if a number is a palindrome

def isPalindrome(num):
    if num < 0:
        return False
    
    num_duplicate = num
    reversed = 0

    while num_duplicate > 0:
        last_digit = num_duplicate%10
        reversed = reversed * 10 + last_digit 
        num_duplicate //= 10
    
    if num == reversed:
        return True
    else:
        return False
    
print(isPalindrome(104))