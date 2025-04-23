print("Welcome to Izfin Technology - Annual Tax Revenue (ATR) Calculator")

years_of_experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))

if years_of_experience > 25 and age >= 55:
    atr = 5600000
elif years_of_experience > 20 and age >= 45:
    atr = 4480000
elif years_of_experience > 10 and age >= 35:
    atr = 1500000
else:
    atr = 550000

    print(f"\nAnnual Tax Revenue (ATR) for this staff is: ₦{atr}")
