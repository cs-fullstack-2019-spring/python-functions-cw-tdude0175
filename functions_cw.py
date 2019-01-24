def main():
    problem1()
    problem2()
    problem3()
    problem4()

# Create a function in your program that counts from 0 to [NUMBER]

def problem1():
    counttonumber(100)

# use a for loop

def counttonumber(end):
    for x in range(0,end+1):
        print(x)

# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q',
# ask them to input another string.

def problem2():
    dontstoptillq()

# while i do this someone doesn't need help i bet
def dontstoptillq():
    userinput = input("i have given up")
    while(userinput.lower() != "q"):
        userinput = input("this is the give up section")

# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.

# conjunction junction what's your function

def problem3():
    number1 = int(input("give me your first number"))
    number2 = int(input("give me one more"))
    print(add(number1,number2))
    print(subtract(number1,number2))
    print(multiply(number1,number2))
    print(divide(number1,number2))



def add(number,number2):
    return number + number2
def subtract(number,number2):
    return number-number2
def multiply(number,number2):
    return number*number2
def divide(number,number2):
    return number//number2

# Create a function that will ask the user for a number.
# Use the function to get two numbers,
# then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.

# i still F U N C T I O N

def problem4():
    askfornumber()

def askfornumber():
    number1 = int(input("give me a number"))
    number2 = int(input("give me one more"))
    print(whatDoYouWantToDo(number1,number2))

def whatDoYouWantToDo(number,secondnumber):
    operation = input("what operation do you want to use? add / subtract / multiply / divide")
    if(operation.lower() == "add"):
        return number + secondnumber
    elif(operation.lower() == "subtract"):
        return number - secondnumber
    elif(operation.lower() == "multiply"):
        return number*secondnumber
    elif(operation.lower() == "divide"):
        return number/secondnumber

# Create the entire program.
# Create a function that’s passed two numbers and ask if the user wants to
# add, subtract, multiply, or divide.
# Return a string that prints the two numbers,
# which operation it did,
# and the result.




if __name__ == '__main__':
    main()