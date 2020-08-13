class Product():
    def __init__(self, name = None, id = None, quantity = None, price = None):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price

class Catagory():
    def __init__(self, name = None):
        self.name = name
        
class Inventory:

    def __init__(self):
        self.inventory_raw = {}
    # THIS IS FOR CREATING A NEW CATAGORY AND ADDING NEW PRODUCTS
    def add_to_inventory_new_catagory(self):
        print("\t\t---Creating a new Catagory with Product---")
        try:
            catagory=Catagory(input("Catagory Name to create: ").capitalize())
            if catagory.name in self.inventory_raw.keys():
                print("Error, {} has already been created".format(catagory.name))
            else:
                product=Product(input('Product Name: ').capitalize(), int(input("ID: ")),\
                int(input("Quantity: ")), float(input("Price: $")))
                self.inventory_raw.update({catagory.name : {product.name : [product.id, product.quantity, product.price]}})
        except:
            print("--Error--\n--Make sure to fill in all info correctly--")


    #  THIS ASKS FOR A NEW PRODUCT TO BE ADDED INTO THE EXISTING CATAGORY
    def add_product_to_existing_catagory(self):
        print("\t\t---Adding products to existing Catagories---")

        def inventory_keys():
            def yield_keys(dictionary):
                index = 0
                for keys in dictionary:
                    index += 1
                    yield "{}.{}".format(index,keys) 
            for catagory_key in yield_keys(self.inventory_raw):
                print(catagory_key)
        inventory_keys()
        
        # this asks for the catagory
        try:
            catagory=Catagory(input("Catagory Name: ").capitalize())
            if catagory.name not in inventory.inventory_raw.keys():
                print("--Error: {} has not been created--".format(catagory.name))
            else:
                product=Product(input('Product Name: ').capitalize(), int(input("ID: ")),\
                int(input("Quantity: ")), float(input("Price: $")))
                if product.name in inventory.inventory_raw[catagory.name]:
                    print("--Error: Item already in the given Catagory")
                else:
                    self.inventory_raw[catagory.name][product.name] = [product.id, product.quantity, product.price]
        except:
            print("---Make sure to fill in all info correctly---")
    
    # THIS IS TO DELETE A CATAGORY
    def deleting_a_catagory(self):
        print("\t\t---Deleting A Catagory---")
        def inventory_keys():
            def yield_keys(dictionary):
                index = 0
                for keys in dictionary:
                    index += 1
                    yield "{}.{}".format(index,keys) 
            for catagory_key in yield_keys(self.inventory_raw):
                print(catagory_key)
        inventory_keys()
        catagory=Catagory(input("Catagory Name to delete: ").capitalize())
        if catagory.name in self.inventory_raw:
            print('Catagory deleted')
            del self.inventory_raw[catagory.name]
        else:
            print('---Catagory not found---')
   
    # TO DELETE PRODUCTS INSIDE CATAGORIES
    def delete_products_inside_catagories(self):
        print("\t\t---Deleting Products inside Catagories---")
        
        def inventory_keys():
            def yield_keys(dictionary):
                index = 0
                for keys in dictionary:
                    index += 1
                    yield "{}.{}".format(index,keys) 
            for catagory_key in yield_keys(self.inventory_raw):
                print(catagory_key)
        inventory_keys()

        # Ask For Catagory Name:
        catagory=Catagory(input("Catagory Name to create: ").capitalize())
        if catagory.name not in inventory.inventory_raw.keys():
            print("--Error: {} does not exist--".format(catagory.name))
        else:
            product=Product(input('Product Name: ').capitalize())
            try:
                if catagory.name != "":
                    del self.inventory_raw[catagory.name][product.name]
                else:
                    for products in self.inventory_raw.values():
                        if product.name in products:
                            del products[product.name]
            except:
                    print("---No product found in the given Catagory---")

    # To Change the price of the product
    def change_product_price(self):
        print("\t\t---Changing Product Price---")
        try:
            counter = 0
            product_name = Product(input("Product Name: ").capitalize())
            new_price = float(input("The new price will be: $"))
            for products in inventory.inventory_raw.values():
                for product, info in products.items():
                    if product == product_name:
                        counter += 1
                        info[2] = new_price
            if counter == 0:
                print("Invalid amount or Product not found")
            else:
                print("---Price Changed---")
        except:
            print("Invalid amount or Product not found")

    #  To change products Quantity
    def change_product_quantity(self):
        print("\t\t---Changing Product Quantity---")
        try:
            counter = 0
            product_name = Product(input("Product Name: ").capitalize())
            new_quantity = int(input("The new quantity will be: "))
            for products in inventory.inventory_raw.values():
                for product, info in products.items():
                    if product == product_name:
                        counter += 1
                        info[1] = new_quantity
            if counter == 0:
                print("Invalid amount or Product not found")
            else:
                print("---Quantity Changed---")
        except:
            print("Invalid amount or Product not found")

    # To change Product ID
    def change_product_id(self):
        print("\t\t---Changing Product ID---")
        try:
            counter = 0
            product_name = Product(input("Product Name: ").capitalize())
            new_Id = int(input("The new ID will be: "))
            for products in inventory.inventory_raw.values():
                for product, info in products.items():
                    if product == product_name:
                        counter += 1
                        info[0] = new_Id
            if counter == 0:
                print("Invalid amount or Product not found")
            else:
                print("---ID Changed---")
        except:
            print("Invalid amount or Product not found")
     
