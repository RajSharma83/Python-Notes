#                                   File Handling in Python 
#                             --------------------------------------------


#1. "r" --> Read - Default value. Opens a file for reading, error if the file does not exist
#2. "w" --> Write - Opens a file for writing, creates the file if it does not exist
#3. "a" --> Append - Opens a file for appending, creates the file if it does not exist
#4. "x" --> Create - Creates the specified file, returns an error if the file exists
#5. "t" --> Text - Default value. Text mode
#6. "b" --> Binary - Binary mode (e.g. images)
#7. "x"	--> Exclusive creation mode. Creates a new file. Raises an error if the file 
        # already exists.
#8. seek() --> Reset the cursor. Mainly used to read the file line by line.




# "r" --> Read - Default value. Opens a file for reading, error if the file does not exist

# Read all data in the file
f = open("deno.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# Read the data a given index
g = open("deno.txt" , "r")
data = g.read(7)
print(data)
g.close()

# Read the data line - by - line 
h = open("deno.txt" , "r")
line1 = h.readline()
print(line1)

line2 = h.readline()
print(line2)
h.close()
#Once the all data is reades in the file then the line by line is to be  blank 






# "w" --> Write - Opens a file for writing, creates the file if it does not exist

f = open("deno.txt", "w")
f.write("Welcome to the world of the programming.")
f.close()




# "a" --> Append - Opens a file for appending, creates the file if it does not exist

f = open("deno.txt", "a")
f.write("\nNext I will move to the reactJs")
f.close()

#If we open a file in "w" or "a" mode and the file didn't exist then it will create a newc file 

f = open("sumo.txt", "w")
f.close()

f = open("Eemo.txt", "a")
f.close()

print("End of the first Topics")







# 1. "r+" --> Read and write mode.	Opens the file for both reading and writing. File must exist;
                # otherwise, it raises an error.
# 2. "rb" --> Read-only in binary mode.	Opens the file for reading binary data. File must exist;
                # otherwise, it raises an error.
# 3. "rb+" --> Read and write in binary mode. Opens the file for both reading and writing
                # binary data. File must exist; otherwise, it raises an error.
# 4. "wb"  --> Write in binary mode.	Opens the file for writing binary data. Creates a new
                # file or truncates the existing file.
# 5. "w+" --> Write and read mode.	Opens the file for both writing and reading. 
                # Creates a new file or truncates the existing file.
# 6. "wb+" --> Write and read in binary mode.	Opens the file for both writing and reading
                #  binary data.Creates a new file or truncates the existing file.
# 7. "ab" --> Append in binary mode.	Opens the file for appending binary data. 
                # Creates a new file if it doesn't exist.
# 8. "a+" --> Append and read mode.	Opens the file for appending and reading. 
                # Creates a new file if it doesn't exist.
# 9. "ab+" --> Append and read in binary mode.	Opens the file for appending and reading binary data.
                # Creates a new file if it doesn't exist.
# 10. "xb" -->Exclusive creation in binary mode.	Creates a new binary file.
                # Raises an error if the file already exists.
# 11. "x+" -->Exclusive creation with read and write mode.
                # Creates a new file for reading and writing. Raises an error if the file exists.
# 12. "xb+" -->Exclusive creation with read and write in binary mode.	
                # Creates a new binary file for reading and writing. Raises an error if the
                # file exists.
        




# "r+" --> Read and write mode.	Opens the file for both reading and writing. File must exist; otherwise, 
#               it raises an error.

j = open("deno.txt", "r+")
j.write("YO")
print(j.read())
j.close()




# with is type of function for file handling but no the funtion and close() is also provided in end 

with open("deno.txt", "r") as f: 
    data = f.read()
    print(data)


# others are also  but major part had done 






# Deletion a File
# using the os module
# Modules are  (like a code library) is a filewritten by another programmer that generally 
# has a function we can use

# import  os 
# os.remove( filename )

import os
os.remove("sumo.txt")