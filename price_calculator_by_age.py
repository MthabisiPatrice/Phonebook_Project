price_kid = input("What is the price of a child's meal? $" )
price_adult = input("What is the price of an adult's meal? $")
count_child = input('How many children are there? ')
adult_count = input('How many adults are there? ')
sale_tax= input('What is the sales tax rate? ')

#these are the computations for the values of totals and tax.
subtotal = float(price_kid) * int(count_child) + float(price_adult) * int(adult_count)
tax = float(sale_tax)/100 * subtotal
grand_total = subtotal+ tax

#these are the print statements for the various prompts that are there. 
print(' ')
print(f'Subtotal:${subtotal:.2f}')
print(f'tax:${tax:.2f}')
print(f'Total:${grand_total:.2f}')
print(' ')

amount_paid = input('What is the payment amount? $')

#this is the computed change and the print statement for the change.
change = float(amount_paid) - grand_total
print(f'Change:${change:.2f}')