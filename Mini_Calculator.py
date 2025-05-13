class Calculator:
    def print_menu(self):
        '''This function will print out menu of calculator'''
        print('Mini Calculator')
        print('1. Sum')
        print('2. Minus')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')
        
    def sum(self,num1,num2):
        '''This function will return sum of 2 numbers'''
        return num1 + num2
    
    def minus(self,num1,num2):
        '''This function will return minus result of 2 numbers'''
        return num1 - num2
    
    def multiply(self,num1,num2):
        '''This function will return multiply result of 2 numbers'''
        return num1 * num2
    
    def divide(self,num1,num2):
        '''This function will return division result of 2 numbers and raise error if divive by 2'''
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return "Can't divide by zero"
                
    
    def options(self):
        '''This function will: 
        _ Take user input
        _ Raise Error if input is not a number or out of range
        _ Call the function depends on user input'''
        while True:
            while True:
                try:
                    option = int(input('What is your choice: '))
                    break
                except ValueError:
                    print('Your choice is not valid, please try again.')
                    continue
            if option == 5:
                exit = False
                break
            while True:
                try:
                    num1 = int(input('Please enter the first number: '))
                    break
                except:
                    print('Your choice is invalid, please try again')
                    continue
            while True:
                try:
                    num2 = int(input('Please enter the second number: '))
                    break
                except ValueError:
                    print('Your choice is invalid, please try again')
                    continue
            if option == 1:
                print(self.sum(num1,num2))
                print('')
            elif option == 2:
                print(self.minus(num1,num2))
                print('')
            elif option == 3:
                print(self.multiply(num1,num2))
                print('')
            elif option == 4:
                print(self.divide(num1,num2))
                print('')
            else:
                print('Vui lòng chọn số từ 1-5')

            
    def display(self):
        '''This function will display everything, call this function'''
        while True:
            self.print_menu()
            if not self.options():
                break
            
math = Calculator()
math.display()
            
