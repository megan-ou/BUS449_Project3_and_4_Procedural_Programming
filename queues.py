import math
#queues.py
#Calculates the average number of people in queue (L_q) for an M/M/C queue
#@Author Megan Ou, Toby Okoji
#@Version September 2025

def factorial(x):
    """
    Helper method for calculating a factorial. Taken from code we wrote
    in Project 1. Takes an integer and recursively calculates the factorial.
    Factorial is defined as x! = x(x-1)(x-2)⋯1
    :param x: integer where factorial starts
    :return: integer solution
    """
    # Error Checking: x is a positive integer less than 1000
    if not isinstance(x, int):
        return -math.inf
    if x < 0:
        return math.nan

    if x > 1000:
        return math.inf

    # Recursive base case, factorial of 0 will always be 1
    # This is how we check to see if we are at the end of our factorial
    if x == 0:
        return 1;
    # Recursively call factorial function on (x-1)
    else:
        return x * factorial(x - 1)

def is_valid(lamda, mu, c = 1):
    """
    Checks to see if all arguments are numerical scalars.
    Checks to see if value of arguments are within the valid range.
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: True if all arguments are valid, False if any argument is invalid
    """

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

def calc_p0(lamda, mu, c=1):
    """
    Calculates the probability that there is no one in the system (empty system).
    There are two different calculations depending on queue type.
    For single server queues, p0 = 1 - rho.
    For multi-server queues, p0 = ∑((r^n/n!) + (r^c/(c!*(1-rho))))
    :param lamda: arrival rate of customers (per time interval)
    :param mu: service rate (per time interval)
    :param c: number of servers in the system
    :return: Probability of an empty queue
    """

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