               # 1. Pattern right angle traingle
                #  *
                #  * *
                #  * * *
                #  * * * *
                #  * * * * *

 
# for i in range(5):
#     for j in range(5):
#         if j<=i: 
#          print("*",end= "")
#         else: 
#          print()
#          break   




          # 2. Reverse right angle pattern:
                    #          *
                    #        * *
                    #      * * *
                    #    * * * * 
                    #  * * * * * 

# for i in range(5):
#     for j in range(5):
#       if i+j<4:
#          print(" ",end="")
#       else:
#          print("*",end="")
#     print()     




                   # 3. Piramid Pattern
                        #         *
                        #       * * *
                        #     * * * * *
                        #   * * * * * * *
                        # * * * * * * * * *


# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()   



                # 4. Reverse Piramid Pattern         
                        #  * * * * * * * * *
                        #    * * * * * * *
                        #      * * * * *
                        #        * * * 
                        #          *
                               


# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(2*(5 - i)-1):
#         print("*", end="")
#     print()




               # 5. Left side stairs
                  #       *
                  #      *
                  #     *
                  #    *
                  #   *

# for i in range(1, 5+ 1):
#     for j in range(5 - i):
#         print(" ", end="")
#     print("*")

     




         # 6. Right side stairs 
             #  *
             #   *
             #    *
             #     *
             #      *     

# for i in range(1, 5 + 1):
#     for j in range(i - 1):
#         print(" ", end="")
#     print("*")



            # 7. Kaju katli ( Diamond )
               #      *    
               #     * *   
               #    *   *  
               #   *     * 
               #  *       *
               #   *     * 
               #    *   *  
               #     * *   
               #      *    

# for i in range(1,5+1):
#     for j in range(1,2*5):
#         if j == 5 - i + 1 or j == 5 + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(5-1, 0,-1):
#     for j in range(1,2*5):
#         if j == 5 - i + 1 or j == 5 + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()





          #  Print the pattern of our  initail letter  of our name:
        
            #   ******
            #   *     *
            #   *     *                                        ********
            #   *    *                    *                        *      
            #   *   *                    * *                       *
            #   * *                     *   *                      *
            #   *   *                  * * * *                     * 
            #   *    *                *       *                    *
            #   *      *             *         *             ******* 

n = 7 
m = n // 2  

for i in range(n):
    for j in range(n):
        if j == 0:
            print("R", end="")
        elif i == 0 and j < n - 1:
            print("R", end="")
        elif i == m and j < n - 1:
            print("R", end="")
        elif j == n - 1 and i < m and i != 0:
            print("R", end="")
        elif i - j == m - 1:
            print("R", end="")
        else:
            print(" ", end="")
    print()


n = 5
for i in range(n):
    for j in range((2 * n) - 1):
        if j == n - i - 1 :
            print("A" , end="")
        elif j == n + i - 1:
            print("A" , end="")
        elif i == n // 2 and n - i - 1 < j < n + i - 1:
            print("A" , end="")
        else:
            print(" " , end="")
    print()


for i in range(7):
    for j in range(5):
        if i == 0:
            print("J", end="")
        elif i < 6 and j == 2:
            print("J", end="")
        elif i == 6 and (j == 0 or j == 1 or j == 2):
            print("J", end="")
        else:
            print(" ", end="")
    print()




    


          




