#make more lists....
rare_numbers = [1, 5, 8, 4, 12, 52]
friends = ["Someone", "mum", "Friend", "Youtube", "random"]

#Add Another element to the 'Friends' list made above
friends.extend(rare_numbers)



#Add a string to your list.
friends.append("You", "Someone")



#Add something in between the The number
friend.insert(2, "Step-Mum")


#removes a string from the list
friend.remove("Someone")


#Clears the whole list
friend.clear()


#Gets rid of the last String of the element in the list
friends.pop()


#Tells you if Someone is in the list.
print (friends.index("Friend"))


#Shows how many times this String is in the List.
print (friends.count("Friend"))


#put the list in alphabetical Order.
friends.sort()


#Sort again....
rare_numbers.sort()
print (rare_numbers)


#Reverse the order From z to a
rare_numbers.reverse()
print (rare_numbers)


#COpys a list to another variabled list
friends2 = friends.copy


#printing it would be the same as 'friends' Variable
print (friends2)


#Shows the list
print (friends)