'''
Question : Monsoon Weather Advisory
Create a program that gives weather advisory based on rainfall (in mm): Light rain (0-25), Moderate rain (26-75), Heavy rain (76+). Take value for rainfall amount from user.

Expected Output Format:
Display rain category and appropriate advisory
'''

rainfall = float(input("Enter rainfall in mm: "))

if rainfall <= 25:
    category = "Light rain"
    advisory = "Carry an umbrella"
elif rainfall <= 75:
    category = "Moderate rain"
    advisory = "Avoid unnecessary travel"
else:
    category = "Heavy rain"
    advisory = "Stay indoors, avoid travel"

print(f"{category}: {advisory}")