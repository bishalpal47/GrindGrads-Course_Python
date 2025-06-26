'''
Problem: Suggest appropriate clothing for Kolkata weather.
- Temperature > 35°C: "Wear light cotton clothes and carry water"
- Temperature 25-35°C: "Comfortable weather - normal clothes"
- Temperature 15-24°C: "Pleasant weather - light jacket recommended"
- Temperature < 15°C: "Cold weather - wear warm clothes"
'''

temperature = float(input("Enter temperature in Celsius: "))

if temperature > 35:
    print("Wear light cotton clothes and carry water")
elif 25 <= temperature <= 35:
    print("Comfortable weather - normal clothes")
elif 15 <= temperature <= 24:
    print("Pleasant weather - light jacket recommended")
elif temperature < 15:
    print("Cold weather - wear warm clothes")


'''
Yes, as you noticed, there is no else statement at the end.
It is possible to have an if-elif-else statement without else statement.

However, you can do this too - 

temperature = float(input("Enter temperature in Celsius: "))

if temperature > 35:
    print("Wear light cotton clothes and carry water")
elif 25 <= temperature <= 35:
    print("Comfortable weather - normal clothes")
elif 15 <= temperature <= 24:
    print("Pleasant weather - light jacket recommended")
elif temperature < 15:
    print("Cold weather - wear warm clothes")
else:
    print("Invalid temperature entered")

'''