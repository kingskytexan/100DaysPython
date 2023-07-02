# Tip Calculator that determines what the total bill person including tip
print("Welcome to the Tip Calculator!")

# User inputs for total bill, tip percentage, and people per bill
total_bill = float(input("What is the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people_per_bill = int(input("How many people to split the bill? "))

# Math operations to determine the total bill person with tip
bill_per_person = total_bill / people_per_bill
tip_per_person = bill_per_person * (tip_percentage / 100)
total_per_person = round(bill_per_person + tip_per_person, 2)

# Prints out the total bill per person with tip included
print(f"Each person should pay: ${total_per_person}")
