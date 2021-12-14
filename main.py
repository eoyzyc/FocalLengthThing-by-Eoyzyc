import time
Flag = True
while True:
    print("This is a physics dictionary on focal length")
    print("What do you want to search on?")
    print("""    a) object distance 
    b) image distance 
    c) properties of image 
    d) application of light ray diagram scenario""") 
    question = input("Please select(a/b/c/d): ")
##==========Object Distance (a)==========##
    if question == 'a':
        print("You have selected: object distance")
        Flag = True
        while True:
            print("There are 6 positions which the object can be at ")
            print("""    a)Object at infinity
    b)Object distance greaer than 2F
    c)Object distance equals to 2F
    d)Object distance between F and 2F
    e)Object distance equals F
    f)Object distance less than F""")
            a = input("Please select(a/b/c/d/e/f): ")
            if a == 'a':
                print("You have selected: Object at infinity")
                print("Here, the image formed will be Real and at F")
                print("It can be used in a Telescope")
                break 
            elif a == 'b':
                print("You have selected: Object distance greaer than 2F")
                print("Here, the image formed will be Real, Inverted, Diminished and between F and 2F")
                print("It can be used in a Camera")
                break
            elif a == 'c':
                print("You have selected: Object distance equals to 2F")
                print("Here, the image formed will be Real, Inverted, Same size and at 2F")
                print("It can be used in a Photocopier")
                break
            elif a == 'd':
                print("You have selected: Object distance between F and 2F")
                print("Here, the image formed will be Real, Inverted, Magnified and beyond 2F")
                print("It can be used in a Slide Projector")
                break
            elif a == 'e':
                print("You have selected: Object distance equals F")
                print("Here, the image formed will be at infinity")
                print("It is not used in anything")
                break
            elif a == 'f':
                print("You have selected: Object distance less than F")
                print("Here, the image formed will be Virtual, Upright, Magnified and beyond the object")
                print("It can be used in a magnifying Glass")
                break
            else:
                print("Only inputs a/b/c/d/e/f")
##==========Image Distance (b)==========##
    elif question == 'b':
        print("You have selected: Image distance")
        Flag = True
        while True:
            print("There are 6 positions which the image can be at ")
            print("""    a)Image at F
    b)Image between F and 2F
    c)Image at 2F
    d)Image beyonf 2F
    e)Image at infinity
    f)Image behind the object""")
            b = input("Please select(a/b/c/d/e/f): ")
            if b == 'a':
                print("You have selected: Image between F and 2F")
                print("Here, the image formed will be Real and Object will be at infinity")
                print("It can be used in a Telescope")
                break
            elif b == 'b':
                print("You have selected: Image at 2F")
                print("Here, the image formed will be Real, Inverted, Diminished and Object distance greater than 2F")
                print("It can be used in a Camera")
                break
            elif b == 'c':
                print("You have selected: Image at 2F")
                print("Here, the image formed will be Real, Inverted, Same size and Object distance equals to 2F")
                print("It can be used in a Photocopier")
                break
            elif b == 'd':
                print("You have selected: Image beyonf 2F")
                print("Here, the image formed will be Real, Inverted, Magnified and Object distance between F and 2F")
                print("It can be used in a Slide Projector")
                break
            elif b == 'e':
                print("You have selected: Image at infinity")
                print("Here, Object distance equals F")
                print("It is not used in anything")
                break
            elif b == 'f':
                print("You have selected: Image behind the object")
                print("Here, the image formed will be Virtual, Upright, Magnified and Object distance less than F")
                print("It can be used in a magnifying Glass")
                break
            else:
                print("Only inputs a/b/c/d/e/f")
##==========Properties of Image(c)==========##
    elif question == 'c':
        print("You have selected: properties of image")
        Flag = True
        while True:
            print("There are properties of an image")
            print("""    a) Real
    b) Inverted
    c) Diminished
    d) Same size
    e) Magnified
    f) Virtual
    g) Upright""")
            c = input("Please select(a/b/c/d/e/f/g)")
            if c == 'a':
                print("You have selected: Real")
                print("There are 4 ways a real image can be formed")
                print("Here, object will be at infinity, image formed will be at F")
                print("Or, Object distance will be greater than 2F, Between F and 2F , Diminished and Inverted")
                print("Or, Object distance equals 2F, image at 2F, Inverted and Same size")
                print("Or, Object distance between F and 2F, image will be beyond 2F, Inverrted and Magnified")
                break
            elif c == 'b':
                print("You have selected: Inverted")
                print("There are 3 ways a Inverted image can be formed")
                print("Here, Object distance will be greater than 2F, Between F and 2F, Real and Diminished ")
                print("Or, Object distance equals 2F, image at 2F, Real and Same size")
                print("Or, Object distance between F and 2F, image will be beyond 2F, Real and Magnified")
                break
            elif c == 'c':
                print("You have selected: Diminished")
                print("There is 1 way a Diminished image can be formed")
                print("Here, Object distance will be greater than 2F, Between F and 2F , Real and Inverted")
                break
            elif c == 'd':
                print("You have selected: Same size")
                print("There is 1 way a Same size image can be formed")
                print("Here, Object distance equals 2F, image at 2F, Real and Inverted")
                break
            elif c == 'e':
                print("You have selected: Magnified")
                print("There is 2 way a Magnified image can be formed")
                print("Here, Object distance between F and 2F, image will be beyond 2F, Real and Inverted")
                print("Or, Object distance less than F, image will be behind the object, Virtual, Upright")
                break
            elif c == 'f':
                print("You have selected: Virtual")
                print("There is 1 way a Virtual image can be formed")
                print("Object distance less than F, image will be behind the object, Upright, Magnified")
                break
            elif c == 'g':
                print("You have selected: Upright")
                print("There is 1 way a Upright image can be formed")
                print("Object distance less than F, image will be behind the object, Virtual, Magnified")
                break
            else:
                print("Only inputs a/b/c/d/e/f/g")
##==========Applications of Light Ray Diagram==========##
    elif question == 'd':
        print("You have selected: application if light ray diagram scenario")
        Flag = True
        while True:
            print("There are 5 Applications of light ray diagram sceanario")
            print("""a) Telescope
    b) Camera
    c) Photocopier
    d) Slide Projector
    f) Magnifying Glass""")
            d = input("Please select(a/b/c/d/f): ")
            if d == 'a':
                print("You have selected: Telescope")
                print("Here, the image formed will be Real, Object will be at infinity and image at F")
                break
            elif d == 'b':
                print("You have selected: Camera")
                print("Here, the image formed will be Real, Inverted, Diminished, Object distance greater than 2F and image between F and 2F")
                break
            elif d == 'c':
                print("You have selected: Photocopier")
                print("Here, the image formed will be Real, Inverted, Same size, Object distance equals to 2F and image at 2F")
                break
            elif d == 'd':
                print("You have selected: Slide Projector")
                print("Here, the image formed will be Real, Inverted, Magnified, Object distance between F and 2F and image will be beyond 2F")
                break
            elif d == 'f':
                print("You have selected: Magnifying Glass")
                print("Here, the image formed will be Virtual, Upright, Magnified, Object distance less than F and Image behind the object")
                break
            else:
                print("Only inputs a/b/c/d/f")
    else:
        print("Only inputs a/b/c/d")
##==========Again==========##
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
