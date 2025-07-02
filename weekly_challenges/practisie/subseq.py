def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    t = []
    for i in range(0, n, k):
        if i < n:
            t += [string[i:i + k]]

    for i in t:
        sub = ''
        for j in i:
            if j not in sub:
                sub += j
        print(sub)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)