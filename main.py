import random
name = input("pelse give your name: ")
number = input("plses select number: ")
chanse = random.randint(0 , 100)
while int(number) != chanse:
    print(chanse)
    help = input("plse certin range number: ")
    if help == "up":
       chanse = random.randint(chanse , 100) 
    elif help == "down":
        chanse = random.randint(0 , chanse)
print("its ",chanse," vectoryyyy... ",name)


