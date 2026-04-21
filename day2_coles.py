#定义3个变量，并且增加输入功能，然后通过f-string输出
item_name = input("What's the name of this item?")
price = float(input("What's the price of this item?"))
quantity = int(input("How many items will you buy?"))

if quantity == 1:
    display_name = item_name
else:
    display_name = f"{item_name}s"
    
print(f"\nThe price of {quantity} {display_name} is {price*quantity} AUD")