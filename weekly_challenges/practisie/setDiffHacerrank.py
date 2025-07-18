# Students of District College have a subscription to English and French newspapers.
# Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper,
# and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
# and one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to only English newspapers.
#
# Input Format
#
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
#
# Output Format
#
# Output the total number of students who are subscribed to the English newspaper only.



# Enter your code here. Read input from STDIN. Print output to STDOUT
english = set()
french = set()

enum = int(input())
e_vals = input().strip()

fnum = int(input())
f_vals = input().strip()

e_lst = e_vals.split()
f_lst = f_vals.split()

for i in e_lst:
    english.add(i)

for i in f_lst:
    french.add(i)

print(len(english.difference(french)))

