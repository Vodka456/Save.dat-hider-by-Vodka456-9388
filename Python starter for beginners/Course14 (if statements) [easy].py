
is_male = False
is_tall= False

#And, they have to be both true statements
if is_male and is_tall:
    print ("You are an Male Or tool")
else:
    print ("You are neither an Male or tall")



is_gay = True
is_lesbian = False
#It has to be either one true or both false which would say Lesbian or gay
if is_lesbian or is_gay:
    print ("you are gay or lesbian")
elif is_male and not (is_tall):
    print ("you are a short male")
elif not (is_male) and is_tall:
    print ("you are not a male but are tall")
else:
    print ("You are neither lesbian or Gay")
