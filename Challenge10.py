unit_cost = 0.15
start_reading = int(input("What is the reading at the start of the month? "))
end_reading = int(input("What is the reading at the end of the month? "))
units_used = end_reading - start_reading
cost = unit_cost * units_used
print(f"The total bill is", {int(cost) + 12})