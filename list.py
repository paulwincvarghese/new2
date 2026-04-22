list = [1,2,3,4,5]
print(list)
print(list[0]) # This line prints the first element of the list
print(list[1]) # This line prints the second element of the list
print(list[2]) # This line prints the third element of the list 
thislist = ["apple", "banana", "cherry", "cherry"]
print(thislist)
print(thislist[1]) # This line prints the second element of the list
print(thislist[-1]) # This line prints the last element of the list
print(thislist[0:2]) # This line prints the first two elements of the list
thislist[3] = "blackcurrant" # This line changes the second element of the list to "blackcurrant"
print(thislist)
thislist.append("orange") # This line adds "orange" to the end of the list
print(thislist)

thislist.remove("banana") # This line removes "banana" from the list
print(thislist)

thislist.pop(1) # This line removes the second element of the list
print(thislist)