'''
Question: Take wake-up time (24-hour format). If before 7, print "Oho! early bird 🐦", else print "Bhai tu to alarm ka dushman hai 😴".
'''

time = int(input("Kitne baje uthta hai tu? "))
if time < 7:
    print("Oho! early bird 🐦")
else:
    print("Bhai tu to alarm ka dushman hai 😴")