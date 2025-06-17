#triangles
print("Enter the three angles of the triangle:")
angle1 = int(input("Enter the first angle:"))
angle2 = int(input("Enter the second angle:"))
angle3 = int(input("Enter the third angle:"))
total_angle = angle1 + angle2 + angle3
if total_angle > 180:
    print("This is not an triangle!!")

if angle1 == angle2 == angle3:
    print("This is a Equilateral Triangle")
else:
    if angle1 == angle2 and angle1 != angle3 or angle1 == angle3 and angle1 != angle2:
        print("This is a Isosceles Triangle")
    else:
        print("This is a Scalene Triangle")