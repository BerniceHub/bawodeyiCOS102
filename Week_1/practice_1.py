print("This is used to calculate the final amount after applying simple interest, compound interest and annuity.")
print("To calculate the final amount after applying the Simple Interest, enter an input for the following values:")
P = float(input("Enter Principal Amount (P): "))
R = float(input("Enter Rate of Interest (R%): "))
T = float(input("Enter Time Period (T years): "))
A = P * (1 + (R / 100) * T)
print(f"The total amount(in naira) after adding the Simple Interest is {A}")

print("To calculate the final amount after applying the Compound Interest, enter an input for the following values:")
P = float(input("Enter Principal Amount (P): "))
R = float(input("Enter Rate of Interest (R%): "))
t = float(input("Enter Time Period (T years): "))
n = int(input("Enter the no. of periods the interests will be compounded (n): "))
A = P * (1 + (R / (100 * n))) ** (n * t)
print(f"The total amount(in naira) after adding the Compound Interest is {A}")

print("To calculate the accumulated value of Annuity, enter an input for the following values:")
PMT = float(input("Enter Payment Amount (PMT): "))
R = float(input("Enter Rate of Interest (R%): "))
n = int(input("Enter Number of Payments per Year (n): "))
t = float(input("Enter Number of Years (t): "))
Rn = R / (100 * n)  # to convert rate to a fraction
A = PMT * ((1 + Rn) ** (n * t) - 1) / Rn
print(f"The total amount(in naira) after adding the Annuity is {A}")
