import random, time, base64, psutil, os, subprocess
from multiprocessing import Queue
from stegano import lsb

q = Queue()
def guessNum():
    aNum = random.randint(1, 100)
    guessestaken = 0
    print(aNum)
    while guessestaken < 5:
        guess = int(input("Enter your guess: "))
        if guess == aNum:
            print("You guessed the right number!")
            q.put("stg1compte")
            break
        elif guess > aNum:
            guessestaken += 1
            print("Your guess is too high!")
            print("You have guessed ", guessestaken, "times.")
            print("Try again!")
        elif guess < aNum:
            guessestaken += 1
            print("Your guess is too low!")
            print("You have guessed ", guessestaken, "times.")
            print("Try again!")
    print("You failed!!")
    q.put("faild")
    subprocess.call(["python", "game/fork.py"])

def prob():
    s = time.time()
    while s < 600:
        wait = q.get()
        if wait == "stg1compte":
            q.close()
            print("Good luck! You'll need it!")
            please = random.randint(1, 1000000)
            while please != 192:
                please = random.randint(1, 1000000)
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
    quit()

def mem():
    while True:
        wait = q.get()
        if wait == "proddon":
            q.close()
            print("Your job it to get your memory all the way to 99%")
            memory = psutil.virtual_memory().percent
            while memory <= 95:
                memory = psutil.virtual_memory().percent
                print(memory, end = "\r")
                if memory >= 95:
                    print("Nice job!")
                    print("Now you have to make your memory to 25%")
                    if memory <= 25:
                        print("On to the next stage")
                        print("Only 2 stages left!")
                        q.put("memdone")
                    else:
                        continue
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
            randNum = random.randint(100, 999)
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            wordPart = ''.join(random.choice(letters) for _ in range(3))
            password = wordPart + str(randNum)
            guess = None
            print("Great job finishing the first task!")
            print("Now, you have to guess the password!")
            time.sleep(1)
            print("The password consists of 3 lowercase and uppercase letters followed by 3 digits")
            print("You can use any means necessary (Bruteforce, dictionary attack, etc.)")
            while guess != password:
                guess = str(input("Enter the password: "))
                if guess == password:
                    print("You guessed the right password!")
                    q.put("pswdone")
                else:
                    print("You guessed the wrong password!")
                    print("Try again!")
                    os.system("shutdown /s /t 0")
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
            print("Nice job on completing the previous stage!")
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
                    os.system("shutdown /s /t 60")
                    print("Shutting down system in 60 seconds")
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
            
            theflag = input("Enter the flag: ")
            while theflag != lsb.reveal("game/images/new.png"):
                theflag = input("Enter the flag")
                if theflag == lsb.reveal("game/images/new.png"):
                    print("You did it! You won!!!!")
                else:
                    subprocess.call(["python", "game/fork.py"])
                    continue
        else:
            quit()
def get_leaderboard(filename):
    try:
        with open(filename, 'r') as file:
            leaderboard = []
            for line in file:
                parts = line.strip().split('. ')
                if len(parts) > 1:
                    name_time = parts[1].split(', ')
                    if len(name_time) == 2:
                        usrname, time = name_time
                        time_value = ''.join(filter(str.isdigit, time))  
                        try:
                            leaderboard.append((usrname, int(time_value)))
                        except ValueError:
                            print(f"Invalid points value: {time}")
            return leaderboard
    except FileNotFoundError:
        return []

def update_leaderboard(filename, usrname, time):
    leaderboard = get_leaderboard(filename)
    leaderboard.append((usrname, time))
    leaderboard.sort(key=lambda x: x[1])  

    with open(filename, 'w') as file:
        for i, entry in enumerate(leaderboard, start=1):
            file.write(f"{i}. {entry[0]}, {entry[1]} seconds\n")

def main2():
    name = input("Before proceeding, enter a name you would like to be called in the leaderboard: ")
    start = time.time()
    print("Welcome to the impossible game!")
    print("Your goal is to guess the right number!")
    guessNum()
    time.sleep(0.8)
    paswrdGuess()
    time.sleep(0.8)
    decrypt()
    time.sleep(0.8)
    mem()
    time.sleep(1)
    print("Now that your computer is very slow,\nyou will now have to leave it to chance to continue to the next stage")
    time.sleep(0.8)
    prob()
    time.sleep(0.8)
    print("Nice job! This is the last and hardest stage!")
    time.sleep(0.8)
    steg()
    end = time.time()
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
    filename = 'leaderboard.txt'
    update_leaderboard(filename, name, rem)
main2()
