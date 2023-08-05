'''
CS 115, Inheritance Activity
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement missing sections of the Employee class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Employee(object):
    def __init__(self, first, last, title, hours, rate):
        self.__first_name = first
        self.__last_name = last
        self.__title = title
        self.__hours_per_week = hours
        self.__hourly_rate = rate
    '''Write the constructor below. It should take in five arguments:
       - first_name (a string)
       - last_name (a string)
       - title (a string)
       - hours_per_week (an int)
       - hourly_rate (a float)
       All fields must be private. No error checking or type conversions
       are required.'''

    '''Write a getter for hourly_rate.'''
    def get_hourly_rate(self):
        return self.__hourly_rate

    '''Write a setter for hourly rate.'''
    def set_hourly_rate(self, r):
        self.__hourly_rate = r

    '''Write a method called get_total_compensation.
       It returns the total amount of money an employee earns in a year.
       Assume that the employee works 50 weeks each year, with the remaining
       2 set aside for vacation.'''
    def get_total_compensation(self):
        return self.__hours_per_week * self.__hourly_rate * 50

    def __str__(self):
        return 'Employee: %s %s\n  Title: %s\n  Hours per week: %d\n' \
               '  Hourly rate: $%.2f\n  Yearly compensation: $%.2f' % \
            (self.__first_name, self.__last_name, self.__title, \
             self.__hours_per_week, self.__hourly_rate, \
             self.get_total_compensation())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement missing sections of the Manager class. Manager should be a
' subclass of Employee.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Manager(Employee):
    
    def __init__(self, first, last, title, hours, rate, bonus):
        super().__init__(first, last, title, hours, rate)
        self.__bonus_percent = bonus
    '''Write the constructor below. It should take in six arguments:
    - the first five are the same as in the Employee constructor
    - bonus_percent, a float >= 0. This attribute represents the percentage
      of the employee's yearly compensation that will be used to
      create the manager's annual bonus.'''

    '''Override the method get_total_compensation.
    It returns the total amount of money the manager earns in a year, i.e.
    basic employee compensation + bonus.
    Your implementation should call get_total_compensation in class Employee.
    Note: If a manager's yearly compensation is $100,000 and the bonus_percent
          is 10 (ten), the total compensation will be 110,000.'''
    def get_total_compensation(self):
        money = super().get_total_compensation()
        return money + money*(self.__bonus_percent / 100)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' A rudimentary test.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test():
        m = Manager("Greta", "Thunberg", "Climate Change Leader", 50, 20.0, 10.0)
        print(m.get_total_compensation())
        m.set_hourly_rate(m.get_hourly_rate() + 20) # she earned it 
        print(m) # This will call Employee.__str__ which will call Manager.get_total_compensation
                 # She's making 110,000.00

test()
