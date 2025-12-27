    # 1. Assign grading system -
        # 100 - 90 ----> A
        # 89 - 80  ---> B
        # 79 - 70  ----> C
        # 60 - 55 ----> D
        # Below ss and fail


     # 2. Age group classification -
       # 0 - 12 ----> chid
       # 13 - 19 ----> adult
       # 65 ----> Budhaaaaa

     # 3. User based calculator -
        # choice (+,-,*,/,%)
     
     # 4. Largest of 3 number - 

     # 5. Leap year checker- 

     # 6. Program a game for user called Rock , Paper , Scissor


# --------------------------------------------------------------------------------------------------------
                                #  Answer 
        # Note:    90 <= score <= 100  --> This is called chained condition 
        # we can use chained condition instead of and . This more efficient and easy to understand


      # @1.

# score = int(input("Enter Your score: "))
# if 90 <= score <= 100: print("A")
# elif 80 <= score <= 89: print("B")
# elif 70 <= score <= 79: print("C")
# elif 55 <= score <= 60: print("D")
# elif 54 >= score : print("Below ss or fail")
# else: print("Error : Don't enter value above 100")



      # @2.

# age = int(input("Enter your age: "))
# if age >= 0 and age <= 12: print("Child")
# elif age >= 13 and age <= 19: print("Adult")
# elif age == 65: print("Budhaaaaa")
# else: print("You are Dead , Say Hi to YamRAj from my side ")


     # @3.

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print("Choose operation: +  -  *  /  %")
# choice = input("Enter your choice: ")
# if choice == "+": print("Result:", num1 + num2)
# elif choice == "-": print("Result:", num1 - num2)
# elif choice == "*": print("Result:", num1 * num2)
# elif choice == "/":
#     if num2 != 0: print("Result:", num1 / num2)
#     else: print("Error: Cannot divide by zero")
# elif choice == "%":
#     if num2 != 0: print("Result:", num1 % num2)
#     else:  print("Error: Cannot perform modulus by zero")
# else: print("Invalid operation choice")



      # @4.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 >= num2 and num1 >= num3:print("Largest number is:", num1)
# elif num2 >= num1 and num2 >= num3: print("Largest number is:", num2)
# else: print("Largest number is:", num3)


      
      # @5.

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print(year, "is a Leap Year")
# else: print(year, "is NOT a Leap Year")




       # @6.

# print("Select any option given below")
# print("1 = Rock ; 2 = Paper ; 3 = Scissors")
# ply1 = int(input("Enter your choice Player1 : "))
# ply2 = int(input("Enter your choice Player2 : "))
# if ply1>= 4 or ply2>= 4 :  print("You have entered wrong choice number Dear !")
# elif ply1 == ply2: print(" Match draw !") 
# elif (ply1 == 1 and ply2 == 3) or \
#          (ply1 == 2 and ply2 == 1) or \
#          (ply1 == 3 and ply2 == 2):
#          print("Player1 wins and Player1 have choosen :", ply1)
# else: print("Player2 wins and Player2 have choosen :", ply2)
        


         # Prime number
    
# a = int(input("Enter your number to check : "))
# if a>1 :
#  for i in range(2,a) : 
#     if(a%i==0) :  print("this is not prime number")
#     break
#  else : print("this is prime number")
# else : print("Invaild input")   



         # WAP to print the sum of two user input numbers if the input are numerical and print the
         # message not possible if the inputs are string. 

# a = input("Enter your number 1 : ")
# b = input("Enter your number 2 : ")
# if a.isdigit() and b.isdigit():
#     r = int(a) + int(b)
#     print("Sum:", r)
# else: print("Not possible ! Invalid input are string. ")





       # @1. WAP Take user input for temprature in celcius cand convert it into fahrenheit.

      #  @2. WAP to the user and check if the number is positive, negative or 0 further is the number is
      #    postive check it is even or odd and check if it is negative then check if it is >-10 or <-10 
      #    check if it zero then print zero.



      #  @3. Ask the user for the withdrawal amount and check the balance of the account :
      #       1. Your atm machine contains only 100 and 500 rupee notes proceed with the possible message
      #       2. transaction successful . enter amount in multiple of 100 and 500
      #       3. Print insufficient balance  


      #  @4. A user want to apply for driving licence. Ask the user for the age :
      #  if age is greater is >=18 check the leaner licence is exist or not then print 
      #         licence is issued 
      #  And if not issued then print proceed for learning licence 
      #   and if age is below 18 then your are not eligble for licence.



       # @1 .

