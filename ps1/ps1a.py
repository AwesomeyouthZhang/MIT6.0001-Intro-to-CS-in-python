annual_salary=float(input("Enter your annual salary :"))
portion_saved=float(input("Enter the percent of your salary to save,as a decimal :"))
total_cost=float(input("Enter the cost of your dream home:"))
monthly_salary=annual_salary/12
current_savings=0
portion_down_payment=total_cost*0.25
months=0
while current_savings<=portion_down_payment:
    months+=1 
    current_savings+=monthly_salary*portion_saved+(current_savings*0.04)/12
print("Number of months:",months)

