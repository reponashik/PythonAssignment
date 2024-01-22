import json

'''
Activity 1: Implementing a simple eCommerce system.
In summary, this program will enable users to 
    -add 
    -remove
    -show a summary
    -export content to JSON format. 
For all products 

'''
#1.1 Start

''' 
Creating instances via the keywork "self" for 
all required attributes. 
Self enables the access to attributes and methods of the 
classes in Python. 

def __init__ is the constructor for the class called "Product"
This method is called when objects from the class in question (Product) need to be created.
and it also enables to initialize the attributes of the class
For example name, price, quantity, brand and EAN are attributes of the 
class Product

'''
class Product:
    def __init__(self, name, price, quantity, brand, ean):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
        self.ean = ean
        
    def to_json(self):
        return {
                "name": self.name,
                "price": self.price,
                "quantity": self.quantity,
                "brand": self.brand,
                "ean": self.ean
        } 

'''
to_json() is a method that is returning using the keyword return 
a JSON formatted representation of the product 
This function returns a list of key-value pairs describing the product attributes

Here, a dictionary is returned, emulating an identical JSON format
json.dumps() function has been considered, however for the logic 
of this program, accessing key value pairs is easier than
working with json string (which is what json.dumps() returns)

''' 
   
''' 
Creating three subclasses.
    -Clothing : with attributes size and material
    -Food : with attributes expiry date, gluten free (yes or no), suitable for vegans (yes or no)
    -One additional class of choice: Book (attributes specified in the sub class definition)
    
'''

class Clothing(Product): #takes Product as argument
    #init method or constructor
    def __init__(self, name, price, quantity, brand, ean, size, material):
        #using keyword super to have access to the attributes and methods of the constructor class of Product
        super().__init__(name, price, quantity, brand, ean)
        #initialising class Clothing attributes
        self.size = size #size instance of the class
        self.material = material #material instance of the class
    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "brand": self.brand,
            "ean": self.ean,
            "size": self.size, #clothing specific attribute instance
            "material": self.material #clothing specific attribute instance
        }

#Under the Clothing class, the to_json() function 
#needs to be tailored accordingly on the Clothing Class attributes 
#as shown in the method definition below.

#Food subclass: 
#    additional attributes are 
#    expiry date
#    gluten free
#    suitable for vegans 
#    expiry date
    

class Food(Product):
    def __init__(self, name, price, quantity, brand, ean, expiry_date, gluten_free, suitable_for_vegans):
        #using keyword super to have access to the attributes and methods of the constructor class of Product
        super().__init__(name, price, quantity, brand, ean) 
        #initialising class Food attributes
        self.expiry_date = expiry_date #food specific attribute instance
        self.gluten_free = gluten_free #food specific attribute instance
        self.suitable_for_vegans = suitable_for_vegans #food specific attribute instance
   
    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "brand": self.brand,
            "ean": self.ean,
            "expiry_date": self.expiry_date, #food specific attribute instance
            "gluten_free": self.gluten_free, #food specific attribute instance
            "suitable_for_vegans": self.suitable_for_vegans #food specific attribute instance
        }

#Under the Food class, the to_json() function 
#needs to be tailored accordingly on the Food Class attributes 
#as shown in the method definition below.

#Book subclass: 
#    additional attributes are: 
#    author
#    isbn
#    pages
    
class Book(Product):
    def __init__(self, name, price, quantity, brand, ean, author, isbn, pages):
        #using keyword super to have access to the attributes and methods of the constructor class of Product
        super().__init__(name, price, quantity, brand, ean) 
        #initialising class Book attributes
        self.author = author
        self.isbn = isbn
        self.pages = pages
   
    def to_json(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "brand": self.brand,
            "ean": self.ean,
            "author": self.author, #book specific attribute instance
            "isbn": self.isbn, #book specific attribute instance
            "pages": self.pages #book specific attribute instance
        }

#Under the Book class, the to_json() function 
#needs to be tailored depending on the Book Class attributes 
#as shown in the method definition below.


#1.1 End 

#-------------------------------------------------------------------------------------------------------------

#1.2 Start
'''
This part contains the implementation of a Shopping Cart
which is a container of products during a shopping session

'''

#Defining ShoppingCart Class
class ShoppingCart:
    def __init__(self): #Defining ShoppingCart constructor class
        #{} symbol to initialize dictionary
        self.products = {} 
    '''
    In the section below, all the ShoppingCart Class 
    methods will be defined: 
        addProduct() 
        removeProduct()
        changeProductQuantity()
        getContents()
        
    '''
    '''
    addProduct() function
    addProduct() takes self and product as the arguments
    self is the first argument to be passed in any instance method
    the second argument is of course the product that the user wishes to add.
    
    '''
    def addProduct(self, product): #is product an object? 
        #if statement below is checking if and else block below is checking if
        #the EAN of the product that user wishes to add already exists. 
        if product.ean in self.products:
        #keyword "in" ...
            self.products[product.ean].quantity += product.quantity
        else:
            self.products[product.ean] = product
    '''
    removeProduct() function
    removeProduct() takes self and product as the arguments
    self is the first argument to be passed in any instance method
    the second argument is of course the product that the user wishes to delete.
    
    '''
    def removeProduct(self, ean):
        #keyword "del" removes key-value pairs from a dictionary
        del self.products[ean]

    '''
    changeQuantityProduct() function
    takes self, product and quantity
    self is the first argument to be passed in any instance method
    the second argument is the product the user wishes to change the quantity of.
    quantity is the parameter of the new quantity that the user wishes to change their product to. 
    
    '''
    def changeProductQuantity(self, product, quantity):
        if product.ean in self.products:
            self.products[product.ean].quantity = quantity
        #in keyword checks if it is present in the dictionary. 
    
    #getContents() function
    def getContents(self):
        #return self.products simply returns the key value pair dictionary of all 
        #the products present in the cart
        return self.products

