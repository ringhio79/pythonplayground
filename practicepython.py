# Challenge 1 Character input

# name = input ("what is your name? ")
# age = int(input ("how old are you? "))
# year = str((2018 - age) + 100)
# number = int(input ("what's your favourite number? "))
# output = "hi " + name + " you will be 100 in " + year + "\n"
# print (output * number)

# Challenge 2 - Odd Or Even

# number = int (input ("Choose a number? "))
# if number % 2 == 0:
#     print ("This is an even number")
# if number % 4 == 0:
#     print("this is an even number divisble by 4")
# else:
#     print ("odd")
    
# num = int(input("Enter a number "))
# check = int(input("check if divisible by "))
# if num % check == 0:
#     print ("number divides evenly")
# else:
#     print ("number is not divisble")


# challenge 3 List Less Than Ten

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# newlist = []

# for num in a:
#     if num < 5:
#         newlist.append(num)
#         print (newlist)

# OR 

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# print ([num for num in a if num < 5])


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# check = int(input(" 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 \n Which of these numbers is divisble by (enter a number)"))
# new_list = []

# for i in a:
#     if i % check == 0:
#         new_list.append(i)
#         print (new_list)

# challenge 4 Divisors

# num = int(input("Choose a number to find it's divisors: "))
# max_num = num+1
# div_by = range(2,max_num)
# divisors = []


# for i in div_by:
#     if num % i == 0:
#         divisors.append(i)
# print(divisors)



# # Challenge 5 List overlap

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# blended_list = []

# for i in a:
#     if i in b:
#         if i not in blended_list:
#             blended_list.append(i)
# print (blended_list)

    
    
# import random
# a=[]
# b=[]
# blended_list = []

# for x in range(10):
#   a.append(random.randint(1,21))
#   b.append(random.randint(1,21))
  
#   for i in a:
#       if i in b:
#           if i not in blended_list:
#               blended_list.append(i)
# print (a)
# print (b)
# print (blended_list)

# Challenge 6

# simon_says = input("Please write a word here: ")

# if simon_says[::-1] == simon_says[0:]:
#     print ("this is a palindrome")
# else:
#     print("this is not a palindrome")
    
    
# Challenge 7

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even=[]
# for i in a:
#     if i %2==0:
#         even.append(i)
# print(even)

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even = [i for i in a if i%2== 0]
# print(even)


# Challenge 8 - Rock paper scissors

player_1 = input("P1 choose your weapon (R=rock, P=paper or S=scissors)\n").upper()
player_2 = input("P2 choose your weapon (R=rock, P=paper or S=scissors)\n").upper()

if player_1 == player_2:
    print ("No win, play again")
if (player_1 == "R" and player_2 == "S") or ( player_1 == "S" and player_2 == "P") or ( player_1 == "P" and player_2 == "R"):
    print ("Player 1 wins")
else:
    print ("Player 2 wins")
