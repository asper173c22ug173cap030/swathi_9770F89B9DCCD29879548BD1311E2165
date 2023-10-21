 # 1.1 Implement a recursive function to calculate the factorial of a given number.

"""
1! = 1 x 1
2! = 2 x 1! --->2 x 1
3! = 3 x 2! --->3 x 2 x 1
.
.
10! = 10 x 9! ---> 10 x 9 x 8 x... x 1

Formula - n x (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number = int(input("Enter a value : "))
res = fact_rec(number)

print("The factorial of {} is {}.".format(number,res))
# Leap year

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("Enter a year : "))

if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
print('{} is not a leap year.'.format(year)) 
'''Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance. Include methods to
deposit money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:
  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_…
 '''Implement a class called Player that represents a cricket player. The Player class should have a
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and
Bowler, from the Player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''


# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
 …
 """
Write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found, or an empty list if the product is not
found.
"""


def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sort…