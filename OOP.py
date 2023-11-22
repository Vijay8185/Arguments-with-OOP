# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# OOP : Objet Oriented Programming
# Assignment:
# 1.Positional Argument with OOP
class Test:
    def info(self,name,age):
        print('name',name)
        print('age',age)
t = Test()
t.info('Vijay',33)

# 2.Keyword Argument with OOP
class Test:
    def display_info(self,first_name,last_name):
        print('First Name:',first_name)
        print('Last Name:',last_name)
t = Test()
t.display_info(first_name='vijay',last_name='shinde')


# 3.Default Argument with OOP
class Test:
    def add_numbers(self,a=25,b=45,c=75):
        sum = a + b + c
        print('Sum:', sum)
t = Test()
t.add_numbers(25,45,75)

# 4.Variable Length Argument with OOP
class Test:
    def multiply(self,*args):
        y = 1
        for num in args:
            y *= num
            print(y)
t =  Test()
t.multiply(7,3)
t.multiply(1,2,3,4,5)

class Test:
    def my_function(self,**kid):
        print("His last name is " + kid["lname"])
t = Test()
t.my_function(fname = "Aseet", lname = "Shinde")







