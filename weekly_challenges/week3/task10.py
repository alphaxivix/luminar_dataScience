#ipv4 addresses
print("Enter the four octets of the ipv4 address :")
ipv4 = [int(input(f"{i+1} ==> ")) for i in range(0,4)]
print(*ipv4)
print("---------------NEXT 4 IPV4 ADDRESSES----------------")

for i in range(0,5):
    if ipv4[3] < 255:
        ipv4[3] += 1
    elif ipv4[3] == 255:
        if ipv4[2] < 255:
            ipv4[2] += 1
            ipv4[3] = 0
        elif ipv4[2] == 255:
            if ipv4[1] < 255:
                ipv4[1] += 1
                ipv4[2], ipv4[3] = 0,0
            elif ipv4[1] == 255:
                if ipv4[0] < 255:
                    ipv4[0] += 1
                    ipv4[1], ipv4[2], ipv4[3] = 0,0,0
                elif ipv4[0] == 255:
                    ipv4 = [0, 0, 0, 0]
    print(*ipv4)
