import math
from toolz import isiterable
from numbers import Number
#queues.py
#Calculates the average number of people in queue (L_q) for an M/M/C queue
#@Author Megan Ou, Toby Okoji
#@Version September 2025

def is_valid(lamda, mu, c = 1):
    """
    Checks to see if all arguments are numerical scalars.
    Checks to see if value of arguments are within the valid range.
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: True if all arguments are valid, False if any argument is invalid
    """
    #Check to see is lamda is iterable. If lamda is a single value, bundle it into a single
    # value tuple so that we can treat all cases of lamda the same
    if not isiterable(lamda):
        lamda = (lamda,)

    #Check to see if all values of lamda are numbers
    if not all([isinstance(lamda[i],Number) for i in range(len(lamda))]):
        return False

    #Check to see if all values of lamda are greater than zero
    if not all([lamda[i]>0 for i in range(len(lamda))]):
        return False

    #Check to see if mu is a number
    if not isinstance(mu, (int, float)):
        return False

    #Check to see if c is a number
    if not isinstance(c, (int, float)):
        return False

    #Check to see if mu and c are within the valid ranges
    if mu <= 0:
        return False

    if c <= 0:
        return False

    else:
        return True



def is_feasible(lamda, mu, c = 1):
    """
    Calculates rho (ρ) and checks to see if the value of rho is feasible.
    rho must be a value between 0 and 1.
    rho = lamda / mu * c
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: True if rho is feasible False if rho is not feasible
    """
    #Check to see if all values are valid
    if not is_valid(lamda, mu, c):
        return False

    #Check to see if lamda is iterable and sum lamda up if it is
    if isiterable(lamda):
        lamda = sum(lamda)

    #Calculate rho based on lamda
    rho = 0
    rho = lamda / (c * mu)

    #Check to see if 0 < rho < 1
    if rho <= 0:
        return False

    if rho >= 1:
        return False

    else:
        return True


def calc_p0(lamda, mu, c=1):
    """
    Calculates the probability that there is no one in the system (empty system).
    There are two different calculations depending on queue type.
    For single server queues, p0 = 1 - rho.
    For multi-server queues, p0 = ( ∑((r^n/n!)) + r^c/(c!*(1-rho)) ) ** -1
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: Probability of an empty queue
    """
    #check to see if lamda, mu, and c are numerical scalars and within a valid range
    if not is_valid(lamda,mu,c):
        return math.nan

    #check to see if rho is within feasible range
    if not is_feasible(lamda, mu, c):
        return math.inf

    #check if lamda is iterable and sum it up if it is not
    #for some reason (I cannot figure out why) sum() function reads sum as an unknown variable
    # and throws error: UnboundLocalError: cannot access local variable 'sum' where it is
    # not associated with a value
    #I will manually sum up lamda with a list comprehension. I tried googling the issue and
    # cannot seem to find a fix. sum() works everywhere else in this file
    # I cannot for the life of me figure out why it chooses not to work HERE
    #Originally did list comprehension [lamda_sum += lamda[i] for i in range(len(lamda))]
    # but the program doesn't like that either!!!
    if isiterable(lamda):
        lamda_sum = 0
        for i in range (len(lamda)):
            lamda_sum += lamda[i]
        lamda = lamda_sum

    #calculate r, the expected number of people in service
    r = lamda / mu

    #calculate rho, the traffic intensity
    rho = lamda / (mu * c)

    p0 = 0

    #Single server queue calculation
    if c == 1:
        p0 = 1 - rho

    #Multi server queue calculation
    else:
        # Split the equation into three different parts
        # Calculate the 1st term (summation) in the p0 equation
        term_1 = 0
        for i in range(0, c):
            term_1 += (r ** i) / math.factorial(i)

        # Calculate the 2nd term in the p0 equation
        term_2 = (r ** c) / (math.factorial(c) * (1 - rho))

        # Raise the entire equation to the -1 power
        sum = term_1 + term_2
        p0 = sum ** (-1)

    return p0


def calc_lq_mmc(lamda, mu, c=1):
    """
    Calculates the Lq, or average number of people waiting in the queue, for an M/M/C type
    queue. There are two different calculations depending on queue type.
    For single server queues, Lq = lamda^2/(mu*(mu-lamda))
    For multi-server queues, Lq = r^c*rho/(c!*(1-rho)^2)*p0
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: average number of people waiting in the queue
    """
    #check to see if lamda, mu, and c are numerical scalars and within a valid range
    if not is_valid(lamda, mu, c):
        return math.nan

    #check to see if rho is within feasible range
    if not is_feasible(lamda, mu, c):
        return math.inf

    # check to see if lamda is iterable and if so, take the sum of lamda
    if isiterable(lamda):
        lamda = sum(lamda)

    #Initialize variables for calculating Lq
    lq = 0
    r = lamda / mu
    rho = lamda / (mu * c)
    p0 = calc_p0(lamda, mu, c)

    #Single server queue calculation
    if c == 1:
        lq = (lamda ** 2) / (mu * (mu - lamda))

    #Multi server queue calculation
    else:
        #Split up equation so it is easier to read
        lq_numerator = (r ** c) * rho
        lq_denominator = math.factorial(c) * ((1 - rho) ** 2)
        lq = (lq_numerator / lq_denominator) * p0

    return lq

