        #  Q1. Library Fine Calculator (if / else) 
        #    A college library charges a fine if a student returns a book late. 
        #    • 1–5 days late → ₹10/day 
        #    • 6–10 days late → ₹20/day 
        #    • More than 10 days → ₹50/day 
        #   Write a program to calculate the fine. 
        #   Test Cases: 
        #   Input: 3  → Output: Fine=30   
        #   Input: 7  → Output: Fine=140   
        #   Input: 12 → Output: Fine=600  

# fine = 0
# day = int(input("Enter the Day : "))
# if day> 0 and day <= 5:
#     fine = day * 10
# if day > 5 and day<= 10:
#     fine = day * 20
# if day > 10:
#     fine = day * 50
# print("Fine = ", fine)



    # Q2. Multiplication Revision (recuesion) 
    #  A teacher asks the student to print all even numbers from 1 to n (user input) using recursion. 
    # Test Cases: 
    #  Input: 15   
    #  Output: 2 4 6 8 10 12 14   
    #  Input: 29   
    #  Output: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 
    #  Input: 4   
    #  Output: 2   


# def print_even_numbers(n):
#     if n <= 1:
#         return
#     if n % 2 == 0:
#         print_even_numbers(n - 2)
#         print(n, end=" ")
#     else:
#         print_even_numbers(n - 1)
# n = int(input("Enter a number: "))
# print_even_numbers(n)

   

        # Q3. Staircase Assignment (while loop) 
        #  A hostel staircase has n steps. A student climbs 2
        #  steps at a time until he reaches or crosses n. Print 
        #  the steps he lands on. 
        # Test Cases: 
        #  Input: 10 → Output: 2 4 6 8 10   
        #  Input: 7  → Output: 2 4 6   
        #  Input: 5  → Output: 2 4  

# n = int(input("Enter the number of steps: "))
# step = 2
# while step <= n:
#     print(step, end=" ")
#     step += 2

        

        # Q4. Canteen Queue (break, continue, pass) 
        #  Students are standing in a queue. If a student has ₹0 balance,
        #  skip them (continue). If balance < ₹20, 
        #  break (canteen closes for them). Otherwise, process order (pass). 
        #  Test Cases: 
        #   Input: [50, 0, 30, 10, 25]   
        #   Output: Processed → [50, 30]   
        #   Input: [100, 0, 0, 15, 50]   
        #   Output: Processed → [100]   
        #   Input: [20, 0, 25]   
        #  Output: Processed → [20]   

# money = list(map(int, input("Enter balances: ").split(",")))
# processed = []
# for balance in money:
#     if balance == 0:
#         continue
#     if balance < 20:
#         break
#     processed.append(balance)
# print("Processed :", processed)





    #    Q5. Hostel Room Pattern (Nested Loops) 
    #    Print a hostel room layout: floors and rooms. 
    #    Example: 2 floors, 3 rooms → 
    #    Floor 1: R1 R2 R3   
    #    Floor 2: R1 R2 R3   
    #   Test Cases: 
    #    Input: 2,3   
    #   Output:  
    #  Floor 1: R1 R2 R3   
    #  Floor 2: R1 R2 R3   

# floors = int(input("Enter the number of floors: "))
# rooms = int(input("Enter the number of rooms per floor: "))
# for floor in range(1, floors + 1):
#     print(f"Floor {floor}: ", end="")
#     for room in range(1, rooms + 1):
#         print(f"R{room}", end=" ")
#     print()





    #   Q6. College Email Validator (Strings) 
    #   Check if a student email is valid (must end with @college.edu). 
    #   Test Cases: 
    #   Input: "ram@college.edu"   → Output: Valid   
    #   Input: "neha@gmail.com"    → Output: Invalid   
    #  Input: "amit@college.edu"  → Output: Valid   

# email = input("Enter your email: ")
# if email.endswith("@college.edu"):
#     print("Valid")
# else:
#     print("Invalid")


