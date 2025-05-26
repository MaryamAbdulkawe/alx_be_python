monthly_savings = float(input("Enter your monthly income:")) - float(input("Enter your total monthly expenses:"))
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", annual_savings)
