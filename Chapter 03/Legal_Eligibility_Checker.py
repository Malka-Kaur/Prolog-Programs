#Experiment 17: Legal Eligibility Checker
#Description: This program checks a person's eligibility for voting, driving, and employment based on their age. 
#It uses IF-ELSE conditional statements to make decisions.

# Legal Eligibility Checker

age = int(input("Enter your age: "))

# Voting Eligibility
if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")

# Driving Eligibility
if age >= 18:
    print("Eligible for Driving")
else:
    print("Not Eligible for Driving")

# Employment Eligibility
if age >= 18:
    print("Eligible for Employment")
else:
    print("Not Eligible for Employment")