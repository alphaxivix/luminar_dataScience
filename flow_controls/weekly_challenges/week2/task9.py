#city and monuments

print("Cities :\t Delhi \t Agra \t Jaipur")
print("View Monuments belonging to each cities ===>")
city = input("Enter the city name :")

if city == 'Delhi' or city == 'DELHI' or city == 'delhi':
    print("Monument : Red fort")
elif city == 'Agra' or city == 'AGRA' or city == 'agra':
    print("Monument : Taj Mahal")
elif city == 'Jaipur' or city == 'JAIPUR' or city == 'jaipur':
    print("Monument : Jal Mahal")
else:
    print("Data available for the displayed cities only or check the spelling")
