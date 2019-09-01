

print("                                                    ")
COMPASS_DIRECTION = input("Enter a Compass direction: ") #0
print("                                                    ")
CITY = input("Enter a city: ") #1
print("                                                    ")
PLACE = input("Enter a place: ") #2
print("                                                    ")
VERB = input("Enter a verb: ") #3
print("                                                    ")
VERB2 = input("Enter a diffrent verb: ") #4
print("                                                    ")
PLACE2 = input("Enter a diffrent place: ") #5
print("                                                    ")
ACTIVITY = input("Enter your favorite activity: ") #6
print("                                                    ")
NOUN = input("Enter a noun: ") #7
print("                                                    ")
NOUN2 = input("Enter a diffrent noun: ") #8
print("                                                    ")
EMOTION = input("Enter an emotion: ") #9
print("                                                    ")
FAMILY = input("Enter a family member: ") #10
print("                                                    ")
FAMILY2 = input("Enter a diffrent family member: ") #11
print("                                                    ")
CITY2 = input("Enter a diffrent city: ") #12

Veriable_ls = [COMPASS_DIRECTION, CITY, PLACE, VERB, VERB2, PLACE2, ACTIVITY, NOUN, NOUN2, EMOTION, FAMILY, FAMILY2, CITY2]



def function():
    print("                                                    ")
    print("====================================================")
    print("The Fresh Prince of", Veriable_ls[12])
    print("====================================================")
    #print("In", Veriable_ls[0], Veriable_ls[1], "Born and raised")
    print("In {0} {1} born and raised".format(Veriable_ls[0], Veriable_ls[1]))
    #print("on the", Veriable_ls[2],"was where I spent most of my days")
    print("on the {0} was were I spent most of my days".format(Veriable_ls[2]))
    #print("Chillin' out", Veriable_ls[3]+"in'", "relaxin' all cool")
    print("Chillin' out, {0}in' relaxin' all cool".format(Veriable_ls[3]))
    #print("and all",Veriable_ls[4],"some",Veriable_ls[6],"outside of the",Veriable_ls[5])
    print("and all {0} some {1} outside of the {2}".format(Veriable_ls[4], Veriable_ls[6], Veriable_ls[5]))
    #print("When a couple of", Veriable_ls[7]+"'s","who were up to no good")
    print("When a couble of {0}'s who were up to no good".format(Veriable_ls[7]))
    print("Started making Trouble in my neighborhood")
    #print("I got in one little",Veriable_ls[8],"and my mom got",Veriable_ls[9])
    print("I got in one little {0} and my mom got {1}".format(Veriable_ls[8], Veriable_ls[9]))
    #print("She said 'You're movin' with your", Veriable_ls[10], "and", Veriable_ls[11], "in", Veriable_ls[12]+"'")
    print("She said 'You're movin' with your {0} and {1} in {2}'".format(Veriable_ls[10], Veriable_ls[11],Veriable_ls[12]))
    print("=====================================================")
    print("                                                     ")

function()
