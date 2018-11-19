# print('Hello World')
# print('Welcome To Python')

# name = input("What is your name?")
# print("hello " + name)

# x = int(input("pick a number"))
# y = int(input("pick another number"))
# print(x + y)

# string = input('please type something: ')
# print(string.upper())

# string = input('type in caps: ')
# print(string.lower())

# string = input("type something here")
# print(string.title())

# s = input("say something here")
# str = ''

# for i in s:
#     str = i + str
# print(str)

# num1 = int(input('enter a number here '))

# if num1 <= 10:
#     print('small')
# else:
#     print('big')
    
# num1 = int(input('enter a random number'))
# num2 = int(input('enter another number'))

# if num1 == num2:
#     print('same')
# else:
#     print('different')


# num1 = int(input('please enter a number '))

# if num1 == 1:
#     name = (input("what is your name? "))
    
#     print("your name is " + name)
    
# if num1 == 2:
#     age = (input('how old are you? '))
    
#     print("your age is " + age)

# num1 = int(input('enter a number'))
# num2 = int(input('enter a number'))
# num3 = int(input('enter a number'))
# num4 = int(input('enter a number'))
# num5 = int(input('enter a number'))
# num6 = int(input('enter a number'))
# num7 = int(input('enter a number'))
# num8 = int(input('enter a number'))
# num9 = int(input('enter a number'))
# num10 = int(input('enter a number'))

# print(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)

# total = 0
# for i in range(10):
#     a = int(input("Enter a number: "))
#     total += a

# print(total)

# l = [1,2,3,4,5]


# for i in range(11):
#     print(i)

# total = 0
# for i in range(10):
#     a = int(input('enter a number: '))
#     total += a
    
# print(total)

# def add(a,b):
#     return(a + b)

# print(add(3,5))   



# def add():
#     a = int(input('enter a number '))
#     b = int(input('enter another number '))
#     return a+b
    
# print(add())

# def checkevenorodd(n):
#     if (n % 2 == 0):
#         return "even"
#     else:
#         return "odd"

# print(checkevenorodd(7))

# def message():
#     return "this is the message"

# print(message())
# print(message)

#  NO 57
# newlist = []

# for numbers in range(1,7):
#     newlist.append(numbers)

# print(newlist)

# print(sum(newlist))

# my_list = [1,2,3,4,5,6]
# result = 0

# for n in my_list:
#     result +=  n 

# print(result)


# NO 58
# # print(list(range(100)))

# NO 59

# print(list(range(10, 52, 2)))

# NO 60

# my_list_of_lists = [[0], [0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]

# num_at_location = my_list_of_lists[4][2]

# print(num_at_location)
    
# NO 61
even_nos = []

for n in range(11):
    if n % 2 == 0:
        even_nos.append(n)
        
print(even_nos)
        

# or

# even_nos = []

# for n in range(2,12,2):
#         even_nos.append(n)
        
# print(even_nos)
    
# NO 62

# my_list = ['apple', 'orange', 'lemon', 'grapfruit', 'pear']

# print(my_list[2])

# NO 63 & 64

# student1 = {'name':'Guido', 'age':64, 'nationality':'Dutch', 'subjects':['English', 'History', 'Drama', 'Physics']}
# student2 = {'name':'Tom', 'age':38, 'nationality':'Maltese', 'subjects':['English', 'History', 'Drama', 'Physics']}
# student3 = {'name':'Rachel', 'age':67, 'nationality':'Belgian', 'subjects':['English', 'History', 'Drama', 'Physics']}
# student4 = {'name':'Mac', 'age':34, 'nationality':'Italian', 'subjects':['English', 'History', 'Drama', 'Physics']}

# my_student_list = []

# my_student_list.append(student1)
# my_student_list.append(student2)
# my_student_list.append(student3)
# my_student_list.append(student4)

# my_student_dict = {}

# for the_student in my_student_list:
    
#     my_student_dict[the_student['name']] = the_student
    
# print(my_student_dict)

# updating a dictionary

# student1 = {'name':'Guido', 'age':64, 'nationality':'Dutch'}

# student1['sport'] = 'football'

# print(student1)