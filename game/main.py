import subprocess, time

def func():
    choice = input("Type in a difficulty level (hard, easy): ")
    if choice == "hard":
        ask = input("Have you read and signed the consent form? (y/n) ")
        if ask == "y":
            from hard import main2
            main2()
        elif ask == "n":
            print("Please read and sign the consent form before playing the hard mode.")
            quit()
        else:
            print("Input not found.")
    elif choice == "easy":
        from easy import main1
        main1()
    else:
        print("The choice you selected is not valid")
func()
from hide import hider
hider()
