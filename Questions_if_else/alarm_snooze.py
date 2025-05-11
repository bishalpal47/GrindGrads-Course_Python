'''
Question: Write a program to take how many times alarm was snoozed from user. 
If more than 3, print "Alarm bhi thak gaya hoga bhai 😩", else "Discipline OP 🔔".
'''

snooze = int(input("Alarm kitni baar snooze kiya? "))
if snooze > 3:
    print("Alarm bhi thak gaya hoga bhai 😩")
else:
    print("Discipline OP 🔔")