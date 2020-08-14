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
        self.inventoryLog = {}
        self.idLog = []

    # THIS IS FOR CREATING A NEW CATAGORY AND ADDING NEW PRODUCTS
    def add_to_inventory_new_category(self):
        print("\t\t---Creating a new Catagory with Product---")
        try:
            category=Catagory(input("Catagory Name to create: ").capitalize())
            if category.name in self.inventoryLog.keys():
                print("--Error, {} has already been created--".format(category.name))
            else:
                product=Product(input('Product Name: ').capitalize(), int(input("ID: ")),\
                int(input("Quantity: ")), float(input("Price: $")))
                if product.id in self.idLog:
                    print("--A item already exists with that id--")
                else:
                    self.inventoryLog.update({category.name : {product.name : [product.id, product.quantity, product.price]}})
                    self.idLog.append(product.id)
                    print("--{} added to {}--".format(product.name, category.name))
        except:
            print("--Error--\n--Make sure to fill in all info correctly--")

    # HELPER FUNCTION TO LIST ALL THE CATEGORIES
    def inventory_keys(self):
            def yield_keys(dictionary):
                for keys in dictionary:
                    yield "- {}".format(keys) 
            for category_key in yield_keys(self.inventoryLog):
                print(category_key)

    #ASKS FOR A NEW PRODUCT TO BE ADDED INTO THE EXISTING CATAGORY
    def add_product_to_existing_category(self):
        print("\t\t---Adding products to existing Catagories---")
        self.inventory_keys()
        # asks for the category
        try:
            category=Catagory(input("Catagory Name: ").capitalize())
            if category.name not in self.inventoryLog.keys():
                print("--Error: {} has not been created--".format(category.name))
            else:
                product=Product(input('Product Name: ').capitalize(), int(input("ID: ")),\
                int(input("Quantity: ")), float(input("Price: $")))
                if product.name in self.inventoryLog[category.name]:
                    print("--Error: Item already in the given Catagory--")
                elif product.id in self.idLog:
                    print("--A item already exists with that id--")
                else:
                    self.inventoryLog[category.name][product.name] = [product.id, product.quantity, product.price]
                    self.idLog.append(product.id)
                    print("--{} added to {}--".format(product.name, category.name))
        except:
            print("---Make sure to fill in all info correctly---")
    
    # THIS IS TO DELETE A CATAGORY
    def deleting_a_category(self):
        print("\t\t---Deleting A Catagory---")
    
        self.inventory_keys()
        category=Catagory(input("Catagory Name to delete: ").capitalize())
        if category.name in self.inventoryLog:
            print('--Catagory deleted--')
            del self.inventoryLog[category.name]
        else:
            print('---Catagory not found---')
   
    # TO DELETE PRODUCTS INSIDE CATAGORIES
    def delete_products_inside_catagories(self):
        print("\t\t---Deleting Products inside Catagories---")

        self.inventory_keys()

        # Ask For Catagory Name:
        category=Catagory(input("Catagory Name to search: ").capitalize())
        if category.name not in self.inventoryLog.keys():
            print("--Error: {} does not exist--".format(category.name))
        else:
            product=Product(input('Product Name: ').capitalize())
            try:
                del self.inventoryLog[category.name][product.name]
                print('--deleted {}--'.format(product.name))
            except:
                    print("---No product found in the given Catagory---")
    
    #Check if the category exists
    def categoryCheck(self, categoryName):
        if self.inventoryLog == "":
            print("The inventory is empty")
            return False
        elif categoryName not in self.inventoryLog:
            print("--{} does not exist--".format(categoryName))
            return False
        else:
            return True
    #Check if the product exists
    def productCheck(self, productName, categoryName):
        if productName not in self.inventoryLog[categoryName]:
            print("--{} does not exist in {}--".format(productName, categoryName))
            return False
        else:
            return True

    # TO CHANGE THE PRODUCT PRICE
    def change_product_price(self):
        print("\t\t---Changing Product Price---")
        self.inventory_keys()
        category_name = input("Catagory Name to search: ").capitalize()
        if self.categoryCheck(category_name):
            product_name = input("Product Name: ").capitalize()
            if self.productCheck(product_name, category_name):
                try:
                    new_price = float(input("The new price will be: $"))    
                    self.inventoryLog[category_name][product_name][2] = new_price
                    print("--{}'s price changed--".format(product_name.capitalize()))
                except:
                    print("--Error. Invalid price--")

    #  TO CHANGE THE PRODUCT QUANTITY
    def change_product_quantity(self):
        print("\t\t---Changing Product Quantity---")
        self.inventory_keys()
        category_name = input("Catagory Name to search: ").capitalize()
        if self.categoryCheck(category_name):
            product_name = input("Product Name: ").capitalize()
            if self.productCheck(product_name, category_name):
                try:
                    new_quantity = int(input("The new quantity will be: "))    
                    self.inventoryLog[category_name][product_name][1] = new_quantity
                    print("--{}'s quantity changed--".format(product_name.capitalize()))
                except:
                    print("--Error. Invalid quantity--")

    # To change Product ID
    def change_product_id(self):
        print("\t\t---Changing Product ID---")
        self.inventory_keys()
        category_name = input("Catagory Name to search: ").capitalize()
        if self.categoryCheck(category_name):
            product_name = input("Product Name: ").capitalize()
            if self.productCheck(product_name, category_name):
                try:
                    new_id = int(input("The new Id will be: ")) 
                    if new_id not in self.idLog:   
                        self.inventoryLog[category_name][product_name][0] = new_id
                        print("--{}'s id changed--".format(product_name.capitalize()))
                    else:
                        print("--Error. Id already exists.")
                except:
                    print("--Error. Invalid Id--")


