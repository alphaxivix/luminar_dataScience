# # Enter your code here. Read input from STDIN. Print output to STDOUT
# mn = input().split()
# arr = input().split()
#
# A = input().split()
# B = input().split()
#
# happiness = sum((i in A) - (i in B) for i in arr)
#
# print(happiness)
# Read n and m
n, m = map(int, input().split())

# Read arr
arr = input().split()

# Read sets A and B
A = set(input().split())
B = set(input().split())

# Optimized happiness calculation
happiness = sum((i in A) - (i in B) for i in arr)

print(happiness)
