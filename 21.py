gross = float(input("Enter gross salary: "))

allowance = gross * 10 / 100
deduction = gross * 3 / 100

net_salary = gross + allowance - deduction

print("Allowance =", allowance)
print("Deduction =", deduction)
print("Net Salary =", net_salary)