#this variable shopping_cart is important as it is being initialised as an object 
#of type ShoppingCart(), which takes shopping_cart as an argument and makes it accessible in the
#form of a dictionary
#shopping_cart will be relevant in upcoming sections - it is used predominantly in 
#handle_add_product() and handle_remove_product() 

shopping_cart = ShoppingCart()

'''
This section contains a number of helper function which rectify that the user has 
entered the correct input, input data type and handles the program graciously without 
causing an error.

In the following blocks of code, try/except blocks are being 
used to catch and handle errors
The statements that follow the "except" statement is the program's 
way of responding to any exceptions in the preceding "try" clause

'''
#try/catch helper function for correct float input
def input_float(prompt):
    #prompt is the name for the argument related to the user input
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please Enter a Valid Price")
            
#try/catch helper function for correct integer input
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Value should be an integer")
            
#try/catch helper function for correct format of the EAN
def input_ean():
    while True:
        ean = input("Insert the EAN code: ")
        #if statement below checking the correct charachteristics of EAN format
        #the if statement is also checking that the EAN is unique by executing a 
        #boolean check on whether it is already part of any of the keys of the existing products
        if ean.isdigit() and len(ean) == 13 and not (ean in shopping_cart.products.keys()):
            return ean
        else:
            print("EAN code should be 13 digits and unique")

#helper function to convert prompt into a boolean
#yn means yes/no: meaning behind variable name choice. 
#returns True if prompt (input) is "y" and False if prompt is "f"
def input_yn(prompt):
    while True:
        answer = input(prompt)
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter y or n")

#1.2 End

#------------------------------------------------------------------------------------------------

#1.3 Start
#Doing Some Shopping 
'''
handle_add_product() function
enables the main program to add a new item. 
at the beginning of this function, there is a series of input functions to collect
the data from the user. 
Depending on the input, it is double-checked using the input helper functions defined 
in the previous section, for example: ean = input_ean() is checking if the EAN entered 
is valid.

The program then enters the first if statement, dedicated to product type Clothing. 
Specifically, here the size and material of the Clothing are requested for input
then the program proceeds into creating an object of type Clothing with the data entered.

The program then enters the elif statement, dedicated to product type Food. 
Specifically, here the expiry date, if it is gluten free and if it is suitable for vegans
is requested for input as part of the Food class.
then the program proceeds into creating an object of type Food with the data entered.

The program then enters the second elif statement, dedicated to product type Book. 
Specifically, here the author, isbn and pages of the Book class are requested for input 
then the program proceeds into creating an object of type Book with the data entered.

The else statement is enabling a product to be inserted that is not part of the types 
that the program is familiar with (Food, Clothing and Book)

All inputs are validated and checked with lower/upper case.

'''
def handle_add_product():
    #data about the product collected and validated from input
    print("Adding a new product:")
    product_type = input("Insert its type: ")
    name = input("Insert its name: ")
    price = input_float("Insert its price (£): ")
    quantity = input_int("Insert its quantity: ")
    brand = input("Insert its brand: ")
    ean = input_ean()
    #end of data collection and validation sub section. 
    if product_type.lower() == "clothing":
        size = input("Insert its size: ")
        material = input("Insert its material: ")
        product = Clothing(name, price, quantity, brand, ean, size, material)
    elif product_type.lower() == "food":
        #expiry_date should be a date object
        expiry_date = input("Insert its expiry date (dd/mm/yyyy): ")
        gluten_free = input_yn("Is it gluten free? (y/n): ")
        suitable_for_vegans = input_yn("Is it suitable for vegans? (y/n): ")
        product = Food(name, price, quantity, brand, ean, expiry_date, gluten_free, suitable_for_vegans)
    elif product_type.lower() == "book":
        author = input("Insert its author: ")
        isbn = input("Insert its ISBN: ")
        #note: I am aware that ISBN has its own format which is universal with a specific size
        #for this coursework submission, the conventional ISBN rules have NOT been considered
        pages = input_int("Insert its number of pages: ")
        product = Book(name, price, quantity, brand, ean, author, isbn, pages)
    else:
        product = Product(name, price, quantity, brand, ean)
    shopping_cart.addProduct(product) #calling addProduct
    print(f"The product {product.name} has been added to the cart.")
    print(f"The cart contains {len(shopping_cart.getContents())} products.")
    #printing the number of items in the cart

