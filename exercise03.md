## Exercise 03

1. The list of non-negative integers that are [5,10,7,14,25,36] . Print the square of each number.
   eg for [1,2,3,4] the output would be
   1
   4
   9
   16
2. Write a function called showNumbers that takes a parameter called limit.
   It should print all the numbers between 0 and limit with a label to
   identify the even and odd numbers. For example, if the limit is 3, it
   should print:
   0 EVEN
   1 ODD
   2 EVEN
   3 ODD
3. Write a function called raindrops that takes a number.

   - If the number is divisible by 3, it should return “Pling”.
   - If it is divisible by 5, it should return “Plang”.
   - If it is divisible by both 3 and 5, it should return “PlingPlang”.
   - If it is divisible by by 7, it should return "Plong"
   - If it is divisible by both 7 and 5, it should return “PlongPlang”.
   - If it is divisible by both 7 and 3, it should return “PlongPling”.
   - If it is divisible by both 7, 5 and 3, it should return “PlongPlangPling”.
   - Otherwise, it should return the same number.

4. Given a year, write a function that outputs if it is a leap year.
   Condition for leap year:
   on every year that is evenly divisible by 4
   except every year that is evenly divisible by 100
   unless the year is also evenly divisible by 400

5. Given the list ["nail", "shoe",
   "horse", "rider",
   "message", "battle",
   "kingdom"],
   you will output the full text of this proverbial rhyme.
   For want of a nail the shoe was lost.
   For want of a shoe the horse was lost.
   For want of a horse the rider was lost.
   For want of a rider the message was lost.
   For want of a message the battle was lost.
   For want of a battle the kingdom was lost.
   And all for the want of a nail.

6. Create classes from the following class diagrams:
   ![Class Diagrams](/images/classes.png)

I have solved problem A as an example

```
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    return 3.14159*(self.radius**2)

  def get_circumference(self):
    return 2*3.14159*self.radius

# An example of use

new_circle = Circle(6)

print(new_circle.get_circumference())  #This prints the circumferance

print(new_circle.get_area())  #This prints the area of the circle

```
