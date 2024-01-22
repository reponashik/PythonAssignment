#importing json, csv libraries required for this task
import json 
import csv

'''
Activity 3 
reading/writing files 
medals.csv
    -each country as an object
    -defines functionalities for these objects
    -creates an interface through which users can query the information in these objects
    
'''
#3.1 Start

'''
CountryMedals class
defining CountryMedals class with following attributes: 
    -name
    -no. of gold medals
    -no. of silver medals
    -no. of bronze medals
    -total no. of medals

this class will also comprise of methods:
    -to_json(): which returns a JSON representation of the object in key-value format
    -get_medals(medal_type): medal_type would be either gold,silver or bronze and return corresponding no. of 
    medals
    -print_summary(): summary of medals received by the country
    -compare(country_2): shows a comparision of the medals received by two countries (format in the specification)
    
'''
class CountryMedals:
    #defining the constructor class of CountryMedals
    def __init__(self, name, gold, silver, bronze):
        #keyword self enables the access to attributes and methods of the classes in Python. 
        self.name = name #name attribute definition
        self.gold = gold #gold attribute definition
        self.silver = silver #silver attribute definition
        self.bronze = bronze #bronze attribute definition
    
    #the to_json() function
    def to_json(self):
        #returns the object's attributes as key value pairs in the form of a dictionary. 
        #just like in shopping.py, using a dictionary has been preferred over json.dumps()
        #this is because accessing a dictionary is more practical than accessing a json string
        return {
            self.name:
                {
                    'gold': self.gold,
                    'silver': self.silver,
                    'bronze': self.bronze,
                    'total': self.gold + self.silver + self.bronze #summing all the medals
                }}
    
    #get_medals() function
    #this method uses a block of if,elif,else statements to check if medal type is any of the 
    #options between gold, silver or bronze, and then returns as per specification
    #the total is also returned in a similar way
    def get_medals(self, medal_type):
        if medal_type == 'gold':
            return self.gold
        elif medal_type == 'silver':
            return self.silver
        elif medal_type == 'bronze':
            return self.bronze
        elif medal_type == 'total':
            return self.gold + self.silver + self.bronze
        else:
            return None
        
    #print_summary() function
    #this function uses templating in the print function and displays the country name and corresponding
    #medal names and quantities by accessing the corresponding objects i.e. self.gold
    def print_summary(self):
        print(f"{self.name} received {self.gold + self.silver + self.bronze} medals in total; {self.gold} gold, {self.silver} silver, and {self.bronze} bronze")
    
    '''
    compare(country_2) function
    this function comprises of 4 sets of if,elif,else blocks 
    the first 3 blocks compare country no.1 with country no.2 for each medal type
    the fourth conditional block compares the total no. of medals for country no.1 and country no.2
    across this method, the print function again uses templating to access different object names to display
    the comparative text
    
    '''
    def compare(self, country_2):
    #the conditional block below compares country no.1 gold medals with country no.2 gold medals 
    #there is a condition set for all possibilities, even the case in which the no. of medals is the same
        print(
            f"Medals comparison between '{self.name}' and '{country_2.name}':")
        if self.gold > country_2.gold:
            print(f"- {self.name} received {self.gold} gold medal(s), {self.gold - country_2.gold} more than {country_2.name}, which received {country_2.gold}.")
        elif self.gold < country_2.gold:
            print(f"- {self.name} received {self.gold} gold medal(s), {country_2.gold - self.gold} fewer than {country_2.name}, which received {country_2.gold}.")
        else:
            print(
                f"- Both {self.name} and {country_2.name} received {country_2.gold} gold medal(s).")
            
    #the conditional block below compares country no.1 silver medals with country no.2 silver medals 
    #there is a condition set for all possibilities, even the case in which the no. of medals is the same
        if self.silver > country_2.silver:
            print(f"- {self.name} received {self.silver} silver medal(s), {self.silver - country_2.silver} more than {country_2.name}, which received {country_2.silver}.")
        elif self.silver < country_2.silver:
            print(f"- {self.name} received {self.silver} silver medal(s), {country_2.silver - self.silver} fewer than {country_2.name}, which received {country_2.silver}.")
        else:
            print(
                f"- Both {self.name} and {country_2.name} received {country_2.silver} silver medal(s).")

    #the conditional block below compares country no.1 bronze medals with country no.2 bronze medals 
    #there is a condition set for all possibilities, even the case in which the no. of medals is the same
        if self.bronze > country_2.bronze:
            print(f"- {self.name} received {self.bronze} bronze medal(s), {self.bronze - country_2.bronze} more than {country_2.name}, which received {country_2.bronze}.")
        elif self.bronze < country_2.bronze:
            print(f"- {self.name} received {self.bronze} bronze medal(s), {country_2.bronze - self.bronze} fewer than {country_2.name}, which received {country_2.bronze}.")
        else:
            print(
                f"- Both {self.name} and {country_2.name} received {country_2.bronze} bronze medal(s).")

    #the conditional block below compares the total no. of medals of country no.1 and country no.2
    #there is a condition set for all possibilities, even the case in which the no. of medals is the same
        self_total = self.gold + self.silver + self.bronze
        country_2_total = country_2.gold + country_2.silver + country_2.bronze
        print()
        if self_total > country_2_total:
            print(
                f"Overall, {self.name} received {self_total} medals, {self_total - country_2_total} more than {country_2.name}, which received {country_2_total}.")
        elif self_total < country_2_total:
            print(
                f"Overall, {self.name} received {self_total} medals, {country_2_total - self_total} fewer than {country_2.name}, which received {country_2_total}.")
        else:
            print(
                f"Overall, both {self.name} and {country_2.name} received {country_2_total} medals.")

