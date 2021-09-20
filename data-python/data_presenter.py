cupcake_invoices = open('CupcakeInvoices.csv')

for row in cupcake_invoices:
    print(row)

cupcake_invoices.close()

cupcake_invoices = open('CupcakeInvoices.csv')

for row in cupcake_invoices:
    values = row.split(',')
    print(values[2], values[3])

cupcake_invoices.close()

cupcake_invoices = open('CupcakeInvoices.csv')

for row in cupcake_invoices:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)
    
cupcake_invoices.close()

cupcake_invoices = open('CupcakeInvoices.csv')
total = 0

for row in cupcake_invoices:
    values = row.split(',')
    total = total + (int(values[3])) * (float(values[4]))

print(total)
cupcake_invoices.close()

