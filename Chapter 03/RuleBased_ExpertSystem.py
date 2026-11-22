#Experiment 18: Rule-Based Expert System for Fault Diagnosis
#Description: This program creates a car fault diagnosis expert system using IF-THEN production rules. 
#It asks questions about the car's condition and identifies possible faults along with suggested solutions.

# Car Fault Diagnosis Expert System

print("===== CAR FAULT DIAGNOSIS EXPERT SYSTEM =====")

battery = input("Is the battery working properly? (yes/no): ")
fuel = input("Is fuel available? (yes/no): ")
engine = input("Is the engine overheating? (yes/no): ")
sound = input("Is there an unusual noise? (yes/no): ")
start = input("Is the car starting? (yes/no): ")

print("\n===== DIAGNOSIS RESULT =====")

# Rule 1
if battery == "no":
    print("Problem: Battery is weak or dead.")
    print("Solution: Charge or replace the battery.")

# Rule 2
elif fuel == "no":
    print("Problem: Fuel is empty.")
    print("Solution: Refill the fuel tank.")

# Rule 3
elif engine == "yes":
    print("Problem: Engine overheating.")
    print("Solution: Check coolant and radiator.")

# Rule 4
elif sound == "yes":
    print("Problem: Unusual engine noise.")
    print("Solution: Check engine components.")

# Rule 5
elif start == "no":
    print("Problem: Starter motor problem.")
    print("Solution: Check the starter motor.")

else:
    print("No major car fault detected.")

print("\nDiagnosis Completed.")