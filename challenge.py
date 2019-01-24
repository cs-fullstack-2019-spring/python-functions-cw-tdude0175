def main():
    challenge()




def add(number,number2):
    return number + number2
def subtract(number,number2):
    return number-number2
def multiply(number,number2):
    return number*number2
def divide(number,number2):
    return number//number2



def askfornumber():
    number1 = int(input("give me a number"))
    return number1




def whatDoYouWantToDo(number,secondnumber):
    operation = input("what operation do you want to use? add / subtract / multiply / divide")

    if(operation.lower() == "add"):
        result =add(number,secondnumber)
    elif(operation.lower() == "subtract"):
        result = subtract(number,secondnumber)
    elif(operation.lower() == "multiply"):
        result = multiply(number,secondnumber)
    elif(operation.lower() == "divide"):
        result = divide(number,secondnumber)
    thisIsWhatYouDid(number,secondnumber,result,operation)


def thisIsWhatYouDid(num1,num2,solution ,operation):
    print(f"{num1} and {num2} make {solution} when you {operation}")

# Create the entire program.
# Create a function that’s passed two numbers and ask if the user wants to
# add, subtract, multiply, or divide.
# Return a string that prints the two numbers,
# which operation it did, and the result.

def challenge():
    whatDoYouWantToDo(askfornumber(),askfornumber())







if __name__ == '__main__':
    main()