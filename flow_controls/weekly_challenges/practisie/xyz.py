def is_valid_start(c):
    return c.isalpha() or c == '_'


def is_valid_char(c):
    return c.isalpha() or c.isdigit() or c == '_'


def generate_identifiers(chars, n, current, result):
    if len(current) == n:
        result.append(''.join(current))
        return

    for ch in chars:
        if len(current) == 0:
            if is_valid_start(ch):
                generate_identifiers(chars, n, current + [ch], result)
        else:
            if is_valid_char(ch):
                generate_identifiers(chars, n, current + [ch], result)


# --- Main program ---
n = int(input("Enter the desired identifier length: "))
chars = []

print(f"Enter characters to use (you can reuse characters):")
for _ in range(n):
    ch = input().strip()
    chars.append(ch)

result = []
generate_identifiers(chars, n, [], result)

print("\nValid Identifiers:")
for identifier in result:
    print(identifier)
