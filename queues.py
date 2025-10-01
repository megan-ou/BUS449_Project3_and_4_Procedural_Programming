import math
from toolz import isiterable
from numbers import Number
#queues.py
#Calculates the average number of people in queue (L_q) for an M/M/C queue
#@Author Megan Ou, Toby Okoji
#@Version September 2025

def is_valid(lamda, mu, c = 1):
    """
    Checks to see if all arguments are numerical.
    Checks to see if value of arguments are within the valid range for queue calculations.
    Streamlined version of is_valid that is used was given to us as feedback by Dr. Mitchell.

    Args:
        lamda: arrival rate of customers per time interval (scalar or multivalued)
        mu: service rate per time interval (scalar)
        c: number of servers in the system (scalar)

    Returns: True if all arguments are valid, False if any argument is invalid
    """
    #Check to see is lamda is iterable. If lamda is a single value, bundle it into a single
    # value tuple so that we can treat all cases of lamda the same
    #If lamda is an iterable, coerce it into a tuple as well so we can bundle it with
    # the other arguments
    if isiterable(lamda):
        wlamda = tuple(lamda)
    else:
        wlamda = (lamda,)

    #Combine args into a single tuple so that we can check to see if all arguments are
    # numbers and greater than 0 once.
    #TODO: Can you explain why it is args = (mu, c) + wlamda and not args = (mu, c, wlamda)
    args = (mu, c) + wlamda

    if all([isinstance(a, Number) and a > 0 for a in args]):
        return True

    else:
        return False

def is_feasible(lamda, mu, c = 1):
    """
    Calculates rho (ρ) and checks to see if the value of rho is feasible.
    rho must be a value between 0 and 1.
    rho = lamda / mu * c

    Args:
        lamda: arrival rate of customers per time interval (scalar or multivalued)
        mu: service rate per time interval (scalar)
        c: number of servers in the system (scalar)

    Returns: True if rho is feasible False if rho is not feasible
    """
    #Check to see if all values are valid
    if not is_valid(lamda, mu, c):
        return False

    #Check to see if lamda is iterable and sum lamda up if it is
    if isiterable(lamda):
        lamda = sum(lamda)

    #Calculate rho using Little's Laws
    rho = lamda / (c * mu)

    #Check to see if 0 < rho < 1 because rho is a percentage of time a server is busy
    #Since is_valid() already ensures that lamda, mu, and c are non-negative values, we only need to check
    # to see if rho is less than 1.

    if rho >= 1:
        return False

    return True

def calc_p0(lamda, mu, c=1):
    """
    Calculates the probability that there is no one in the system (empty system).
    There are two different calculations depending on queue type.
    For single server queues, p0 = 1 - rho.
    For multi-server queues, p0 = ( ∑((r^n/n!)) + r^c/(c!*(1-rho)) ) ** -1

    Args:
        lamda: arrival rate of customers per time interval (scalar or multivalued)
        mu: service rate per time interval (scalar)
        c: number of servers in the system (scalar)

    Returns: Probability of an empty queue
    """
    #check to see if lamda, mu, and c are numerical scalars and within a valid range
    if not is_valid(lamda,mu,c):
        return math.nan

    #check to see if rho is within feasible range
    if not is_feasible(lamda, mu, c):
        return math.inf

    #check if lamda is iterable and sum it up if it is not
    if isiterable(lamda):
       lamda = sum(lamda)

    #calculate r using Little's Laws, the expected number of people in service
    r = lamda / mu

    #calculate rho using Little's Laws, the traffic intensity
    rho = lamda / (mu * c)

    #Single server queue calculation
    if c == 1:
        p0 = 1 - rho

    #Multi server queue calculation
    else:
        # Split the equation into different parts because one term is a summation
        # This also ensures that PEMDAS is honored.
        term_1 = 0
        for i in range(0, c):
            term_1 += (r ** i) / math.factorial(i)

        term_2 = (r ** c) / (math.factorial(c) * (1 - rho))

        p0 = 1.0 / (term_1 + term_2)

    return p0


def calc_lq_mmc(lamda, mu, c=1):
    """
    Calculates the Lq, or average number of people waiting in the queue, for an M/M/C type
    queue. There are two different calculations depending on queue type.
    For single server queues, Lq = lamda^2/(mu*(mu-lamda))
    For multi-server queues, Lq = r^c*rho/(c!*(1-rho)^2)*p0

    Args:
        lamda: arrival rate of customers per time interval (scalar or multivalued)
        mu: service rate per time interval (scalar)
        c: number of servers in the system (scalar)

    Returns: average number of people waiting in the queue
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
    r = lamda / mu
    rho = lamda / (mu * c)

    if c == 1:
        # Single server queue calculation
        lq = (lamda ** 2) / (mu * (mu - lamda))

    else:
        #Multi server queue calculation
        #Calculate numerator and denominator of the formula (listed in header) independently
        #This will help me debug if I were to have a typo; it also helps reduce the need for
        # parentheses within the denominator
        p0 = calc_p0(lamda, mu, c)
        lq_numerator = (r ** c) * rho
        lq_denominator = math.factorial(c) * ((1 - rho) ** 2)
        lq = (lq_numerator / lq_denominator) * p0

    return lq

