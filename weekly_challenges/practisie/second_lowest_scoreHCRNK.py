# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
    
if __name__ == '__main__':
    lst = []
    dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])

    for i in range(len(lst)):
        if lst[i][1] not in dict:
            dict[lst[i][1]] = [lst[i][0]]
        elif lst[i][1] in dict:
            dict[lst[i][1]] += [lst[i][0]]
    di_ky = dict.keys()
    min_score = min(di_ky)

    del dict[min_score]

    min_score1 = min(di_ky)
    sec_lowest = dict[min_score1]
    sec_lowest.sort()

    for i in sec_lowest:
        print(i, end='\n')


