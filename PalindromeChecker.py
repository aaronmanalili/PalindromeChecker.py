def checkForPalindrome(string):
    if (string == string[::1]):
        print('This word is a Palindrome.')
    
    else:
        print("This is NOT a Palindrome.")
        
string = input('Enter a String: ')
print(checkForPalindrome(string)) 