inventory = Inventory()          

# LISTING ALL CATAGORIES
def list_all_catagories():
    print("\t\t---Listing All Catagories---")
    try:
        if inventory.inventory_raw != "":
            print("All Catagories Listed: ")
            for count, catagories in enumerate(inventory.inventory_raw, 1):
                print("{}. {}".format(count, catagories))
        else:
            print("No Catagories Created")
    except:
        print("No Catagory Created")
    finally:
        print("---Search Complete---")

# lIST ALL PRODUCTS IN CATAGORY
def list_all_products_in_catagory():
    print("\t\t--Listing Products in Catagory--")
    catagory = Catagory(input("Catagory to Search: ").capitalize())
    if catagory.name not in inventory.inventory_raw.keys():
        print("No such catagory\n---Search Complete---")
    else:
        try:
            print("Products in {}:".format(catagory.name))
            for count, products in enumerate(inventory.inventory_raw[catagory.name].keys(), 1):
                print("{}. {}".format(count, products))
        except:
            print("No Products in Catagory")
        finally:
            print("---Search Complete---")

# LIST ALL PRODUCT INFO THROUGH NAME
def search_product_through_name():
    print("\t\t--Searching Product through Name--")
    catagory = Catagory(input("Catagory Name(Optional): ").capitalize())
    product = Product(input("Product Name: ").capitalize())
    counter = 0
    try:
        if catagory.name == "" and product.name == "":
            print("Please fill in at least the Product name")
        elif catagory.name != "":
            product_info = inventory.inventory_raw[catagory.name][product.name]
            print("ID: {}\nQuantity: {}\nPrice: ${}".format(product_info[0], product_info[1], product_info[2]))
        elif catagory.name == "":
            for products in inventory.inventory_raw.values():
                if product.name in products:
                    counter+=1
                    info = products[product.name]
                    print("ID: {}\nQuantity: {}\nPrice: ${}".format(info[0], info[1], info[2]))
            if counter == 0:
                print("No results matched.")
    except: 
        print("No results matched.")
    finally:
        print("\t\t---Seach Complete---")

# LIST ALL PRODUCT INFO THROUGH ID
def search_product_through_ID():
    print("\t\t---Search Product through ID---")
    try:
        counter = 0
        product_id = Product(id = input("ID Number:"))
        if product_id.id == "":
            return
        else:
            for product in inventory.inventory_raw.values():
                for product_name, info in product.items():
                    if info[0] == int(product_id.id):
                        counter += 1
                        print("\nProduct: {}\nID: {}\nQuantity: {}\nPrice: ${}".format(product_name, info[0], info[1], info[2]))
            if counter == 0:
                print("No results matched")
    except:
        print("Not A valid ID")
    finally:
        print("\t\t---Seach Complete---")

# TOTAL INVENTORY PRICE
def print_total_inventory_price():
    print("\t\t---Total Inventory Price---")
    product_price=0
    for products in inventory.inventory_raw.values():
        for info in products.values():
            product_price+=info[2]
    print("${}".format(product_price))

# LIST THE WHOLE INVENTORY
def list_all_inventory():
    print("\t\t---Listing All Inventory---")
    try:
        for catagory, products in inventory.inventory_raw.items():
            print("Catagory-{}".format(catagory))
            for product, info in products.items():
                print(" {}:\n   ID: {}\n   Quantity: {}\n   Price: ${}".format(product, info[0], info[1], info[2]))
    except:
        print("--The Inventory is empty--")

#  The Entry Screen
def main_menu():
    while True:
        print("\n\n\n\t\t---Welcome---\n1. Enter\n2. Program Info\n3. Quit")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3):
                return user_input
            print("invalid")
        except:
            print("invalid")

