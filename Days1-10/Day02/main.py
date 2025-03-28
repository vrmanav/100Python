# Tip Calculator

bill_amount = float(input("What was the bill amount:\n"))
tip = float(input("What percent of tip would you like to give:\n"))
tip_as_percent = tip / 100
tip_amount = bill_amount * tip_as_percent
bill_with_tip = bill_amount + tip_amount
persons = int(input("How many persons do you want to split the bill:\n"))
final_bill = bill_with_tip / persons

print(f"Each person needs to pay ₹{final_bill}")