#
# END OF CLASS
#         

# LISTING ALL CATAGORIES
def list_all_catagories(inventory):
    print("\t\t---Listing All Catagories---")
    try:
        if inventory.inventoryLog != "":
            print("All Catagories Listed: ")
            for count, catagories in enumerate(inventory.inventoryLog, 1):
                print("{}. {}".format(count, catagories))
        else:
            print("No Catagories Created")
    except:
        print("No Catagory Created")
    finally:
        print("---Search Complete---")

# lIST ALL PRODUCTS IN CATAGORY
def list_all_products_in_category(inventory):
    print("\t\t--Listing Products in Catagory--")
    category = Catagory(input("Catagory to Search: ").capitalize())
    if category.name not in inventory.inventoryLog.keys():
        print("No such category\n---Search Complete---")
    else:
        try:
            print("Products in {}:".format(category.name))
            for count, products in enumerate(inventory.inventoryLog[category.name].keys(), 1):
                print("{}. {}".format(count, products))
        except:
            print("No Products in Catagory")
        finally:
            print("---Search Complete---")

# LIST ALL PRODUCT INFO THROUGH NAME
def search_product_through_name(inventory):
    print("\t\t--Searching Product through Name--")
    category = Catagory(input("Catagory Name(Optional): ").capitalize())
    product = Product(input("Product Name: ").capitalize())
    counter = 0
    try:
        if category.name == "" and product.name == "":
            print("Please fill in at least the Product name")
        elif category.name != "":
            product_info = inventory.inventoryLog[category.name][product.name]
            print("ID: {}\nQuantity: {}\nPrice: ${}".format(product_info[0], product_info[1], product_info[2]))
        elif category.name == "":
            for products in inventory.inventoryLog.values():
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
def search_product_through_ID(inventory):
    print("\t\t---Search Product through ID---")
    try:
        counter = 0
        product_id = Product(id = input("ID Number:"))
        if product_id.id == "":
            return
        else:
            for product in inventory.inventoryLog.values():
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
def print_total_inventory_price(inventory):
    print("\t\t---Total Inventory Price---")
    product_price=0
    for products in inventory.inventoryLog.values():
        for info in products.values():
            product_price+=(info[2]*info[1])
    print("${}".format(product_price))

# LIST THE WHOLE INVENTORY
def list_all_inventory(inventory):
    print("\t\t---Listing All Inventory---")
    try:
        for category, products in inventory.inventoryLog.items():
            print("Catagory-{}".format(category))
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
3. Delete a Product in a Exisiting category\n4. Change Product's Info\n5. Go Back")
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

def main():
    initInventory = Inventory()
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
                            search_product_through_ID(initInventory)
                            enter()
                        # Search product through name
                        elif subMenuOne == 2:
                            search_product_through_name(initInventory)
                            enter()
                        # Search category
                        elif subMenuOne == 3:
                            while True:
                                subMenuOneCata = sub_menuOneCata()
                                # List All Catagories
                                if subMenuOneCata == 1:
                                    list_all_catagories(initInventory)
                                    enter()
                                # All Products in Catagories
                                elif subMenuOneCata == 2:
                                    list_all_products_in_category(initInventory)
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
                        # Create a new product and new category
                        if subMenuTwo == 1:
                            initInventory.add_to_inventory_new_category()
                            enter()
                        # Add a new product ot existing category
                        elif subMenuTwo == 2:
                            initInventory.add_product_to_existing_category()
                            enter()
                        # Delete a product in a existing category
                        elif subMenuTwo == 3:
                            initInventory.delete_products_inside_catagories()
                            enter()
                        # Change Products Info
                        elif subMenuTwo == 4:
                            while True:
                                infoChange = sub_menuTwo_infochange()
                                # Change ID
                                if infoChange == 1:
                                    initInventory.change_product_price()
                                    enter()
                                # Change Quantity
                                elif infoChange == 2:
                                    initInventory.change_product_quantity()
                                    enter()
                                # Change Price
                                elif infoChange == 3:
                                    initInventory.change_product_id()
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
                            initInventory.add_to_inventory_new_category()
                            enter()
                        # Delete a existing category
                        elif subMenuThree == 2:
                            list_all_catagories(initInventory)
                            initInventory.deleting_a_category()
                            enter()
                        # Go back
                        elif subMenuThree == 3:
                            break
                # Screen for "Total inventory price"
                elif subMenu == 4:
                    print_total_inventory_price(initInventory)
                    enter()
                # Screen for "Full inventory list"
                elif subMenu == 5:
                    list_all_inventory(initInventory)
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

if __name__ == "__main__":
    main()