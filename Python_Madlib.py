


COMPASS_DIRECTION = input("Enter a Compass direction: ") #0
CITY = input("Enter a city: ") #1
PLACE = input("Enter a place: ") #2
VERB = input("Enter a verb: ") #3
VERB2 = input("Enter a diffrent verb: ") #4
PLACE2 = input("Enter a diffrent place: ") #5
ACTIVITY = input("Enter your favorite activity: ") #6
NOUN = input("Enter a noun: ") #7
NOUN2 = input("Enter a diffrent noun: ") #8
EMOTION = input("Enter an emotion: ") #9
FAMILY = input("Enter a family member: ") #10
FAMILY2 = input("Enter a diffrent family member: ") #11
CITY2 = input("Enter a diffrent city: ") #12

Madlib_ls = [COMPASS_DIRECTION, CITY, PLACE, VERB, VERB2, PLACE2, ACTIVITY, NOUN, NOUN2, EMOTION, FAMILY, FAMILY2, CITY2]



def function():
    print("                                                    ")
    print("====================================================")
    print("The Fresh Prince of", Madlib_ls[12])
    print("====================================================")
    print("In", Madlib_ls[0], Madlib_ls[1], "Born and raised")
    print("on the", Madlib_ls[2],"was where I spent most of my days")
    print("Chillin' out", Madlib_ls[3]+"in'", "relaxin' all cool")
    print("and all",Madlib_ls[4],"some",Madlib_ls[6],"outside of the",Madlib_ls[5])
    print("When a couple of", Madlib_ls[7]+"'s","who were up to no good")
    print("Started making Trouble in my neighborhood")
    print("I got in one little",Madlib_ls[8],"and my mom got",Madlib_ls[9])
    print("She said 'You're movin' with your", Madlib_ls[10], "and", Madlib_ls[11], "in", Madlib_ls[12]+"'")
    #print("She said 'You're movin' with your {10} and {11} in {12}'".format(Madlib_ls[10], Madlib_ls[11], c=Madlib_ls[12]))
    print("=====================================================")
    print("                                                     ")

function()

# Add a list
