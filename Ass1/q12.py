print("Hello roll 21052410, input the p, r, t to calculate SI and CI")

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time):
    compound_interest = principal * (pow((1 + rate / 100), time)) - principal
    return compound_interest

# input
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate 
simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
compound_interest = calculate_compound_interest(principal_amount, interest_rate, time_period)

# Print 
print(f"\nSimple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
