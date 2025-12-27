# def add(a,b):
#     return a+b
# p = int(input("Enter value of P: "))
# q = int(input("Enter value of Q: "))
# sum = add(p,q)
# print("Result =",sum)


        # Funtion is block of statement providing modular approach to the solution 
         # a function can be declared using def keyword followed the name of function
         # along with parameter in parenthese . Functions are resuable , modular
         # containing return statement as an optional exectution



    # WAP which containes two funtions named as input and dissplay
    # the input function takes the user input of name, department , age 
    # for a particular employ and stores in the dictionary further 
    # display function is used to print the same details    

# def input_data():
#     employee = {}
#     employee['name'] = input("Enter employee name: ")
#     employee['department'] = input("Enter employee department: ")
#     employee['age'] = input("Enter employee age: ")
#     return employee

# def display_data(employee):
#     print("\n--- Employee Details ---")
#     print("Name      :", employee['name'])
#     print("Department:", employee['department'])
#     print("Age       :", employee['age'])
# emp_info = input_data()
# display_data(emp_info)


# def input_data():
#     employee = {}
#     employee['name'] = input("Enter employee name: ")
#     employee['department'] = input("Enter employee department: ")
#     employee['age'] = input("Enter employee age: ")
#     return employee

# def display_data(employee):
#     print("\n--- Employee Details ---")
#     print("Name      :", employee['name'])
#     print("Department:", employee['department'])
#     print("Age       :", employee['age'])


# for i in range(3):
#     print(f"\nEnter details for employee {i+1}")
#     emp = input_data()
#     display_data(emp)



 

                # @. WAP to take user input and print the multiplication 
                #  table using function and recursion

# def start():
#     num=int(input("Enter the number to print the table :"))
#     table(num,i=1)

# def table(num,i):
    
#     if i<=10:
#         print(num*i)
#         table(num,i+1)
# start()

# def table(number, multiplier=1):
#     if multiplier > 10:
#         return
#     print(f"{number} x {multiplier} = {number * multiplier}")
#     table(number, multiplier + 1)
# num = int(input("Enter a number to print table: "))
# print(f"\nMultiplication Table of {num}:\n")
# table(num)


            #   @. WAP to use Recursion and check number of odd and even integer
             #   digit present in the list of 10 item  

# def check(li, i, even, odd):
#     if i < 10:
#         if li[i] % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#         return check(li, i + 1, even, odd)
#     else:
#         print(f"Even = {even}, Odd = {odd}")     
# def start():
#     li = [14, 12, 52, 32, 15, 78, 95, 5, 81, 100]     
#     even = odd = 0
#     check(li, i=0, even=even, odd=odd)
# start()





