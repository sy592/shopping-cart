    #shopping_cart.py

##################
#PRODUCT DATABASE#
##################

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


###################
#INFORMATION INPUT#
###################

#Use a python dictionary to provide O(1) runtime product_id lookup
#If we don't do that, runtime of product_id lookup would be O(N), which means
#we have to go through the whole database each time we check one id
database = {}
for p in products:
    key = str(p["id"])
    database[key] = p
#Source: https://www.w3schools.com/python/python_dictionaries.asp

subtotal_price = 0
selected_ids = []
while True:
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ") #> "9" (string)

    if selected_id == "DONE":
        break
    
    #Data Validation: if selected ids are not in the database, print error message
    elif selected_id not in database:
        print("Hey, are you sure that product identifier is correct? Please try again!")

    else:
       selected_ids.append(selected_id)

#############################
#INFORMATION OUPUT / DISPLAY#
#############################

#print grocery information
print("---------------------------------")
print("SUNING FOODS GROCERY")
print("WWW.SUNING-FOODS-GROCERY.COM")
print("---------------------------------")

#print current date & time
import datetime
now = datetime.datetime.now()
print("CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
#Source: https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

#print selected products
print("---------------------------------")
print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        subtotal_price = subtotal_price + matching_product["price"]
        price_usd = " (${0:.2F})".format(matching_product["price"])
        print(" + " + matching_product["name"] + " " + price_usd)
        
#print subtotal price, sales tax, and total
print("---------------------------------")
subtotal_usd = "${0:.2F}".format(subtotal_price)
print("SUBTOTAL PRICE: " + subtotal_usd)
#calculate and print tax amount by using DC sales tax - 6%
tax = subtotal_price * 0.0875
tax_usd = "${0:.2F}".format(tax)
print("SALES TAX: " + tax_usd)
#calculate the total price by adding the subtotal to the tax amount
total_price = subtotal_price + tax
total_usd = "${0:.2F}".format(total_price)
print("TOTAL PRICE: " + total_usd)

#print ending phrase
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")