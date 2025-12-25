#                              Oops in Python : Object oreiented programming
#                           -----------------------------------------------------

# --> Class and Objects in Python

# Class : class is a blueprint for creating  objects
 # Classs : class is a defination of object is that implrementation of class in the memory

# creating an class syntax
# class Student:
#     name = "Raj sharma"


# Creating a object ( instance )
# s1 = Student()
# print(s1.name)


# For example 

# class MotoGp:
#     name = "RacerNs"
#     speed = "400"
#     color = "Black"

# Deatails = MotoGp()
# print(Deatails.name)
# print(Deatails.speed)
# print(Deatails.color)






# --> __init__ Function
#     Constructor

# All class hava a function called _init_() , which is always executed when the object being initiated.

# Creating the class in constructor
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# Creating object in constructor
# s1 = Student("Raj")
# print(s1.name)


# *The self parameter is a refrence to the current instance ( object ) of the class , 
  #  and used to access varible that belongs to the class



#  Note --> If a is class and ob is its object then what is the data type of ob when a 
    # contains both integer and string data members 
    # Ans -> Inrespective of data type of data members of class object always contains the data 
             # the data type of its class name which means that a is the data type of object ob

  #  How does the concept of destructor works in python when constructor A of class name 
    #  is used for allocating the memory to object             

  # Since pytohn works on memory refrence it does not contain any destructor therefore the work of 
   # the work of destructor ( cleaning of memory ) is done by the automatic garbage collector AGC
   # of python     


#  Note --> In python we can create default constructor allocate memory but in user defined
#           constructor is to initialize the data members of class.

  # Special case constructor --> In python we do not use constructor which is for the same name of
                # the class this is because unlike other programming language python 
                # object creation and initialization is done which seprate methods. this provides
                # the separate code exectution and dependency is reduced. 
# -------------------------------------------------------------------------------------------------


# class BCA:
#     roll = 0
#     name = " "

#     def user(self):
#         self.roll = int(input("Enter your roll no : "))
#         self.name = input("Enter your name : ")

#     def show(self):
#         print(f"Roll no is -> {self.roll} \nName is -> {self.name}")
# stu1 = BCA()
# stu1.user()
# stu1.show()      

# stu2 = BCA()
# stu2.user()
# stu2.show()      



class BCA:
    roll = 0
    name = " "

    def _init_(self):
        self.roll = roll
        self.name = name

    def show(self):
        print(f"Roll no is -> {self.roll} \nName is -> {self.name}")

roll = int(input("Enter your roll no : "))
name = input("Enter your name : ")        
stu1 = BCA()
stu1.user()
stu1.show()      
