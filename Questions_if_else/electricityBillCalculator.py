'''
Question: Electricity Bill Calculator
Calculate electricity bill for households in West Bengal. Up to 100 units: ₹3/unit, above 100 units: ₹5/unit.

Expected Output Format:
Display total bill amount
'''
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 3
else:
    bill = (100 * 3) + ((units - 100) * 5)

print(f"Electricity bill for {units} units: ₹{bill}")