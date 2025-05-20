products = []
prices = []
totoal = 0

while True:
    product = input("Enter a product to buy ( q to quit ) : ")

    if product.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {product} : $"))
        products.append(product)
        prices.append(price)

print("----- YOUR CART -----")
for product in products:
    print(product, end=" ")
for price in prices:
    totoal += price

print(f"\nYour total is : ${round(totoal,2)}")
