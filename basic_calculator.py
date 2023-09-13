def add(a,b):
        return a + b
def sub(a,b):
       return a - b
def mul(a,b):
       return a * b
def div(a,b):
       return a // b
def mod_div(a,b):
       return a%b
        
print("welcome to calculator")
print("YOr options are: ")
print("1)Addition:")
print("2)Subtraction:")
print("3)Multiplication:")
print("4)Division:")
print("5)mod Division:")
print("")



while True:
        try:
            num1 = float(input("first number:"))
            num2 = float(input("second number:"))
        except ValueError:
            print("give valid number")
        choice = input("choose your option:")
        if choice in ('1','2','3','4','5'):
                
                if choice == '1':
                       print(num1,"+",num2,"=",add(num1,num2))
                elif choice == '2':
                       print(num1,"-",num2,"=",sub(num1,num2))
                elif choice == '3':
                       print(num1,"*",num2,"=",mul(num1,num2))
                elif choice == '4':
                       print(num1,"//",num2,"=",div(num1,num2))
                elif choice == '5':
                       print(num1,"%",num2,"=",mod_div(num1,num2))
                next_op = input("would you like to continue:(y/n)")
                if next_op== 'n' :
                       break                       
        else:
               print("inavlid input")
print("CASIO")
                      
                      

        
          

