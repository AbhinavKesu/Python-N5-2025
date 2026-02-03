import random 
counter=0
decision= "yes"
fruitnames = ["apple", "banana", "blueberry", "kiwi", "mango", "orange", "peach", "pineapple", "raspberry", "strawberry"]
userfruit= []

while decision == "yes" and counter <0:
    userinput = input("please enter the fruit name")
    while len(userinput) < 4:
        print("incorrect fruit name")
        userinput = input("please enter the fruit name: ")
        counter = counter + 1
        decison = input("enter another fruitname")


number = random.randit(0,9)



        