#3.1 End 

#----------------------------------------------------------------------------------------------------------

#3.2 Start

#defining countries as an empty dictionary
countries = {}

#the keyword "with open()" in Python opens a file, which name is passed as the parameter
with open("Medals.csv") as csvfile:
    #keyword "next" skips the first line in the csv file
    next(csvfile)
    #csv reader is used to read the csv file, and returns an iterable reader object
    reader = csv.reader(csvfile)
    #for loop iterates over the iterable object and adds name, medal types and 
    #the total of all medals for each country in a separate row in "countries"
    for row in reader:
        countries[row[1]] = CountryMedals(
            row[1], int(row[2]), int(row[3]), int(row[4]))

#3.2 End 

#------------------------------------------------------------------------------------------------------------

#3.3 Start

#no need of sorting by lambda as python knows to sort by string that is "alphabetically"
def get_sorted_list_of_country_names(countries):
    return sorted(countries.keys())

#we provide a lambda function to sort by medal type (Python is not sure how to sort objects)
def sort_countries_by_medal_type_ascending(countries, medal_type):
    return sorted(countries.values(), key=lambda country: country.get_medals(medal_type))

#we provide a lambda function to sort by medal type (Python is not sure how to sort objects)
def sort_countries_by_medal_type_descending(countries, medal_type):
    return sorted(countries.values(), key=lambda country: country.get_medals(medal_type), reverse=True)

#using try/except block to handle positive integer reading graciously
def read_positive_integer():
    while True:
        try:
            user_input = int(
                input("Enter the threshold (a positive integer): "))
            if user_input >= 0:
                return user_input #prompting user to enter again
        except ValueError: 
            pass

def read_country_name():
    #returns a country name and boolean (did the user enter a valid country name?)
    while True:
        user_input = input("Insert a country name ('q' to quit): ")
        #if statement to check if country name is already present
        if user_input in countries:
            return user_input, False
        #setting exit condition
        elif user_input == 'q':
            return None, True
        else:
            print("Please enter a valid country name.")
            print("Valid country names:")
            #the .join() function separates a list by the given comma ,
            print(', '.join(get_sorted_list_of_country_names(countries)))

#prompting the user to enter a medal type
def read_medal_type():
    while True:
        user_input = input(
            "Insert a medal type (chose among 'gold', 'silver', 'bronze', or 'total'): ")
        user_input = user_input.lower() 
        #.lower() to prevent any issues to case sensitivity
        if user_input in ['gold', 'silver', 'bronze', 'total']:
            return user_input

#3.3 End

#--------------------------------------------------------------------------------------------------------------------------------------------------

#3.4 Start 

