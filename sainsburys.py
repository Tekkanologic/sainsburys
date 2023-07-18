"""Sainsburys Test on Hackajob"""

product_names = ["Apples", "Oranges", "Pears"]
quantities = [5, 3, 10]
prices = [1, 2, 1]
discount = 10
delivery_fee = 5

def basket(product_names, quantities, prices, discount, delivery_fee):

    order = []

    for i, product in enumerate(product_names):
        name = product
        price = prices[i] * quantities[i]
        price = price * (100-discount)
        price = price + (delivery_fee*100)
        price = price / 100
        order.append((name, price))
        print(f"{name}: {price} \n")

    #for item in order:
        #output = str(item[0]) + ": " + str(item[1]) + "\n" 
        #print(output)

    #return output

if __name__ == "__name__":
    basket(product_names, quantities, prices, discount, delivery_fee)