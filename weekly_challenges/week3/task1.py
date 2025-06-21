#print numbers divisible by 3 and 5 from 1 to 20 using a for loop
div_3 = []
div_5 = []
for i in range(1,21):
    if i % 3 == 0:
        div_3.append(i)
    elif i % 5 == 0:
        div_5.append(i)
print(f"Numbers that are divisible by 3 is :{div_3}")
print(f"Numbers that are divisible by 5 is :{div_5}")
