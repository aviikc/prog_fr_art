my_file = open("./buy.txt", "r")
my_var = my_file.read()
my_file.close()


# print(my_var)


#Second method of doing the same thing
with open("./buy.txt", "r") as my_file_b:
    my_var_b = my_file_b.read()
    # do something

print(my_var_b.split("\n"))
# print(type(my_var_b[0]))