#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation of prices')
    print('(5) Find the day has maximum number of price')
    print('(6) Find if any price is lower than threshold')
    print('(7) Find the best investment')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
#funtion 3
def avg_price(prices):
    """ return the average price of a list prices
    input: prices is a list of 1 or more numbers.
    """
    total=0
    for i in prices:
        total+=i
    return total/len(prices)

#function 4
def std_dev(prices):
    """return the standard deviation of the prices
    input: prices is a list of 1 or more numbers.
    """
    avg = avg_price(prices)
    x=0
    for i in prices:
        x += (i - avg) ** 2
    y=x/len(prices)
    return math.sqrt(y)

#function 5
def max_day(prices):
    """ return the day has the maximum price
    input: prices is a list of 1 or more numbers.
    """
    index=0
    max_p=prices[0]
    for i in range(len(prices)):
        if max_p < prices[i]:
            max_p=prices[i]
            index = i
    return index

#function 6
def any_lower(prices,threshold):
    """ returns one boolean result to test whether there is a price lower than threshold
    input: prices is a list of 1 or more numbers.
    """
    for i in prices:
        if i< (threshold):
            return True
    return False

#funtion 7
def find_tts(prices):
    """return the best days on which to purchase and sell the stock within the prices list
     input: prices is a list of 1 or more numbers.
    """
    sell_day=1
    buy_day=0
    best=prices[sell_day]-prices[buy_day]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            diff=prices[j]-prices[i]
            if diff>best:
                best = diff
                buy_day=i
                sell_day=j
    return [buy_day,sell_day,best]


def tts():
    """ the main user-interaction loop
    """
    prices = []
    threshold = ''

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average_price = avg_price(prices)
            print("The average price is", average_price)
        elif choice == 4:
            standard_dev = std_dev(prices)
            print("The standard deviation is", standard_dev)
        elif choice == 5:
            max_d=max_day(prices)
            print("The max price is",prices[max_d],"on day ",max_d)
        elif choice == 6:
            threshold = eval(input('Enter a threshold: '))
            s =any_lower(prices,threshold)
            if s==False:
                print("There are no prices below", threshold)
            else:
                print("There is at least one price below", threshold)
        elif choice == 7:
            best_inv=find_tts(prices)
            print("Buy on day ",best_inv[0]," at price ", prices[best_inv[0]])
            print("Sell on day ",best_inv[1]," at price ", prices[best_inv[1]])
            print("Total profit:", best_inv[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
