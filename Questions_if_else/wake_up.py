'''
Question: Write a program to take wake-up time (24-hour format) from user. 
If before 7, print "Oho! early bird 🐦", else print "Bhai tu to alarm ka dushman hai 😴".
'''

time = int(input("Kitne baje uthta hai tu? "))
if time < 7:
    print("Oho! early bird 🐦")
else:
    print("Bhai tu to alarm ka dushman hai 😴")