#print_help() function
#this function displays all the commands available as shown in the specification using print()
#statements
def print_help():
    print("""
List of commands:
- (H)elp shows the list of comments;
- (L)ist shows the list of countries present in the dataset;
- (S)ummary prints out a summary of the medals won by a single country;
- (C)ompare allows for a comparison of the medals won by two countries;
- (M)ore, given a medal type, lists all the countries that received more medals than a treshold;
- (F)ewer, given a medal type, lists all the countries that received fewer medals than a treshold;
- (E)xport, save the medals table as '.json' file;
- (Q)uit.
""")

#show_list_of_countries() function
#this function uses templating and in-line commands such as "len"
#the print statement also uses .join() to separate values using a comma
#displays a list of the countries present in the dictionary "countries"
def show_list_of_countries():
    print("")
    print(
        f"The dataset contains {len(countries)} countries: {', '.join(get_sorted_list_of_country_names(countries))}")

#handle_compare_countries() function
#enables user to enter countries to be compared 
#previously defined functions are then called, i.e. compare()
def handle_compare_countries():
    print("\nCompare two countries")
    country_1, quit_flag = read_country_name()
    #quit_flag is a variable which represent if the user has pressed q to quit the program
    print()
    if quit_flag:
        return
    print(
        f"Insert the name of the country you want to compare against '{country_1}'")
    country_2, quit_flag = read_country_name()
    print()
    if quit_flag:
        return
    countries[country_1].compare(countries[country_2]) #calling compare() function

#print_summary()
#calling print_summary() previously defined
def print_summary():
    country_name, quit_flag = read_country_name()
    if quit_flag:
        return
    countries[country_name].print_summary()

#handle_more_medals() function
#considers a threshold
#firstly using sort_countries_by_medal_type_descending it is sorted based on medal type
#then for loop iterates comparing against that threeshold to be more than it
#prints all countries with specific medal type in question more than relevant threshold
def handle_more_medals():
    print("Given a medal type, lists all the countries that received more medals than a threshold;")
    medal_type = read_medal_type()
    threshold = read_positive_integer()
    print(
        f"Countries that received more than {threshold} '{medal_type}' medals:\n")
    countries_more_than_threshold = sort_countries_by_medal_type_descending(
        countries, medal_type)
    for country in countries_more_than_threshold:
        if country.get_medals(medal_type) > threshold:
            print(f"- {country.name} received {country.get_medals(medal_type)}")

#handle_less_medals() function
#considers a threshold
#firstly using sort_countries_by_medal_type_ascending it is sorted based on medal type
#then for loop iterates comparing against that threeshold to be less than it
#prints all countries with specific medal type in question less than relevant threshold
def handle_fewer_medals():
    print("Given a medal type, lists all the countries that received fewer medals than a threshold;")
    medal_type = read_medal_type()
    threshold = read_positive_integer()
    print(
        f"Countries that received fewer than {threshold} '{medal_type}' medals:\n")
    countries_fewer_than_threshold = sort_countries_by_medal_type_ascending(
        countries, medal_type)
    for country in countries_fewer_than_threshold:
        if country.get_medals(medal_type) < threshold:
            print(f"- {country.name} received {country.get_medals(medal_type)}")

#save_to_json() function
#appending extension .json at the end
#so user is only expected to write file name
def save_to_json():
    file_name = input("Enter the file name (.json)") + ".json"
    #keyword 'w' is clear the file and write over it
    with open(file_name, 'w') as json_file:
        #using function json.dumps to convert into json string format 
        #the parameter indent simply just represents the spacing in the json file
        #4 is an appropriate spacing
        json_file.write(json.dumps([x.to_json() for x in countries.values()], indent=4))
    print(f"File '{file_name}' correctly saved in the directory of this .py file.")
    
#------------------------------------------------------------------------------------------------------------------------------------

#main program 
#while loop set to True consisting of a block of if,elif, else statements to act as 
#a centralised menu for the user to pick course of action based on the specification

while True:
    command = input("Insert a command (Type 'H' for help ): ")
    command = command.upper()
    if command == "L":
        show_list_of_countries()
    elif command == "C":
        handle_compare_countries()
    elif command == "S":
        print_summary()
    elif command == "M":
        handle_more_medals()
    elif command == "F":
        handle_fewer_medals()
    elif command == "Q":
        break
    elif command == "E":
        save_to_json()
    elif command == "H":
        print_help()
    else:
        print("Command not recognised. Please try again")
