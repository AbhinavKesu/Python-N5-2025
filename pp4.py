lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
specialOffer = input("Is a special offer running? (y/n): ")
widthOfSquarePacks = widthOfSquarePacks + additionalRows
if specialOffer == "y":
totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
additionalRows = int(input("Please enter the number of additional rows included for free: "))
print("The number of cans in the pack is: "+str(totalNumberOfCans))
widthOfSquarePacks = lengthOfSquarePacks


