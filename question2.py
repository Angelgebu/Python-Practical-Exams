'''
Write a function that takes as an argument a list, data of strings and returns a tuple containing two lists. 
The first list in the tuple should contain all of the strings in the original list 
that have length less than or equal to 4, and the second should contain all of the strings that have length greater than or equal to 7.
'''


arg = ["data", "Happy", "Brave", "Old boy", "Simple", "attenuate", "Shy Ones", "Toxic things", "Silent words", "Big Daddy", "Juveline", "Mothers love"]
list1 = []
list2 = []
def tuple_of_str():
    x = 0
    while x < len(arg):
        if len(arg[x]) <= 4:
            list1.append(arg[x])
        elif len(arg[x]) >= 7:
            list2.append(arg[x])
        x = x + 1
    new_tuple = (list1, list2)
    print(new_tuple)
    

tuple_of_str()