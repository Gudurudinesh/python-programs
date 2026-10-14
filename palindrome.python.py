def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

text = input("Enter a word: ")

if palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")