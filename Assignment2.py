    #  Q1. String Reversal Problem Statement: 
    #   Write a program that takes a string and returns its reverse. 

# str = input("Enter the string to reverse :")
# rev = str[::-1]
# print(rev)


    #  Q2. Count Vowels in String Problem Statement: 
    #     Given a string, count the number of vowels (a, e, i, o, u). 
    #   Input Format: 
    #    • A string. 
    #   Output Format: 
    #   • Integer (count of vowels). 

# text = input("Enter the string : ")
# count = 0
# for char in text:
#     if char in 'aeiouAEIOU':
#         count += 1
# print(count)


    # Q3. List Square Elements Problem Statement: 
    #  Write a function that takes a list of integers and returns a new list containing
    #  the square of each element. 
    #  Input Format: 
    #  • List of integers. 
    #  Output Format: 
    #  • List of squared integers. 

# numbers = [1,2,3,4]
# squares = []
# for num in numbers:
#     squares.append(num * num)
# print(squares)



        # Q4. Maximum in Tuple Problem Statement: 
        #  Given a tuple of integers, return the maximum element. 
        #  Input Format: 
        #  • Tuple of integers. 
        #  Output Format: 
        #  • Integer (max value).

# tup = input("Enter integers : ")  
# input_tuple = tuple(map(int, tup.split(' ')))
# maxi = max(input_tuple)
# print("Maximum value:", maxi)





    #    Q5. Dictionary Word Frequency Problem Statement: 
    #      Write a program to count the frequency of each word in a given sentence using a dictionary. 
    #    Input Format: 
    #   • A string (sentence). 
    #   Output Format: 
    #   • Dictionary with word counts.

# sentence = input("Enter a sentence: ")
# sentence = sentence.lower()
# words = sentence.split()
# word_freq = {}
# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
# print(word_freq)






    #    Q6. Default and Variable-Length Arguments 
    #      Problem Statement: 
    #      Write a function student_info that accepts name (mandatory), age (default = 18), and 
    #      variable-length subjects. Return a formatted string. 
    #      Input Format: 
    #      • Name, (optional age), multiple subjects. 
    #      Output Format: 
    #      • String with details.












    # Q7. Returning Multiple Values 
    #  Problem Statement: 
    #  Write a function that takes two numbers and returns their sum and product using a tuple. 
    #  Input Format: 
    #  • Two integers. 
    #  Output Format: 
    #  • Tuple (sum, product). 

