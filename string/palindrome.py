s1 = input()

s2 = s1[::-1]

if s1 == s2:
    print("The word \"%s\" is palindrome"%s1)
else:
    print("The word \"%s\" is not palindrome"%s1)
