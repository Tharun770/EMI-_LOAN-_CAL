def loan_calculator(principal, annual_rate, years):


  # Convert annual rate to monthly
    monthly_rate = annual_rate / 100 / 12 

  # Total months  
    months = years * 12   
  # If interest rate is 0% 
    if monthly_rate == 0:   
        monthly_payment = principal / months
    else:
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    
    total_payment = monthly_payment * months
    total_interest = total_payment - principal
    
    return monthly_payment, total_payment, total_interest

principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (in %): "))
years = int(input("Enter loan tenure (in years): "))

monthly_payment, total_payment, total_interest = loan_calculator(principal, annual_rate, years)

print(f"\nMonthly Payment: {monthly_payment:.2f}")
print(f"Total Payment: {total_payment:.2f}")
print(f"Total Interest: {total_interest:.2f}")




