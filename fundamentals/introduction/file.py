num1 = 42 #variable declaration, integer
num2 = 2.3 #variable declaration, float
boolean = True #variable declaration, Boolean value
string = 'Hello World' #variable declaration, string value
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declartion, dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple initialize
print(type(fruit)) #function(function(argument))
print(pizza_toppings[1]) #function(list access value)
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #function(argument dictionary access value)
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dicionary add value
print(fruit[2]) #function(argument tuple access value)

if num1 > 45: #conditional if
    print("It's greater")
else: #conditional else
    print("It's lower")

if len(string) < 5: #conditional if
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for lopp start at 0 go to 4
    print(x)
for x in range(2,5): #for loop start at 2 go to 4
    print(x)
for x in range(2,10,3): #for loop start at 2 go to 9 increment by 3
    print(x)
x = 0
while(x < 5): #while loop start 
    print(x) 
    x += 1 #while loop increment

pizza_toppings.pop() #list delete last element
pizza_toppings.pop(1) #list delete second element

print(person)
person.pop('eye_color') #dictionary delete item
print(person)

for topping in pizza_toppings: #for loop in itialize
    if topping == 'Pepperoni': #conditional initialize
        continue #for loop continue 
    print('After 1st if statement')
    if topping == 'Olives': #conditional initialize
        break #for loop break

def print_hello_ten_times(): #function initialize
    for num in range(10): 
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x): #function initialize, parameter x
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function call with argument = 4

def print_hello_x_or_ten_times(x = 10): #funciton initilize with default argument x = 10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)