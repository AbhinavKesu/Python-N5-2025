thisArray = [50, 100, 150, 200, 250, 300,]
totalamountofDogfood = len(thisArray[0])
pos = 0
for index in range(1, len(thisArray)):
    if len(thisArray[index]) > totalamountofDogfood:
       totalamountofDogfood = len(thisArray[index])
pos = [index]

print(thisArray[pos], "total amount of dog food given to the dog over 5 days", totalamountofDogfood) 