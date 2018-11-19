# x = 11

# print ("first")
# print ("second")
# if x > 10:
#     print ("third")
# print ("fouth")
# print ("fifth")
# print ("sixth")
# print ("seventh")

# Create a list l.
# Loop through all the numbers from 1 to 5 (x) and with that, loop through all the numbers from 20 to 50 (y).
# At each tick of the loops, if y is a multiple of x, add True to the list l. Otherwise add False to the list.

# -----------------------------------------

# li = []

# for x in range(1,6):
#     for y in range (20,51):
#         if y % x == 0:
#             li.append(True)
#         else:
#             li.append(False)
       
# print(li)

# -----------------------------------

# li = []

# for x in range(1,6):
#     for y in range (20,51):
#         msg = "x is {0} and y is {1} the resutl is {2}".format(x, y, y % x ==0)
#         li.append(msg)

# print(li)

# -------------------------------------

# li = []

# for i in range (20):
#     if i%3 ==0:
#         li.append(i)
        
# print(li)


# li = [i for i in range (20) if i%3 ==0]

# print(li)

# ----------------------------------

# words = ["hello", "world", "this", "is", "a", "tough", "challenge"]

# output = []

# for word in words:
#     if not word.startswith("t"):
#         output.append(word.upper())
    
# print(output)


# words = ["hello", "world", "this", "is", "a", "tough", "challenge"]

# output = [w.upper() for w in words if not w.startswith("t")]

# print(output)

