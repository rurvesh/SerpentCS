lst = [1, 2, 3, 4, 5, 6, 7]
lst1 = ['Urvesh', "Parth", "Nirav", "Haarish"]

print(lst[2])       #access item

lst2 =[1, 2, "Urvesh", 4.4, "Nirav"]        #if you want to use multiple data type in list

lst3 = lst + lst1       #update two list
print(lst3)
print(lst2[2])          #if you want to access elemnt of list
print(lst2[-3])         #access with last elemnt of list


# stringg = input("Enter elements: ")
# lstt = stringg.split()  
# print('The list is:', lstt)

# methods

lst1.append("Roshan")
lst.remove(3)           #if you want to remove specific elemnt
print(lst)
print(lst1)
print(lst1.pop())       #access last element
print(lst.count(3))     #if you want to count elemnt
lstlst = lst.copy()
print(lstlst)           #if you want to copy list
print(lst.index(5))     #check index of elemnt
lst.insert(3, 10)
print(lst)
lst.clear()
print(lst)