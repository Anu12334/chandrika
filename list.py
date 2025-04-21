a = ["apple","banana","apple","mango"]
print(a)

a.append("orange")  # Adds an element to the end of the list
print("after append:",a)

a.extend(["mosambi","grepes"]) #Adds elements from another list
print("after extend:",a)

a.insert(2,"kiwi")#Inserts an element at a specified position
print("after insert:",a)

a.remove("banana")
print("after remove:",a)

a.pop()
print("after pop:",a)# Removes the last item

a.index("mango")
print("after index:",a)
print(len(a))

a.count("apple")
print("after count:",a)

a.sort()#Sorts the list in ascending order

print("after sort:",a)

a.reverse()#Reverses the list order

print("after reversing:",a)

a.copy() #Returns a shallow copy of the list
print("after copy:",a)

a.clear()
print("after clear:",a)

