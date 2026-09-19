#write a funtion to check whether a string is palindrome or not
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

print(is_palindrome("racecar"))