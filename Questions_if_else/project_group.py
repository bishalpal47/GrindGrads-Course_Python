'''
Question: Write a program to take the number of people in project group from user. 
If less than 2, print "Solo legend 🤘", else print "Teamwork OP 🔥".
'''

members = int(input("Kitne log hain project group mein? "))
if members < 2:
    print("Solo legend 🤘")
else:
    print("Teamwork OP 🔥")