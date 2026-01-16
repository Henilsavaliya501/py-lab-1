gross_sales = float(input("Enter gross sales: "))

discount = gross_sales * 10 / 100
net_sales = gross_sales - discount

print("Discount =", discount)
print("Net Sales =", net_sales)
