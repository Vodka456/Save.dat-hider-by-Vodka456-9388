phrase = "vSync's\nCourse"


#.upper Converts it to be Upppercase then .isupper sees if its uppercase or not (true or false)
print (phrase.upper().isupper())


#Adding something after the variable
print (phrase + "is cool.")


#len shows how many words are in the variable 'phrase'
print (len(phrase))

#[]inds out First Letter of the string 'Phrase'
print (phrase[0])
print ("this printed out the first character of the Variable")

print (phrase[1])
print ("this printed out the second character of the variable")

print (phrase[3])
print ("this printed out the third character of the variable")



#.index Shows where the Letter is from the Variable Associated.
print (phrase.index("S"))
print ("this would find the letter 'S' from the Variable written and give us back 1")


#.replace; replaces the String wanted to anything you want.
print (phrase.replace("vSync", "Your"))
print (phrase.replace("Course", "Academy"))