#  The Main Screen
def sub_menu():
    while True:
        print("\n\n\n\t\t---Inventory Management---\n1. Search\n2. Add/Remove Products\n3. Add/Remove Catagories\n4. Total Inventory Price\n\
5. List Full Inventory\n6. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3,4,5,6):
                return user_input
            print("invalid")
        except:
            print("invalid")

# Search Screen
def sub_menuOne():
    while True:
        print("\n\n\n\t\t---Search Product---\n1. Search Product through ID \n2. Search Product through name \n3. Search Catagory \n4. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3,4):
                return user_input
            print("invalid")
        except:
            print("invalid")

# Search sreen for searching the catagories
def sub_menuOneCata():
    while True:
        print("\n\n\n\t\t---Catagory Search---\n1. List all Catagories \n2. List products within a Catagory \n3. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3):
                return user_input
            print("invalid")
        except:
            print("invalid")

# Add/Remove products screen
def sub_menuTwo():
    while True:
        print("\n\n\n\t\t---Add/Remove Products---\n1. Create a new Product in a new Catagory\n2. Add a new product in a Existing Catagory\n\
3. Delete a Product in a Exisiting catagory\n4. Change Product's Info\n5. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3,4,5):
                return user_input
            print("invalid")
        except:
            print("invalid")

# Change products info screen
def sub_menuTwo_infochange():
    while True:
        print("\n\n\n\t\t---Change Product Information---\n1. Change Product's Price\n2. Change Products Quantity\n\
3. Change Products ID\n4. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3,4,5):
                return user_input
            print("invalid")
        except:
            print("invalid")

# Add/Remove catagories screen
def sub_menuthree():
    while True:
        print("\n\n\n\t\t---Add/Remove Catagory---\n1. Create a new Catagory and a new Product\n2. Delete a Catagory\n3. Go Back")
        try:
            user_input=int(input("Navigate to (Enter the index): "))
            if user_input in (1,2,3,4):
                return user_input
            print("invalid")
        except:
            print("invalid")

def info():
    print("Place Holder")

# Control flow
def enter():
    input("Back")

#  Main app test: 1
inventory = Inventory()
# Main screen
while True:
    mainMenu = main_menu()
    if mainMenu == 1:
        # screen for "Enter"
        while True:
            subMenu = sub_menu()
            # screen for "Search"
            if subMenu == 1:
                while True:
                    subMenuOne = sub_menuOne()
                    # search product through ID
                    if  subMenuOne == 1:
                        search_product_through_ID()
                        enter()
                    # Search product through name
                    elif subMenuOne == 2:
                        search_product_through_name()
                        enter()
                    # Search catagory
                    elif subMenuOne == 3:
                        while True:
                            subMenuOneCata = sub_menuOneCata()
                            # List All Catagories
                            if subMenuOneCata == 1:
                                list_all_catagories()
                                enter()
                            # All Products in Catagories
                            elif subMenuOneCata == 2:
                                list_all_products_in_catagory()
                                enter()
                            # Go Back
                            elif subMenuOneCata ==3:
                                break
                    # Back key
                    elif subMenuOne == 4:
                        break
            # Screen for "add/remove" products
            elif subMenu == 2:
                while True:
                    subMenuTwo = sub_menuTwo()
                    # Create a new product and new catagory
                    if subMenuTwo == 1:
                        inventory.add_to_inventory_new_catagory()
                        enter()
                    # Add a new product ot existing catagory
                    elif subMenuTwo == 2:
                        inventory.add_product_to_existing_catagory()
                        enter()
                    # Delete a product in a existing catagory
                    elif subMenuTwo == 3:
                        inventory.delete_products_inside_catagories()
                        enter()
                    # Change Products Info
                    elif subMenuTwo == 4:
                        while True:
                            infoChange = sub_menuTwo_infochange()
                            # Change ID
                            if infoChange == 1:
                                inventory.change_product_price()
                                enter()
                            # Change Quantity
                            elif infoChange == 2:
                                inventory.change_product_quantity()
                                enter()
                            # Change Price
                            elif infoChange == 3:
                                inventory.change_product_id()
                                enter()
                            # Go back
                            elif infoChange == 4:
                                break
                    # Go back
                    elif subMenuTwo == 5:
                        break
            # Screen for "add/remove catagories"
            elif subMenu == 3:
                while True:
                    subMenuThree = sub_menuthree()
                    # Create a new Catagory and a new product
                    if subMenuThree == 1:
                        inventory.add_to_inventory_new_catagory()
                        enter()
                    # Delete a existing catagory
                    elif subMenuThree == 2:
                        list_all_catagories()
                        inventory.deleting_a_catagory()
                        enter()
                    # Go back
                    elif subMenuThree == 3:
                        break
            # Screen for "Total inventory price"
            elif subMenu == 4:
                print_total_inventory_price()
                enter()
            # Screen for "Full inventory list"
            elif subMenu == 5:
                list_all_inventory()
                enter()
            # Back key to go back to sub menu
            elif subMenu == 6:
                break
    # Pogram Info 
    elif mainMenu == 2:
        pass
        break
    # Quit Program
    elif mainMenu == 3:
        print("Thank you!")
        break