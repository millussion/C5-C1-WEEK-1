products = [] #list

def new_product():
    product_name = input("Enter product name: ")
    running = True
    while running: #validate that only numbers are entered
        try:
            price = int(input("Enter the unit price of the product: ").replace(",","").replace(".",""))
            running = False
        except ValueError:
            print("wrong. just numbers")

    running = True
    while running: #validate that only numbers are entered
        try:
            amount = int(input("Enter quantity: "))
            running = False
        except ValueError:
            print("wrong. just numbers")

    total = price * amount
    #We save the info in a dictionary
    save_product = {
        "name": product_name,
        "price": price,
        "amount": amount,
        "total": total
    }
    #here we are sending the dictionary to the list
    products.append(save_product)


