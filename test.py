import time 
import random
OD = ['Object at Infinity', 'Object greater than 2F', 'Object equals to 2F', 'Object equal distance between F and 2F', 'Object distance equals 2F', 'Object distance less than F']
ID = ['Image at F', 'Image between F and 2F', 'Image at 2F', 'Image beyond 2F', 'Image at infinity', 'Image behind the object']
OT = ['Real and can be used in a Telescope','Real, Inverted, Diminished and can be used in a Camera','Real, Inverted, Same size and can be used in a Photocopier','Real, Inverted, Magnified and can be used in a Slide projector',' ','Virtual, Upright, Magnified and can be used in a Magnifying glass']
Flag = True
while True:
    print("This is a physics test on focal length")
    print("What do you want to search on?")
    print("""    a) object distance 
    b) image distance """) 
    question = input("Please select(a/b): ")
    if question  == 'a':
        print("You have chosen: Object distance")
        a = random.choice(OD)
        aOD = OD.index(a)
        aID = ID[aOD]

        print("What is the position of the image when " + str(a))
        print("""    0) Image at F
    1) Image between F and 2F
    2) Image at 2F
    3) Image beyond 2F
    4) Image at infinity
    5) Image behind the object""")
        Flag = True
        while True:
            aAnswer = input("What is your answer(0-5)?: ")
            if aAnswer == str(aOD):
                print("Congragulation you got it correct!")
                aOT = OT[aOD]
                print("The properties and application are: " + str(aOT))
                time.sleep(2)
                break
            elif aAnswer != str(aOD):
                print("SOrry you got it wrong...")
                print("Try again")
                time.sleep(2)
    elif question  == 'b':
        print("You have chosen: Image distance")
        b = random.choice(ID)
        bID = ID.index(b)
        bOD = OD[bID]
        print("What is the position of the image when " + str(b))
        print("""    0) Object at Infinity
    1) Object greater than 2F
    2) Object equals to 2F
    3) Object equal distance between F and 2F
    4) Object distance equals 2F
    5) Object distance less than F""")
        Flag = True
        while True:
            aAnswer = input("What is your answer(0-5)?: ")
            if aAnswer == str(bID):
                print("Congragulation you got it correct!")
                bOT = OT[bID]
                print("The properties and application are: " + str(bOT))
                time.sleep(2)
                break
            elif aAnswer != str(bID):
                print("SOrry you got it wrong...")
                print("Try again")
                time.sleep(2)
##==========Again==========##
    else:
        print("Only inputs a/b/c/d")
    Flag = True
    while True:
        tryAgain = input("Do you want to try again? (y/n)")
        if tryAgain == 'y':
            print("Restarting...")
            time.sleep(0.5)
            break
        elif tryAgain == 'n':
            print("Goodbye")
            time.sleep(2)
            exit()
