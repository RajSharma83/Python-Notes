  # Syntax of lambda Function:
    # lambda argument : expression


  # lambda is a keyword to define the lambda function argummnets can be comma separated
   # list of input parameters just like regular function expression is a evaluated value of single 
   # line which is returned

# s1 = "Bca Department"
# res = lambda fun : fun.upper()
# print(res(s1))


# s1 = "Bca Department"
# s2 = "Hello Bca Department"
# res = lambda fun, fun2: fun.upper() + "\n" + fun2.lower()
# print(res(s1,s2))



# li = [lambda arg=x: arg*10 for x in range(1,5)]
# for i in li:
#     print(i())


# calc = lambda x,y: (x+y,x*y)
# result = calc(2,4)
# print(result)


# n = [12,45,78,86,33,66]
# even = filter(lambda x: x%2==0,n)
# print(list(even))


# n = [12,45,78,86,33,66]
# b=map(lambda x: x*10,n)
# print(list(b))





        # Differece between lambda and def keyword:
    #1. def is used for creating standard reuseable function where as lambda is used for 
    # creating short , one line , annomyous function.
    # 2. lambda can have single statement but def can multiple statement.
    # 3. def is capable of performing complex logic but lambda is for short and temporary logic     
