import math
from unittest.util import sorted_list_difference

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
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        mu (number): service rate per time interval (scalar)
        c (number): number of servers in the system (scalar)

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
    args = (mu, c, *wlamda)

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
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        mu (number): service rate per time interval (scalar)
        c (number): number of servers in the system (scalar)

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
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        mu (number): service rate per time interval (scalar)
        c (number): number of servers in the system (scalar)

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
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        mu (number): service rate per time interval (scalar)
        c (number): number of servers in the system (scalar)

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

def calc_lqk_mmc(k, lamda, wqk):
    """
    Calculates the Lqk of specific priority group k in a priority queue.
    Uses the formula L_q,k = W_q,k * lamda_k

    Args:
        k (number): priority class number
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        wqk (number): average waiting time for priority class k

    Returns: Lqk; average number of people waiting in queue for class k

    """
    #Check to see if all arguments are numerical and larger than 0. Was initially going to call is_valid() but we
    # do not have the right types of arguments. (Missing mu).
    if not isinstance(k, Number) or k <= 0:
        return math.nan
    if isiterable(lamda):
        #Check if lamda is iterable and then take the (k-1) index of lamda.
        #Take k-1 since indexing starts at 0 and k classes start at 1.
        lamda = lamda[k-1]
    if not(isinstance(lamda, Number) or isinstance(wqk, Number)) or lamda <= 0 or wqk <= 0:
        return math.nan

    #if all arguments, calculate lqk based on little's laws
    return lamda * wqk

