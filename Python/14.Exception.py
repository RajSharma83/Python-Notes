  # The process in programming by which block of code containing errors can be skipped 
    # and its later block can be executed is called exception handeling it is similar to 
    # if else statement 

# try:
  #body which can create error

#except:
  # body to be run if there is error

  # Exception handeling in python uses two keywords try and except both containes their own block
  # try block containes body which can possibly create the error the solution to handeling the
  # error if occured is return inside the except block suppose we are trying to read the file
  # but the file does not exist in the mentioned part then after having the issueof file not found 
  # the entire code will be terminated 

  # Note : To handel such runtime error we can use exception handeling in the above case the 
          # the process to read the file will be written inside the try bloack and simple 
          # print statement can be written inside the execpt bloack this will ensure that if the 
         # is not found code will print the simple message and move on the next module without 
         # hault 

# res = 0
# a = int(input("Enter the value of A: "))
# b = int(input("Enter the value of B: "))
# try:
#     res=a//b
# except :
#     print("Error !!! B cannot be 0 ")
# print("The value of Res :",res)    


    # Single try can contain which will be benifical for handeling multiple types of possible error.
     # Other can except try can also have two more types of bloack : 1.else and 2.finally
     # In else body which is to be executed if not execpt is run.
     # In finally run in all cases if try , else execpt will run or not.


# res = 0
# try:
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     res=a//b
# except ZeroDivisionError:
#     print("Error !!! B cannot be 0 ")
# except ValueError:
#     print("Error !!! Inserted value is invalid")    
# else:
#     print("Invalid Data !")
# finally:     
#     print("The value of Res :",res)  



    # Explicit exception chaining during exception handeling is the sinerio where the new error
    # occurs while handeling the another error manually this can be done using raise keyword 

  #  Note: Traceback -> Traceback report in python is generated when unhandeled exception occur
    # it provides a detail account of the function call and code execution leading to the point 
    # where the exception is raised. In this report the multiple error occured are registered
    # sequentionaly based on the time they occured (error occured first will be listed first) 
