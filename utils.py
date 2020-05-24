list = []
length = int(input('ENTER LENGTH OF LIST: '))

for i in range(length):
    data = int(input('ENTER NUMBERS: '))
    if data not in list:
        list.append(data)
print(list)
list.sort()

print(f'Max Num Among List is: {list[length-1]}')

