#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month=init_month
        self.day=init_day
        self.year=init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    
# Question 3
    def advance_one(self):
        """change the date to the next day based on the calendar.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29
        if self.day != days_in_month[self.month]:
            self.day+=1
        else:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year+=1
            else:
                self.month+=1
                self.day = 1
# Question 4
    def advance_n(self, n):
        """ change the date to n days later by using previous method and loop
        """
        print(self)
        while n !=0:
            self.advance_one()
            print(self)
            n-=1

# Question 5
    def __eq__(self, other):
        """test if self and other have the same day, month, and year
        """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False

# Question 6
    def is_before(self, other):
        """ returns if called object represents a calendar date that occurs 
        before the calendar date that is represented by other.
        """
        if other.year > self.year:
            return True
        elif other.year < self.year:
            return False
        else:
            if other.month > self.month:
                return True
            elif other.month < self.month:
                return False
            else:
                return other.day > self.day

# Question 7
    def is_after(self, other):
        """ returns if called object represents a calendar date that occurs 
        after the calendar date that is represented by other.
        """
        if other.year > self.year:
            return False
        elif other.year< self.year:
            return True
        else:
            if other.month < self.month:
                return True
            elif other.month > self.month:
                return False
            else:
                return other.day < self.day

# Question 8
    def days_between(self, other):
        """ return the days before other. If self happens before other, return
        a negative number, else return a positive number.
        """
        new_self=self.copy()
        new_other=other.copy()
        days=0
        while not new_self.__eq__(new_other):
            if new_self.is_before(new_other):
                new_self.advance_one()
                days-=1
            else:
                new_other.advance_one()
                days+=1
        return days

# Question 9
    def day_name(self):
        """ return the name of day based on a day we already now
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        other= Date(11, 9, 2020)
        diff = self.days_between(other)
        d=diff % 7
        return day_names[0+d]