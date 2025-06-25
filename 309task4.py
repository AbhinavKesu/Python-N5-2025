# Program 3 - Investigate and modify
temperature = int(input("Please enter the temperature: "))
while temperature < -20 or temperature > 50:
    print("Error, try again.")
    temperature = int(input("Please enter the temperature: "))


print("Temperature accepted.")
