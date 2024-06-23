import sys

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return 'Error! Denominator cannot be zero'
    return x / y

print('Calculator')
print('Enter an operation')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

while True:
        value = input('Select operation to be performed(1,2,3,4): ')

        if value in ('1', '2', '3', '4'):
        
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            

            if value == '1':
                print(f'{num1} + {num2} = {addition(num1, num2)}')
            elif value == '2':
                print(f'{num1} - {num2} = {subtraction(num1, num2)}')
            elif value == '3':
                print(f'{num1} * {num2} = {multiplication(num1, num2)}')
            elif value == '4':
                print(f'{num1} / {num2} = {division(num1, num2)}')
        else:
            print('Invalid operation, Enter a number from the given options.')
            continue
        
        continue_calculation = input('Do you want to continue? (yes/ no) \n').strip().lower() 

        if continue_calculation == 'yes':
            continue
        elif continue_calculation == 'no':
            break
        else:
            print('Error')
            continue_calculation = input('Error! Type(yes/ no) \n').strip().lower()
            while True:
              if continue_calculation == 'yes':
                break
              elif continue_calculation == 'no':
                sys.exit(0)
              else:
                print('Invalid input')