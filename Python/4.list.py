   #  .sort() is a method in python use as an object attribute that makes the changes required
    #   in the orignal collection and not changing for new instance



    # WAP to find the gratest number among the three list items of integer data type.
    
# list1 = [3, 5, 7]
# list2 = [8, 12, 6]
# list3 = [4, 9, 2]
# great = max(max(list1), max(list2), max(list3))
# print("The greatest number is:", great)

# list = [8, 12, 6]
# great = max(list)
# print("The greatest value is : ",great)


     # Second largest value
# list = [8, 12, 6,18,56]
# list.sort(reverse=True)
# print("The greatest value is : " , list[1])



       # 2D list 

     # Print the 3 from 2D list :
# list2d = [[5,9,7],[4,3,12],[11,55,50]]  
# print(list2d)     
# print(list2d[1][1])


# list2d = [[5,9,7],[4,3,12],[11,55,50][39,78,88],[20,30,40]]  
# print(list2d)     
# print(list2d[2][1])
# print(list2d[1:4])     # it print the  1 to 3 index and it is written 4 because it run -1 index


    # It is only possible to implement slicing for the row of 2s list only slicing cannot be implemented
    #  in the columns of 2d lsit directly




       # WAP to creat a 2D list of size 5*5 then take a user input of an interger less then 
         # 5 and print the row of particular index.

       # WAP to create a list of 3 string elements and print the longest string among them.


# list2D = [ [1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]
# ]

# print("Matrix of 5*5:")
# print(list2D[0])
# print(list2D[1])
# print(list2D[2])
# print(list2D[3])
# print(list2D[4])
# index = int(input("Enter an integer less than 5 to select a row: "))
# if 0 <= index < 5:print(f"Row at index {index}: {list2D[index]}")
# else: print("Invalid index! Please enter an integer between 0 and 4.")





# str = ["apple", "banana", "cherry"]
# longest_str = "" 
# for s in str:
#     if len(s) > len(longest_str):
#         longest_str = s
# print("The longest string is:", longest_str)