# cel = float(input("Enter the temperature in Celsius: "))
# fahren = (cel * 9/5) + 32
# print(f"{cel}°C is equal to {fahren}°F")



       # @2 .

# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive :",num)
#     if num % 2 == 0:
#         print("It is even :",num)
#     else:
#         print("It is odd.")
# elif num < 0:
#     print("The number is negative.")
#     if num > -10:
#         print("It is greater than -10.")
#     elif num < -10:
#         print("It is less than -10.")
#     else:
#         print("It is exactly -10.")
# else: print("The number is Zero.")



       
           # @3.

# balance = 50000
# deb = int(input("Enter amount to be debited"))
# if deb > balance : print("Insufficient Balance")         
# else : 
#     if deb%100 == 0 or deb%500 == 0: print(f"Trensaction Successful.\n Left balance = {balance-deb}")
#     else : print("Error ! Enter aomunt in multiple of 100 or 500 !")




          # @4 .

# age = int(input("Enter your age: "))
# if age >= 18:
#     has_learner = input("Do you have a learner's licence? (yes/no): ").strip().lower()
#     if has_learner == "yes":
#         print("Licence is issued.")
#     else:
#         print("Proceed for learning licence.")
# else: print("You are not eligible for licence.")





   #@5. Create a list of tweleve integer number by taking user input use the loop to find the following:
      # 1. Sum of all the number in the list 
       # 2. Count number of even number in the list
        # 3. Count number of add number in the list
          # 4.find  Max min  in the list with for  loop without max min function


# list = []
# print("Enter 12 numbers:")
# for i in range(12):
#     n = int(input())
#     list.append(n)

# total = 0
# for num in list:
#     total += num    
# print("Total sum of the list: ",total)

 
# even = 0
# sumEven = 0
# sumOdd = 0
# odd = 0 
# for i in list:
#       if i % 2 == 0:
#         even += 1  
#         sumEven += i        
#       else:
#         odd += 1 
#         sumOdd += i
# print("Total number of even numbers in the list: ",even) 
# print("Sum number of even numbers in the list: ",sumEven)   
# print("Total number of odd numbers in the list: ",odd)
# print("Sum number of odd numbers in the list: ",sumOdd)   



# max = list[0]
# min = list[0]

# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i

# print("Max in the lit :", max)
# print("Min in the list :", min)








                  # @6. Take the user input of list elements the no of elements depends
                  #  upon the user ans input continues until user a -ve no with the created
                    #  list perform all thr above operations in previous

# list = []
# print("Enter numbers but it stops when you entered negative number:")
# while True:
#     n = int(input())
#     if n ==-1:
#      break
#     else: 
#       list.append(n)

# total = 0
# for num in list:
#     total += num    
# print("Total sum of the list: ",total)



# list = []
# print("Enter numbers but it stops when you enter a negative number:")
# n = 0 
# while n >= 0:
#     n = int(input())
#     if n >= 0:
#         list.append(n)
# print("You entered:", list)

# total = 0
# for num in list:
#     total += num    
# print("Total sum of the list: ",total)

 
# even = 0
# sumEven = 0
# sumOdd = 0
# odd = 0 
# for i in list:
#       if i % 2 == 0:
#         even += 1  
#         sumEven += i        
#       else:
#         odd += 1 
#         sumOdd += i
# print("Total number of even numbers in the list: ",even) 
# print("Sum number of even numbers in the list: ",sumEven)   
# print("Total number of odd numbers in the list: ",odd)
# print("Sum number of odd numbers in the list: ",sumOdd)   



# max = list[0]
# min = list[0]

# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i

# print("Max in the lit :", max)
# print("Min in the list :", min)



  



                  #  @6. WAP  that shows a menu with the following options
                  #      1. Add two numbers 
                  #      2. Subtract two numbers 
                  #      3. Multiply two numbers 
                  #      4. Divide two numbers 
                  #      5. Exit . 
                  #   The program should run until the user chooses exit.
                  #   For each choice take two user input number and perform the operation. 
                  #   If the user enters invalid choice print a message invalid.

