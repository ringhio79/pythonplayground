# d = {
#     "Richard": 10,
#     "Katie": 11,
#     "Steve": 25,
#     "Gijs": 15,
#     "Giselle": 18,
#     "Stein": 23,
#     "Daan": 56,
#     "Dimitar": 45
# }


# # Just the keys in the dictionary
# for i in d:
#     print(i)
    

# # Keys and values in the dictionary
# for i in d.items():
#     print(i)


# # Just the values in the dictionary
# for i in d.values():
#     print(i)


# # Keys and values in the dictionary, in their own variables
# for name, age in d.items():
#     print("The key is {0} and the value is {1}".format(name, age))
    



# for k in range (10, 31):
    
        
d = {k:k%4==0  for k in range (10,31)}

print(d)