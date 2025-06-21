#permutatuions

org = []
print("Enter three numbers for creating permutations:")
for i in range(0,3):
    ch = int(input(f"Value {i+1} ==> "))
    org.append(ch)

permu = [[i,j,k] for i in org for j in org for k in org if i != j and i != k and j != k]
print(permu)

# used List comprehension method for simplifying the process