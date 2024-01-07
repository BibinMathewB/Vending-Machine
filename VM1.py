print('Welcome to the ||||𝖥𝗅𝗈𝖺𝗍 𝖵𝖾𝗇𝖽𝗂𝗇𝗀 𝖬𝖺𝖼𝗁𝗂𝗇𝖾||||')
print('________________________________________')
#define a dictionary of items and their prices
items={
    "Drinks": {
    "A1": {"name": "Coco cola", "price": 2.50, "stock": 10},
    "B1": {"name": "Sprite", "price": 1.50, "stock": 5},
    "C1": {"name": "Pepsi", "price": 2.50, "stock": 10},
    "D1": {"name": "7up", "price": 1.50, "stock": 5},
     },
    "Snacks": {
    "E2": {"name": "Snickers", "price": 2.50, "stock": 10},
    "F2": {"name": "Lindor", "price": 1.50, "stock": 10},
    "G2": {"name": "Mars", "price": 1.00, "stock": 10},
    "H2": {"name": "Toblerone", "price": 2.50, "stock": 10},
    },
    "Chips": {
    "I3": {"name": "Lays", "price": 1.50, "stock": 10},
    "J3": {"name": "Oman Chips", "price": 1.00, "stock": 10},
    "K3": {"name": "Krispy jr", "price": 1.50, "stock": 5},
    "L3": {"name": "Pringles", "price": 3, "stock": 10},
    },
}

# function to print the menu of items
def print_menu(items):
    print("Menu: \n")
    for category, category_items in items.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}:{item["name"]} ({item["price"]:.2f} dhs)')
print()

# function to get a valid code from the user
def get_code(items):
    while True:
        code = input ("Enter code: ")
        #check if code is valid
        for category, category_items in items.items():
            if code in category_items:
                return code
print("Error: Invalid code. Please try again.")

# function to get a valid amount of money from the user
def get_money(items, code):
    # search for item in Drinks, Snacks and chips dict
    for category, category_items in items.items():
        if code in category_items:
            items = category_items[code]
            break
        else:
            print(f'Error: Invalid code "{code}".')
            return
        
    while True:
            money=float (input("Enter amount of money: "))
            # check if enough money was provided
            if money >= items["price"]:
                return money
            print(f'Error: Not enough money. Please insert {items["price"] - money:.2f} dhs more.')

# function to dispense an item and calculate change
def dispense_item(items, code, money):
    # search for item in Drinks, Chips and Snacks dictionaries
    for category, category_items in items.items():
        if code in category_items:
            items = category_items [code]
            break
        else:
            print(f'Error: Invalid code "{code}".')
            return
        #check if the item is in stock
    if items ["stock"] > 0:
            #dispense the item and calculate the change
            print(f'\nDispensing {items["name"]}...')
            change = money - items["price"]
            items["stock"] -= 1
            print (f"Returning ${change:.2f} change...\n")
    else:
        print(f'\nError: (item["name"]) is out of stock.')    

# function to suggest an additional purchase based on the previous purchase
def suggest_purchase(items, code):
    if code in items["Drinks"]:
        print("You might also like: ")
        for code, items in items ["Snacks"].items():
            print(f'{code}: {items["name"]} ({items["price"]:.2f}dhs)')
    elif code in items ["Snacks"]:
        print("You might also like:")
        for code, item in items ["Drinks"].items():
            print(f'{code}:{item["name"]} ({items["price"]:.2f}dhs)')

# the program
while True:
    #print the menu of items
     print_menu(items)
     #get the valid code from user
     code=get_code(items)
     # get a valid amount of money from the user
     money = get_money(items, code)
     #dispense the item and calculate change
     dispense_item(items, code, money)
     #suggest an additional purchase based on the previous purchase
     suggest_purchase(items, code)
     #make the user to prompt continue or exit
     while True:
         response = input("\nWould you like to make another purchase? (y/n) ")
         if response.lower() == "y":
             break
         elif response.lower() == "n":
             print("Thank you for using the ||||𝖥𝗅𝗈𝖺𝗍 𝖵𝖾𝗇𝖽𝗂𝗇𝗀 𝖬𝖺𝖼𝗁𝗂𝗇𝖾|||| vending machine!")
             exit()
         else:
            print("Error: Invalid response. Please try again.")

 
    