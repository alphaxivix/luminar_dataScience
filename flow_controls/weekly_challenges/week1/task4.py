#generate identifiers by reading its length and n values from the user
def is_valid_first(c):
    return c.isalpha() or c == "_"
def is_valid_body(c):
    return c.isalpha() or c.isdigit() or c == "_"
def generate_id(chars,current,n,result):
    if len(current) == n:
        result.append(''.join(current))
        return
    for ch in chars:
        if len(current) == 0:
            if is_valid_first(ch):
                generate_id(chars, current + [ch], n,result)
        else:
            if is_valid_body(ch):
                generate_id(chars, current + [ch], n,result)
#------MAIN PROGRAM--------
n = int(input("Enter the length of each combinations:"))
chars = []
print("Enter",n,"Characters:",end='')
for i in range(n):
    ch = input().strip()
    chars.append(ch)

print("Valid Identifiers list")
result = []
generate_id(chars,[],n,result)

for c in result:
    print(c)

