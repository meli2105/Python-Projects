print("Welcom to the tip calculator")
bill = float(input("How much $ is the bill?\n"))
pers = int(input("How much % tip would you like to give? 10, 12 or 15?\n"))
tip = (bill * (pers / 100))
total = bill + tip
people = int(input("How many people to split the bill?\n"))
bill_pers = round(total / people, 2)
bill_pers = "{:.2f}".format(bill_pers)
print(f"The bill for each person is: {bill_pers} $")
