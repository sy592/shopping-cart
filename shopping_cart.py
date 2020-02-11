    #shopping_cart.py

#Import environement variable TAX_RATE
from dotenv import load_dotenv
import os
load_dotenv()
tax_rate = os.getenv("TAX_RATE", default="0.0875")
tax_rate = float(tax_rate)

#Import email function
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

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
#      WRITE INTO .TXT      #
#############################

import datetime
import os
now = datetime.datetime.now()
filename = "receipts/" + now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, 'w')
#Source: https://www.w3schools.com/python/python_file_write.asp
#Source: https://www.tutorialspoint.com/python3/time_strftime.htm
#Source: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output

#Creating Template
temp_html_content=""

#print grocery information
print("---------------------------------")
print("SUNING FOODS GROCERY")
print("WWW.SUNING-FOODS-GROCERY.COM")
print("---------------------------------")
f.write("---------------------------------\n")
f.write("SUNING FOODS GROCERY\n")
f.write("WWW.SUNING-FOODS-GROCERY.COM\n")
f.write("---------------------------------\n")

#print current date & time
time_str = "CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p")
print(time_str)
f.write(time_str + "\n")
#Source: https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

#print selected products
print("---------------------------------")
print("SELECTED PRODUCTS:")
f.write("---------------------------------\n")
f.write("SELECTED PRODUCTS:\n")

for selected_id in selected_ids:
    # matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    # matching_product = matching_products[0]

    matching_product = database[selected_id] 

    subtotal_price = subtotal_price + matching_product["price"]
    price_usd = " (${0:.2F})".format(matching_product["price"])
    item_str = " + " + matching_product["name"] + " " + price_usd
    print(item_str)
    f.write(item_str + "\n")

    temp_html_content+="<li>You ordered: "
    temp_html_content+=matching_product["name"]
    temp_html_content+=" </li>"
        
#print subtotal price, sales tax, and total
print("---------------------------------")
f.write("---------------------------------\n")
subtotal_usd = "${0:.2F}".format(subtotal_price)
print("SUBTOTAL PRICE: " + subtotal_usd)
f.write("SUBTOTAL PRICE: " + subtotal_usd + "\n")
#calculate and print tax amount by using NY sales tax - 6%
tax = subtotal_price * tax_rate
tax_usd = "${0:.2F}".format(tax)
print("SALES TAX: " + tax_usd)
f.write("SALES TAX: " + tax_usd + "\n")
#calculate the total price by adding the subtotal to the tax amount
total_price = subtotal_price + tax
total_usd = "${0:.2F}".format(total_price)
print("TOTAL PRICE: " + total_usd)
f.write("TOTAL PRICE: " + total_usd + "\n")

#print ending phrase
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

f.write("---------------------------------\n")
f.write("THANKS, SEE YOU AGAIN SOON!\n")
f.write("---------------------------------")

f.close()

print("Do you want to receieve receipts by email? Please enter 'y' or 'n'")
if(input()=="y"):
	subject = "Your Receipt from the Green Grocery Store"
	html_content ="<img src='https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png'><h3>Hello this is your receipt</h3><p>Date: "
	html_content+=now.strftime("%Y-%m-%d %I:%M:%S %p")
	html_content+="</p><p>Total: "
	html_content+=str(total_usd)
	html_content+="</p><ul>"
	html_content+=temp_html_content
	html_content+="</ul>"
	print("HTML:", html_content)
	client_email = input("Please Enter Your Email Address: ")
	message = Mail(from_email=MY_ADDRESS, to_emails=client_email, subject=subject, html_content=html_content)
	try:
	    response = client.send(message)
	    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
	    print(response.status_code) #> 202 indicates SUCCESS
	    print(response.body)
	    print(response.headers)

	except Exception as e:
	    print("OOPS", e.message)
