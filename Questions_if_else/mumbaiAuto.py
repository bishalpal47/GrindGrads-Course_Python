'''
Question: Mumbai auto rickshaw fare
Take the input for travel distance from user. Auto rickshaw charges ₹25 for first 2 km and ₹8 for each additional km. Calculate total fare.

Expected Output Format:
Display breakdown and total fare amounts properly.
'''

distance = float(input("Enter distance in km: "))

if distance <= 2:
    fare = 25
    print(f"Fare for {distance} km: ₹{fare}")
else:
    base_fare = 25
    additional_distance = distance - 2
    additional_fare = additional_distance * 8
    total_fare = base_fare + additional_fare
    print(f"Base fare (first 2 km): ₹{base_fare}")
    print(f"Additional fare ({additional_distance} km): ₹{additional_fare}")
    print(f"Total fare: ₹{total_fare}")