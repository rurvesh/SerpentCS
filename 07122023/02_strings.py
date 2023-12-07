strr = 'strings are immutable in python'        #they also use in double quotation

name = 'Urvesh'
surname = 'Rathod'

print(name[1])          #if you access a character in string so they start with 0
print(name[0:3])        #if you want to access some character in string 
print(name[::-1])       #if you want to revers your string
print("".join(reversed(name)))
print(name[-1])         #if you want to last character in string

fullName = name + " " + surname     #concate two strings
print(fullName)


lst1 = list(fullName)           #if you want to change character in string 
lst1[2] = 'm'
string2 = ''.join(lst1) 
print(string2) 

name = 'Rahul Rathod'      #if you want to update string

# methods

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace('h', 'k'))
print(name.count('R'))
print(name.split(' '))
print(name.swapcase())
print(name.find('h'))