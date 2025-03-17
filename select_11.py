# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) > 8:
    print("Password accepted.")
if len(password) < 8:
  print("Error, try again.")
