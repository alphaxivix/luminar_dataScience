string_i = "abel"
v_letter = ["a","b",'e','c']

if string_i[0] in v_letter:
    print("the string is included")

if all(c in v_letter for c in string_i[1:]):
    print("Valid")
else:
    print("Invalid")