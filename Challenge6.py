Computing = int(input("Enter Computing score: "))
English = int(input("Enter English score: "))
Maths = int(input("Enter Maths score: "))
ArtsDesign = int(input("Enter Arts & Design score: "))
total = English + Maths + ArtsDesign + Computing
average = total / 4
print("Total score is: " + str(total))
print("Average score is: " + str(average))
