num = int(input("How many number do you have : "))
for i in range(1,num): 
    if i==5:
        continue            #if you want to skip some value 
    if i==7:
        break               #if you want to break the loop
    print(i)

names = ['Urvesh', 'Roshansing', 'Shiv', 'Sagar']
surnm = ['Rathod', 'Zala', 'Panday', 'Makvana']
for name,surn in zip(names,surnm):
    print(f'My is {name} {surn}')

for name in names:
    if name == "Shiv":
        print(name.upper())
    if name == "Sagar":
        print(name.lower())
    if name == 'Roshansing':
        print(name.count('s'))
    for n in name:
        if n == "Urvesh":
            print(n)