def use_littles_law(lamda, mu, c=1, **kwargs):
    """
    Takes a keyword argument and uses Little's Laws to calculate r, rho, L, Lq, W, Wq, Wqk, and Lqk based off the
    passed in arguments. If multiple keyword arguments are passed in, only the first one will be used.

    Args:
        lamda (number): arrival rate of customers per time interval (scalar or multivalued)
        mu (number): service rate per time interval (scalar)
        c (number): number of servers in the system (scalar)
        **kwargs:
            l (number): average number of people in the system
            lq (number): average number of people waiting the queue
            w (number): time spent in the system
            wq (number): time spent waiting in the queue

    Returns: a dictionary with r, ro, l, lq, w, wq, and if the queue is a priority queue,
        returns wqk and lqk as a tuple in addition
    """
    # Extract the first kwarg, since it is the only one used. We do not need to delete the other kwargs.
    # By extracting it, we ensure that we won't accidentally reference a different kwarg.
    first_kwarg = next(iter(kwargs))

    #Check for errors in case arguments are passed in weird
    if not is_valid(lamda, mu, c):
        return math.nan
    if not is_feasible(lamda, mu, c):
        return math.inf

    if not (first_kwarg == "l" or first_kwarg == "lq" or first_kwarg == "w" or first_kwarg == "wq"):
        # kwarg is either l, lq, w, wq. Function is not written to handle any other type of kwarg. I was considering
        # writing code to check to see if there are other valid kwargs if the first kwarg is an invalid value, but I
        # think that I might leave that task for if I have more time at the end.
        return math.nan
    if not (isinstance(kwargs[first_kwarg], Number) and kwargs[first_kwarg] > 0):
        return -math.inf

    #Initialize dictionary with empty values. Initialize the dictionary so it is easier to assign values
    # (and that is okay because dictionaries are mutable).

    solution = dict.fromkeys(["r", "ro", "l", "lq", "w", "wq"])

    if isiterable(lamda):
        # Check to see if lamda is iterable because if so, then we know that the queue is a priority queue. That way we can
        # have an aggregate lamda value and have dictionary keys for wqk and lqk. I don't want to create those keys in the
        # dictionary if it is not necessary.
        solution.update({"wqk":None, "lqk":None})

        #To prevent the use of another conditional, also calculate the values of wqk and lqk. I am going to iterate
        # through all lamdas and bundle them into a tuple. First, initialize empty tuples that I will add to with
        # each call to wqk and lqk.
        wqk_tup = ()
        lqk_tup = ()

        #TODO: write code after we write the methods needed
        for i in range(1, len(lamda)+1):
            #Start iterating at 1 instead of 0 because k starts at 1
            #Calculate wqk and save into its own variable so it can be used in the
            # function call for calc_lqk_mmc().
            #TODO: function call for wqk "wqk = wqk + (call,)"
            wqk = 0 #temp value
            wqk_tup = wqk_tup + (wqk,)
            lqk_tup = lqk_tup + (calc_lqk_mmc(i, lamda[i-1], wqk),)

        solution["wqk"] = wqk_tup
        solution["lqk"] = lqk_tup

        #Aggregate lamda after individual lamda calculations are done so queue level calculations can
        # use the sum of lamda.
        lamda = sum(lamda)

    #Start to fill out the dictionary. We can calculate r and ro immediately because the kwargs are not needed for
    # the calculation; we only need the regular args

    solution[first_kwarg] = kwargs.get(first_kwarg)
    solution["r"] = lamda / mu
    solution["ro"] = lamda / (mu * c)

    #Now, do calculations for the values based on kwargs. Go through each "None" value key and calculate if we have the
    # correct variables. Set these calculations within a while loop so that if it is skipped the first time around
    # because the necessary variable was not available, we can come back to it since it might be calculated later on.
    # The idea is that this way, each version/variation of a Little's Law equation is only run once.

    while any([solution[keys] is None for keys in solution]):
        #Arbitrarily chose to check "l" first
        if solution["l"] is None and not (solution["w"] is None):
            solution["l"] = solution["w"] * lamda
        if solution["l"] is None and not (solution["lq"] is None):
            solution["l"] = solution["lq"] + solution["r"]

        #Check for "w" next
        if solution["w"] is None and not (solution["wq"] is None):
            solution["w"] = solution["wq"] + (1 / mu)
        if solution["w"] is None and not (solution["l"] is None):
            solution["w"] = solution["l"] / lamda

        #Check for "wq" next
        if solution["wq"] is None and not (solution["w"] is None):
            solution["wq"] = solution["w"] - (1 / mu)
        if solution["wq"] is None and not (solution["lq"] is None):
            solution["wq"] = solution["lq"] / lamda

        #Finally, check for "lq"
        if solution["lq"] is None and not (solution["wq"] is None):
            solution["lq"] = solution["wq"] * lamda
        if solution["lq"] is None and not (solution["l"] is None):
            solution["lq"] = solution["l"] - solution["r"]

    return solution

#TODO: Old code that didn't seem the most efficient because it calculates the same metric in more than one place.
# Leaving this here while I play around with a possibly more efficient version. Is the new version truly more efficient?
"""
    #Now, do calculations based on the first kwarg. The order of calculations will depend on which kwarg is given first.
    # I was originally to go through each key and check if value was None and then calculate the value using
    # Little's Laws, but then I realized that the order of calculations depends on what kwarg is given.
    # If I were to use that idea, I would have to use a lot of nested if/else statements that I do not like
    # (it feels messy). I think I might have to scrap that idea and do a bunch of if/else statements based on
    # what the kwarg is.
    if first_kwarg == "l":
        solution["lq"] = solution["l"] - solution["r"]
        solution["wq"] = solution["lq"] / lamda
        solution["w"] = solution["wq"] + (1 / mu)
    elif first_kwarg == "lq":
        solution["wq"] = solution["lq"] / lamda
        solution["w"] = solution["wq"] + (1 / mu)
        solution["l"] = solution["w"] * lamda
    elif first_kwarg == "w":
        solution["l"] = solution["w"] * lamda
        solution["lq"] = solution["l"] - solution["r"]
        solution["wq"] = solution["lq"] / lamda
    else:
        solution["lq"] = solution["wq"] * lamda
        solution["w"] = solution["wq"] + (1 / mu)
        solution["l"] = solution["w"] * lamda
"""
