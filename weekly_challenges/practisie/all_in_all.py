valid_s = ['a','b','c','d']
str1 = 'abcd'

if all(c in valid_s for c in str1):
    print("Valid string!!")