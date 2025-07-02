f = open("C:/Users/alpha/Downloads/temper.unknown",'r')
dis = {}

for i in f:
    data = i.rstrip("/n").split(',')
    district = data[0]
    temp = data[1]
    if district not in dis:
        dis[district] = temp
    else :
        old = dis[district]
        if temp > old:
            dis[district] = temp
for k,v in dis.items():
    print(k,v.rstrip('\n'))