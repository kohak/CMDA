#Andrew Koh
#09/30/2014
#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Print "I will now count my chickens:"
print "I will now count my chickens:" 

#Print the String and the arithmetic result of the equation next to it
#Order of operations matter so it's 25 + 5
print "Hens", 25 + 30 / 6
#% is Modulus (or remainder)
#100 - (75%4) = 100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

#Print "Now I will count the eggs:"
print "Now I will count the eggs:"

#Print the arithmetic result of the equations with order of operations
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#Print "Is it true that 3 + 2 < 5 - 7", which is false
print "Is it true that 3 + 2 < 5 - 7?"

#Print boolean answer that the comparison is false
print 3 + 2 < 5 - 7

#Print a string and then the arithmetic result of the equations
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

#Print "Oh, that's why it's False."
print "Oh, that's why it's False."

#Print "How about some more."
print "How about some more."

#Print a string and then the boolean result of the comparison
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#PART II

#Stores the days of the week into a variable as a String
days = "Mon Tue Wed Thu Fri Sat Sun"
#Stores the months of the year into a variable as a String with line breaks
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Prints the strings
print "Here are the days: ", days
print "Here are the months: ", months

#PART III

#Creates arrays and stores single-type variables into the arrays
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
#Creates an array that stores different-type variables into one array
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Prints the variables in array the_count with a foreach loop with % to 
#determine what kind of variable the output is going to be. $d is for decimal
for number in the_count:
    print "This is count %d" % number

# Prints the variables in array fruits with a foreach loop with % to 
#determine what kind of variable the output is going to be. $s is for string
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Prints the variables in array change with a foreach loop
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# Print the list that we just created with the range function that acts like
# a for loop to append the list with numbers from 0 to 6
for i in elements:
    print "Element was: %d" % i
    
    #Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

####Start Stuff from Lecture 14####
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)
####End Stuff from Lecture 14####


print stuff[1] #Print Oranges
print stuff[-1] #Print Corn 
print stuff.pop() #Print Corn and removes it
print ' '.join(stuff) #Prints all from stuff list with " " in between
print '#'.join(stuff[3:5]) #Prints elements 3-5 from stuff list with "#" in between


#PART II

#Create comments where marked with # to explain the code below

# 
#Create a dictionary with states with state names and abbreviations 
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# 
#Create a dictionary with cities with state abbreviations and city names 
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# 
#Addes to dictionary cities with state abbreviations and city names
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 
#Prints to -
#Prints the city name with state abbreviations as key
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# 
#Prints to -
#Prints the state abbreviations with state names as key
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# 
#Prints to -
#Prints the city names with state abbreviations as keys from states with state names as key
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# 
#Prints to -
#Prints each state and abbreviations with for each loop
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# 
#Prints to -
#Prints each city and state abbreviations with for each loop
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# 
#Prints to -
#Prints each city and state name state abbreviations with for each loop using
#cities from the cities list with state abbreviations key
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])


