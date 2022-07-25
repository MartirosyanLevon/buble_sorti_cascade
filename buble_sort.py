data = [6,8,2,5,9,10]

def Buble_sort(data):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(data)-1):
            if data[i] > data[i + 1]:
                data[i],data[i + 1] = data[i + 1],data[i]
                swaped = True
    print(data)

Buble_sort(data)
