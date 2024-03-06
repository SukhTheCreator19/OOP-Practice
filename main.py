# __________________________________Class Variables and Instance Variables_____________________________________

# class Employee:

#   num_of_emps = 0
#   raise_amount = 1.04

#   def __init__(self, first, last, pay):
#     self.first = first
#     self.last = last
#     self.pay = pay
#     self.email = first + '.' + last + '@company.com'

#     Employee.num_of_emps += 1  ##within the employee init method, we are incrementing the num_of_emps by 1 because we know that we are adding more and more employees.  Since we dont want to override the num_of_emps variable we dont use the self syntax because we dont want to change the num_of_emps variable.  We are just adding to it.

#   def fullname(self):
#     return '{} {}'.format(self.first, self.last)

#   def apply_raise(self):
#     self.pay = int(self.pay * self.raise_amount)  ## self is the instance of a attribute. So self.pay looks for the
## instance where the attribute is self.pay is located and looks at the value of self.pay and multiplies it by the
## raise amount.

# emp_1 = Employee('Corey', 'Schafer', 50000)  ## we define an object called emp_1 and we pass in the first, last and pay to the
## be used as the attributes of the class.
# emp_2 = Employee('Test', 'User', 60000)  ## we define an object called emp_2 and we pass in the first, last and pay to the and do the same thing as what we just did above.

# print(Employee.num_of_emps)  ## here we are just printing the number of employees that we have by adding 1 to the number of employees everytime an employe object is created.

#--------------------------------------------------------------------------------------------------------

# __________________________________Classmethods and Staticmethods_______________________________________

## class methods are alternative constructors

##static methods dont pass the intances nor the class but they behave like class methods.  They are used to create utility functions that dont need access to the class and they are used more for logic than anything else. These are used when we want a function to tell us something but the function itself doesnt need to know anything about the class.
# class Employee:

#   num_of_emps = 0
#   raise_amount = 1.04

#   def __init__(self, first, last, pay):
#     self.first = first
#     self.last = last
#     self.pay = pay
#     self.email = first + '.' + last + '@company.com'

#     Employee.num_of_emps += 1

#   def fullname(self):
#     return '{} {}'.format(self.first, self.last)

#   def apply_raise(self):
#     self.pay = int(self.pay * self.raise_amount)

#   @classmethod  ## here we are adding a decorator to the classmethod.  This decorator is used to modify the class itself.  This is a class method.
#   def set_raise_amt(cls, amount):  ## here we are adding a cls parameter to the classmethod.  This is the class itself. and addint the amount into it.
## cls is used to change all the values of the each object.

#     cls.raise_amount = amount  ## here we are tapping into the class employee and changing the instance, cls, where tha raise_amount is found, and chainging it to the amount the user passes in.
## this raises the amount of all the objects in the employee class without needing to tap into each employee individually.

## the method allows us to go from this
# Employee.raise_amount = 1.05
#  to
#  Employee.set_raise_amt(1.05)

#   @classmethod
## here we are creating a new classmethod and what we want to be able to do with this class method is have a string that is inputed and after that string is inputed a certain way, like this: 'Sukhmaan-Sighn-30000', we want to make it into an employee object where the seperation are the - and the first and last name are the first and last name and the pay is the last number.

#   def from_string(cls, emp_str):  ## here we are making another classmethod that is uses the class employee and a employee string as parameters
## here we are working with the class rather than the instance

#     first, last, pay = emp_str_1.split('-')  ## we are going to split the string in every instamce where the - is present, the value that each thing will have is first, last, pay.
#     return cls(first, last, pay)  ## than we want to make sure that this function returns the class Employee with the first, last, pay so it can be used later on. Imagine this return was written like this
## employee_1 = Employee(first, last, pay)
## instead of this, now that we have the function above we can do something that looks more like this:
## emp_str_1 = 'John-Doe-70000'
## emp_str_2 = 'Steve-Smith-30000'
## emp_str_3 = 'Jane-Doe-90000'

## new_emp_1 = Employee.from_string(emp_str_1)

## this is better since the user can input the data for us and all we need to do is call the classmethod function to organize the data so that it works with our Employee class.

## static methods are different than class methods because they dont have access to the class or the instance.  They are just a function that is not associated with
#   @staticmethod
#   def is_workday(day):
#     if day.weekday() == 5 or day.weekday() == 6:
#       return False
#     return True

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)

# import datetime
# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))


# ________________________________________________Inheritance____________________________________________________
class Employee:

  num_of_emps = 0
  raise_amount = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = lastssss
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
  raise_amount = 1.10

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang


class Manager(Employee):

  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_emps(self):
    for emp in self.employees:
      print('--->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
print(mgr_1.fullname())

# print(help(Developer)) ##Everything there is in the Developer class is in the Employee class. This is inheritance. The Developer class is inheriting the Employee class. The Developer class is a child class of the Employee class.
