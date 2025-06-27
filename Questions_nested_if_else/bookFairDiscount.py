'''
Question: Book Fair Discount
At Kolkata Book Fair, books under ₹200 get no discount, books ₹200-₹500 get 5% discount, books above ₹500 get 10% discount.

Expected Output Format:
Display original price, discount amount, and final price of the book.
'''

price = float(input("Enter book price: ₹"))

if price < 200:
    discount_percent = 0
elif price <= 500:
    discount_percent = 5
else:
    discount_percent = 10

discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

print(f"Original price: ₹{price}")
print(f"Discount ({discount_percent}%): ₹{discount_amount}")
print(f"Final price: ₹{final_price}")