thislist =["apple", "banana", "cherry", "cherry"]
print(thislist)
print(*thislist[1]) # This line prints the second element of the list
print(*thislist[-1]) # This line prints the last element of the list

thislist.append("grapes") # This line adds "grapes" to the end of the list
print(*thislist)
thislist.remove("banana") # This line removes "banana" from the list
print(*thislist)
thislist.pop(1) # This line removes the second element of the list
print(*thislist)
