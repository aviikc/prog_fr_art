import math
print("Hello World!")


# variables

# datatypes

# functions


def distance_between_points(point_1, point_2):
    distance = math.sqrt(point_1**2 + point_2**2)
    print(f'distance is {distance}')
    if 4 < distance < 5:
        print("Between 4 and 5")
        if distance < 4.5 and distance > 4:
            print("Value between 4 and 4.5")
    elif distance > 3 and distance < 4:
        print("Between 3 and 4")
    elif distance > 2 and distance < 3:
        print("Between 2 and 3")
    elif distance > 0 and distance < 2:
        print("Between 0 and 2")
    else:
        print("invalid")
    # return distance


print(distance_between_points(3.2, 3))


print("__"*20)

# For Loop

my_attendance = ['adwait', 'ayush', 'adithya', 'rizil', 'nabankur']

# is ayush present in my_attendance

# [1..20] sum of these

print("__"*40)


list_of_numbers = [i for i in range(21)]
place_holder = 0
sum = 0

while place_holder <= len(list_of_numbers):
    sum = sum + place_holder
    place_holder = place_holder + 1

print(f'Sum is {sum}')
