import time
from datetime import datetime
import string
import random
import os


print("bvukasin14 ")
print("Visit my profile on GitHub for more info.")
print("-------")
print("Password Generator v1.0")
curuse = os.environ.get("USERNAME")
mynewpass = ""
ch = int(input("How many characters you want? "))

if ch >= 8 and ch <= 64:
    print("Okay,", ch, "characters!")
    print("Generating...")
    for j in range(ch):
        if random.choice([True, False]):
            mynewpass += random.choice(string.ascii_letters)
        else:
            mynewpass += str(random.randint(0, 9))
    print("Here's your new password: ")
    print(mynewpass)
    time.sleep(1)
    passname = str(input("Please name your password to recognise it: "))
    time.sleep(2)
    print("Saving your password to C:/Users/" + curuse + "/Documents/password-generator.txt")
    time.sleep(2)
    dat = datetime.now()
    totxt = str(dat) + " " + passname + " " + mynewpass
    with open("C:/Users/" + curuse + "/Documents/password-generator.txt", "a+") as myfile:
        myfile.write("\n" + totxt)
    print("Saved!")
    time.sleep(2)
else:
    print("Please choose number between 8 and 64!")
    time.sleep(2)




