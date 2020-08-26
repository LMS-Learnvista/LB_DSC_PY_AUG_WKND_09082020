#Function to add 2 numbers
def add(a,b):
        return a + b

#Function to subtract 2 numbers
def subtract(a,b):
        return  a - b
#Function to multiply 2 numbers
def multiply(a,b):
        return a * b
#Function to divide 2 numbers:
def divide(a,b):
        return a / b

print("Please select a choice" "\n" "1. Add" "\n" "2. Subtract" "\n" "3. Multiply" "\n" "4. Divide" "\n")

choice = input("")


if choice in ('1','2','3','4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
                    print(add(x, y))
        
        elif choice == '2':
                    print(subtract(x, y))

        elif choice == '3':
                    print(multiply(x, y))

        elif choice == '4':
                    print(divide(x, y))

else : print("***Invalid Input***")
