'''
Write a Program that takes in an item value,and adds that item to a group.
items can be shop items liks Bread ,Milo, Sugar
Your program should allow the user to search for an item in the group.If the item is in the group ,the program shouls display the item name ,and the total number
for example Milk 2
Your program should allow user to see the total of items in the group.
for example 
Milk 2
Sugar 4
Bread 2
Total 8
'''

products = []
new_products = []

def enter_p():
    x = input('Enter a product ')
    return x

def add_p(products):
    x = enter_p()
    products.append(x)

def display():
    print('The products are: ',products )
    

def add_another_p():
    x = input('Y to add another N to stop ')
    y = x.upper()
    if y == 'Y':
        add_p(products)
        add_another_p()
    elif y == 'N':
        display()
    else:
        print('invalid input')
        add_another_p()

        
def to_lowerCase():
    x = 0
    while x < len(products):
        new_products.append(products[x].lower())
        x = x+1

        
def search_product():
    x = input('search for a product ')
    y = x.lower()
    if x in new_products:
        count = new_products.count(y)
        total = len(new_products)
        print(f'Number of {y} is {count}')
        print(f'total number of item in products is: {total}')
    else:
         print('item not found')
        

add_p(products)
add_another_p()
to_lowerCase()
search_product()