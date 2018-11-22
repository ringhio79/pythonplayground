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

num = int(input("Choose a number to find it's divisors: "))
max_num = num+1
div_by = range(2,max_num)
divisors = []


for i in div_by:
    if num % i == 0:
        divisors.append(i)
        print(divisors)
    
    