'''
print_help() function
Formatting derives from listing 4. 
Appears if user enters command "H" for Help 
Shows using a print() function all the commands available

'''
def print_help():
    print("""
The program supports the following commands:
    [A] - Add a new product to the cart
    [R] - Remove a product from the cart
    [S] - Print a summary of the cart
    [Q] - Change the quantity of a product
    [E] - Export a JSON version of the cart
    [T] - Terminate the program
    [H] - List the supported commands
""")

'''
handle_remove_product() function
Firstly, shows the user a summary of all the products and quantities
of the existing products in the cart.
Then prompts the user to input the name of the element that the user
wishes to remove. 
an if statement checks if the name exists, if True, removeProduct 
is called taking as the argument the ean of the product to be 
deleted and removes it.

'''
def handle_remove_product():
    print("The following items are in the cart: ")
    #in Python, when we are not interested in some values returned 
    #by a function, we can use the underscore "_" in place
    #of variable names. In this case, it is not relevant how many 
    #times the loop runs, but that it iterates for every element in 
    #the dictionary called shopping_cart to show its content.
    for _, product in shopping_cart.getContents().items():
        print(f"{product.name} - {product.quantity}")
    name = input("Insert the name of the product to remove: ")
    #for _ is effectively an alternative to for i in range...
    for _, product in shopping_cart.getContents().items():
        if product.name == name:
            shopping_cart.removeProduct(product.ean)#removeProduct called from previous section.
            print(f"The product {product.name} has been removed from the cart.")
            return
    #if the check fails, print the product is not there (no association with the names)
    print("The product is not in the cart.")

'''
print_shopping_cart() function
Firstly, this function creates a counter using enumerate()
enumerate() is explained in in-line comments. 
We iterate in shopping_cart by iterating over it and storing it 
in a variable called product, which is then printed to show the cart.
The second part of this program contains a for loop to do the summation 
of the prices of all items

'''
def print_shopping_cart():
    print("This is the total of the expenses: ")
    #enumerate() is used to get a counter in a loop and to display it.
    #it is efficient because you can obtain the counter and the value from
    #the iterable as well. 
    
    #here, a single-liner for loop is being used
    #the way this reads is, for each EAN value in shopping_cart dictionary, obtain its index
    #by accessing its key. 
    #the iteration is being saved in a variable called product
    for index, ean in enumerate(shopping_cart.getContents().keys()):
        product = shopping_cart.getContents()[ean] #calling getContents()
        print(f"{index + 1} - {product.quantity} * {product.name} = £{product.price * product.quantity}")
    
    total = 0 #total price set to 0 before entering for loop
    #for loop to calculate the total number of expenses by accessing product.price
    #and do the summation of all the prices.
    for ean in shopping_cart.getContents().keys():
        product = shopping_cart.getContents()[ean]
        total += product.price * product.quantity
    #using templating to get the value of the variable total in the print
    print(f"Total: £{total}")

'''
handle_change_product_quantity() function 
again, for _ is used to iterate every element in shopping cart
the names of all products are printed first to show how many of each product
exist in the shopping cart using the getContents() function
in the second for loop of the function, if product exists, the program will
ask the user to enter the number of the new quantity, and using the 
changeProductQuantity() function, the product integer will be updated.

'''
def handle_change_product_quantity():
    print("The following items are in the cart: ")
    for _, product in shopping_cart.getContents().items():
        print(f"{product.name} - {product.quantity}")
    name = input("Insert the name of the product to change quantity: ")
    for _, product in shopping_cart.getContents().items(): #iterates over shopping_cart
        if product.name == name: #checking if product exists
            quantity = input_int("Insert the new quantity: ")
            shopping_cart.changeProductQuantity(product, quantity)
            print(f"The quantity of {product.name} has been changed to {quantity}.")
            return
    #print statement in case product is not in the cart
    print("The product is not in the cart.")
'''
print_json_dump() function 
this function iterates again over the content of shopping_cart, and uses 
a block of if and else statements and templating to send the content of the
shopping cart to the to_json() function defined in the first section of this 
program.

'''
def print_json_dump():
    print("The following JSON form is generated: ")
    print("[")
    contents = shopping_cart.getContents()
    for index, ean in enumerate(contents.keys()):
        if index != len(contents) - 1:
            print(f"\t{contents[ean].to_json()},")
        else:
            print(f"\t{contents[ean].to_json()}")
    print("]")

#------------------------------------------------------------------------

#main program
#this is the main While loop that keeps running that acts as the central guiding menu 
#of this program
#it contains a block of if, elif and else stataments containing all the
#commands - denoted by variable "c" to choose the options to navigate
#through this eCommerce system

print("The program has started.")
while True:
    c = input("Insert the next command: ")
    if c == "A":
        handle_add_product()
    elif c == "R":
        handle_remove_product()
    elif c == "S":
        print_shopping_cart()
    elif c == "Q":
        handle_change_product_quantity()
    elif c == "E":
        print_json_dump()
    elif c == "T":
        break
    elif c == "H":
        print_help()
    else:
        print("Command not recognised. Please try again")
#terminate the program
print( "Goodbye.")
