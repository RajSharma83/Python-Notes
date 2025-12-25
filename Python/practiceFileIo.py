#                                   Practice Questions of File Handling
#                              -------------------------------------------------



#1. Create a file and write 4 lines in it.

# with open("practice.txt", "w") as f: 
#     f.write("Hello Everyone \n we are learning File i/o \n ")
#     f.write("Using the Python \n I love programing Python")


#2.  Write a function to replace the python with Javascript in practice.txt.

# with open("practice.txt", "r") as f:
#     data = f.read()
    
# newData = data.replace("Python", "JavaScript")
# print(newData)

# with open("practice.txt", "w") as f:
#     f.write(newData)


#3. Find the Learning is present in the file or not
  
# def checking_of_word():

#      word = "learning"
#      with open("practice.txt", "r") as f:
#         data = f.read()

#         if(data.find(word) !=-1):
#            print("Found in the file")
#         else:
#            print("Not Found in the file")

# checking_of_word()    


#4. Write a function to find in which line first occur the learning found 
# if not found then print the not found

# def check_of_line():
#     word = "joe"
#     data = True  #for while condition
#     line_no = 1
#     with open("practice.txt", "r") as f: 
#        while data:
#           data = f.readline()
#           if(word in data):
#            print(line_no)
#            return
#           line_no += 1

#     return -1
     
# check_of_line()




#5. From a file containing number seprated by the comma, Print the even count in the file 

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]    

# count = 0           
# with open("practice.txt", "r") as f:
#        data = f.read()
#        print(data)
       
#        nums = data.split(",")
#        for val in nums:
#               if(int(val)% 2 ==0):
#                      count +=1
# print(count)            