# while True:
#     print("Select any option from the following options:")
#     print("1. Add two numbers")
#     print("2. Subtract two numbers")
#     print("3. Multiply two numbers")
#     print("4. Divide two numbers")
#     print("5. Exit")
#     choice = input("Enter your choice (1-5): ")
#     if choice == '5':
#         print("Exiting the program!")
#         break
#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         if choice == '1':
#             r = num1 + num2
#             print(f"Result: {num1} + {num2} = {r}")
#         elif choice == '2':
#             r = num1 - num2
#             print(f"Result: {num1} - {num2} = {r}")
#         elif choice == '3':
#             r = num1 * num2
#             print(f"Result: {num1} * {num2} = {r}")
#         elif choice == '4':
#             if num2 == 0:
#                 print("Error: Cannot divide by zero.")
#             else:
#                 r = num1 / num2
#                 print(f"Result: {num1} / {num2} = {r}")
#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")





                # with match case :
# while True:
#     print("Select any option from the following options:")
#     print("1. Add two numbers")
#     print("2. Subtract two numbers")
#     print("3. Multiply two numbers")
#     print("4. Divide two numbers")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     match choice:
#         case '1' | '2' | '3' | '4':
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             match choice:
#                 case '1':
#                     r = num1 + num2
#                     print(f"Result: {num1} + {num2} = {r}")
#                 case '2':
#                     r = num1 - num2
#                     print(f"Result: {num1} - {num2} = {r}")
#                 case '3':
#                     r = num1 * num2
#                     print(f"Result: {num1} * {num2} = {r}")
#                 case '4':
#                     if num2 == 0:
#                         print("Error: Cannot divide by zero.")
#                     else:
#                         r = num1 / num2
#                         print(f"Result: {num1} / {num2} = {r}")
#         case '5':
#             print("Exiting the program!")
#             break
#         case _:
#             print("Invalid choice. Please enter a number between 1 and 5.")




   
                      # @7. Is Prime or not 

# p = int(input("Enter the number to check: "))
# if p <= 1:
#     print(f"{p} is not a prime number")
# else:
#     flag = True
#     for i in range(2, p):
#         if p % i == 0:
#             flag = False
#             break
#     if flag:
#         print(f"{p} is a prime number")
#     else:
#         print(f"{p} is not a prime number")





    # Multiline string :
# massage = """I am good.
# class is fun 
# This is python"""
# print(massage)
# print(massage[:4])
# r  = massage[::-1]
# print(r)





     
            # @8. Take a user input of string and check if it palindrome or not

# str = input("Enter the string to check :")
# r  = str[::-1]
# if str == r:
#     print("This is palindrome")
# else :
#     print("Not")    




# str = input("Enter the string to check :")
# massage = """I am good.
# class is fun 
# This is python"""
# massage = str
# print(massage)





      # @9. WAP to creat a list of five string values inserted by the user and print the
      #  longest is string in the list
 
# strl = []
# for i in range(5):
#     st = input(f"Enter the {i} string value:")
#     strl.append(st)
# longest_str = "" 
# for s in strl:
#     if len(s) > len(longest_str):
#         longest_str = s
# print("The longest string is:", longest_str)


 
    
# lang = "python"
# if lang == "Java" or "html":
#     print("The value of lang is matched ")
# else :
#     print("The value is not matched !")    



      # @. Create a string called message and the message is "Good envening class
      #  this is python language" take the user input of variable task for asking
      # the taget character if the character exist in the message print 
      #  congratulation otherwise print Item nahi mila.


# message = "Good evening class this is python language"
# task = input("Enter the character to search: ")
# if task in message: print("Congratulation")
# else: print("Item nahi mila")



 


      #     @. WAP to take a user input of a string value which contains both uppercase and 
      #       lowercase order your task is to convert the string into upercase and lowercase and print
      #        both of them. 
       
# st = input("Enter the string value to convert :")
# print("You have entered :",st)
# print("The lower of the string is :",st.lower())
# print("The uperCase of the string is :",st.upper())




      #  @. WAP to take the user input of a string sentence including spaces and print the 
      #    sentences without spaces

# sentence = input("Enter a sentence: ")
# no_space = sentence.replace(" ", "")
# print("Sentence without spaces:", no_space)


# sentence = input("Enter a sentence: ")
# print("Sentence without spaces:",sentence)
# print("Sentence without spaces:",sentence.strip())


 


            #   @.  WAP to take the user input sentence containing more than one words seprated by 
            #        viod space convert the sentence into a list containing each word present in 
            #        the list.

# sentence = input("Enter a sentence with words separated by spaces: ")
# words_list = sentence.split()
# print("List of words:", words_list)

