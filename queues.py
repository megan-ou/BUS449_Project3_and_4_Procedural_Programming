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
    if not isiterable(lamda):
        lamda = (lamda,)

    if not all([isinstance(lamda[i],Number) for i in range(len(lamda))]):
        return False

    if not all([lamda[i]>0 for i in range(len(lamda))]):
        return False

    #Check to see if mu is a number
    if not isinstance(mu, (int, float)):
        return False

    #Check to see if c is a number
    if not isinstance(c, (int, float)):
        return False

    if mu < 0:
        return False

    if c < 0:
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

    if not is_valid(lamda, mu, c):
        return False

    lamda_sum = 0

    if isiterable(lamda):
        lamda_sum = sum(lamda)
    else:
        lamda_sum = lamda

    rho = 0
    rho = lamda_sum/(c * mu)

    if rho <= 0:
        return False

    if rho > 1:
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

    #calculate r, the expected number of people in service
    r = lamda / mu

    #calculate rho, the traffic intensity
    rho = r / c

    p0 = 0

    #Single server queue calculation
    if c == 1:
        p0 = 1 - rho

    #Multi server queue calculation
    else:
        #Split the equation into three different parts
        #Calculate the 1st term (summation) in the p0 equation
        for n in range (c):
            p0 += ((r ** n) / (math.factorial(n)))
        #Calculate the 2nd term in the p0 equation
        p0 += ((r^c) / (math.factorial(c) * (1 -rho)))
        #Raise the entire equation to the -1 power
        p0 = (p0) ** (-1)

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

    #Initialize variables for calculating Lq
    lq = 0
    r = lamda / mu
    rho = r / c
    p0 = calc_p0(lamda, mu, c)

    #Single server queue calculation
    if c == 1:
        lq = (lamda ** 2) / (mu * (mu - lamda))

    #Multi server queue calculation
    else:
        lq = (r ** c) * rho / (math.factorial(c) * ((1 - rho) ** 2)) * p0

    return lq

