#Python Calculator
  #Creat Function
  #user Input   
  #Print Output

#Step-1

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def avg(num1, num2):
    return (num1 + num2)/2


#Step-2

print("Please Sel a Opreation\n"\
      "1.Addition\n" \
      "2.Subtraction\n"\
      "3.Multiply\n"\
      "4.Divide\n"\
      "5.Avarege")

while True:
    try:
        select = int(input("Please select 1,2,3,4,5: "))

        number1 =int(input("Put 1st Number: "))
        number2 =int(input("Put 2nd Number: "))

        #step-3

        if select == 1:
            print(number1, "+", number2, "=", add(number1, number2))
            

        elif select == 2:
            print(number1, "-", number2, "=", sub(number1, number2))
            

        elif select == 3:
            print(number1, "x", number2, "=", multiply(number1, number2))
            

        elif select == 4:
            print(number1, "/", number2, "=", divide(number1, number2))
            

        elif select == 5:
            print(number1, "avg", number2, "=", avg(number1, number2))
            

        else:
         print("Invaild Opreation")

        should_countino = input("countinio (y/n)").lower()
        if should_countino == 'n':
            break

    except ValueError:
        print("Enter a valid number.")