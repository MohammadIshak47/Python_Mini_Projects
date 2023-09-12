def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y ==0:
        return "can't divided by zero"
    return x/y 
def mod(x,y):
    return x%y
def flr(x,y):
    return x//y
def expo(x,y):
    return x**y

while True:
    print("Options : ")
    print("Enter 'add' for addition")
    print("Enter 'sub' for substraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'mod' for modulus")
    print("Enter 'flr' for floor")
    print("Enter 'expo' for exponential")
    
    user_input = input(" : ")
    
    if user_input == 'exit':
        break
    elif user_input in ("add","sub","mul","div","mod","flr","expo"):
        num1 = float(input("Enter your first number : "))
        num2 = float(input("Enter your seconde number : "))
        
        if user_input == "add":
            print("The result of your addition is ",add(num1,num2))
        elif user_input == "sub":
            print("The result of your substraction is ",sub(num1,num2))
        elif user_input == "mul":
            print("The result of your multiplication is ",mul(num1,num2))
        elif user_input == "div":
            print("The result of your division is ",div(num1,num2))
        elif user_input == "mod":
            print("The result of your modulus is ",mod(num1,num2))
        elif user_input == "flr":
            print("The result of your floor is ",flr(num1,num2))  
        elif user_input == "expo":
            print("The result of your exponential is ",expo(num1,num2))
        
        else:
            print("Invalid input! Please give valid input")                          
    