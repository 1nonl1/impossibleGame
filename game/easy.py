import random, time, base64, psutil
from stegano import lsb
from multiprocessing import Queue

q = Queue()
def guessNum():
    aNum = random.randint(1, 100)
    guess = None
    while guess != aNum:
        guess = int(input("Enter your guess: "))
        if guess == aNum:
            print("You guessed the right number!")
            q.put("stg1compte")
        elif guess > aNum:
            print("Your guess is too high!")
            print("Try again!")
        elif guess < aNum:
            print("Your guess is too low!")
            print("Try again!")
    q.put("faild")

def prob():
    while True:
        wait = q.get()
        if wait == "stg1compte":
            print("Good luck! You'll need it!")
            please = random.randint(1, 1000000)
            while please != 192:
                print(please, end = "\r")
                time.sleep(0.05)
                if please == 192:
                    print("Yay! You can continue to the next stage!")
                    q.put("proddon")
                else:
                    continue
            q.put("faild")
        else:
            quit()

def mem():
    while True:
        wait = q.get()
        if wait == "probdon":
            q.close()
            print("Your job it to get your memory all the way to 99%")
            memory = psutil.virtual_memory().percent
            while memory <= 99:
                memory = psutil.virtual_memory().percent
                print(memory, end = "\r")
                if memory >= 99:
                    print("Nice job!")
                    print("Only 2 more stages left!")
                    q.put("memdone")
                else:
                    continue
            q.put("faild")
        else:
            quit()
def paswrdGuess():
    while True:
        wait = q.get()
        if wait == "memdone":
            q.close()
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            password = ''.join(random.choice(letters) for _ in range(2)) + str(random.randint(10, 99))
            guess = None
            print("Great job finishing the first task!")
            print("Now, you have to guess the password!")
            time.sleep(1)
            print("The password consists of 2 lowercase and uppercase letters followed by 2 digits")
            print("You can use any means necessary (Bruteforce, dictionary attack, etc.)")
            while guess != password:
                guess = str(input("Enter the password: "))
                if guess == password:
                    print("You guessed the right password!")
                    q.put("pswdone")
                else:
                    print("You guessed the wrong password!")
                    print("Try again!")
            q.put("faild")
        else:
            quit()

def decrypt():
    while True:
        wait = q.get()
        if wait == "pswdone":
            q.close()
            message = b"Life isn't always fun, it can be challenging, boring, or sometimes even painful. But just remember to take it day by day, and you will learn to love life for what it is."
            toBase64 = base64.standard_b64encode(message)
            toBase85 = base64.a85encode(toBase64)
            choice = None
            print("Nice job on completing the last stage!")
            print("Now you need to decrypt a binary Ascii message!")
            time.sleep(1)
            print("Your job is to decrypt the message and find the hidden message!")
            print("The encrypted message: ", toBase85)
            while choice != base64.standard_b64decode(base64.a85decode(toBase85)).decode('utf-8'):
                choice = str(input("Enter the decrypted message: "))
                if choice == base64.standard_b64decode(base64.a85decode(toBase85)).decode('utf-8'):
                    print("You decrypted the message!")
                    q.put("decdone")
                elif choice == "/hint":
                    print("The encrypted message is in base85")
                elif choice != base64.standard_b64decode(base64.a85decode(toBase85)).decode('utf-8'):
                    print("Incorrect! Try Again!")
            q.put("faild")
        else:
            quit()
            
def steg():
    while True:
        wait = q.get()
        if wait == "decdone":
            q.close()
            print("For this part, you will have to find the message in a picture!")
            time.sleep(0.5)
            print("You will need to use stenography in order to pass this!")
            print("You will need to find the folder that holds the pictures!")
            time.sleep(0.5)
            print("But wait! That folder is encrypted!")
            print("Best of luck!")
            time.sleep(0.5)
            x = 1
            theflag = input("Enter the flag: ")
            while theflag != lsb.reveal("game/images/new.png"):
                theflag = input("Enter the flag")
                print("You did it! You won!!!!") if theflag == lsb.reveal("game/images/new.png") else x = 0
        else:
            quit()

def main1():
    start = time.time()
    print("Welcome to the impossible game!")
    print("Your goal is to guess the right number!")
    guessNum()
    time.sleep(0.8)
    prob()
    time.sleep(0.8)
    mem()
    time.sleep(0.8)
    paswrdGuess()
    time.sleep(0.8)
    decrypt()
    time.sleep(0.8)
    steg()
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
main1()