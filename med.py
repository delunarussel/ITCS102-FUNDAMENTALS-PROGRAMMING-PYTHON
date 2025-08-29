#item_price
#item_quantity

item = int(input('input item price -->'))
quantity = int(input('input item quantity -->'))

n1 = item * quantity

print("Your item price:", item)
print("Your quantity", quantity)
print("Your total cost:", n1)

if n1 >= 100:
	discount = n1 * .10
	n2 = n1 - discount
	print("total cost (with a 10% discount)", n2 )

else: 
	print("you are not guaranteed for a discount")