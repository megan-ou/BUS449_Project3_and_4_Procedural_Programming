import math
from math import isclose
import queues as q
from queues import use_littles_law


#queues_tests.py
#Test valid and invalid cases for queues.py
#@Author Toby Okoji, Megan Ou
#@Version September 2025

def tests_is_valid():
    """
    Tests is_valid(lamda, mu, c) function in queues.py
    Returns: None

    """
    #Check for valid inputs
    #Single lamda value
    expected = True
    actual = q.is_valid(37, 35, 1)
    if expected == actual:
        print("Valid test for valid input, single lamda: Passed")
    else:
        print("Invalid test for valid input, single lamda: Failed")

    #Multiple values for lamda
    actual == q.is_valid((9.2,18.1,11.6), 35.66, 1)
    if expected == actual:
        print("Valid test for valid input, multiple lamda: Passed")
    else:
        print("Invalid test for valid input, multiple lamda: Failed")

    #Check from invalid inputs
    #Check for non-numerical inputs for lamda, m, and c
    expected = False
    actual = q.is_valid("45", 30, 1)
    if expected == actual:
        print("Valid test for non numerical lamda: Passed")
    else:
        print("Invalid test for non numerical lamda: Failed")

    actual = q.is_valid(45, "30", 1)
    if expected == actual:
        print("Valid test for non numerical mu: Passed")
    else:
        print("Invalid test for non numerical mu: Failed")

    actual = q.is_valid(45, 30, "1")
    if expected == actual:
        print("Valid test for non numerical c: Passed")
    else:
        print("Invalid test for non numerical c: Failed")

    #Test for negative and out of range values
    actual = q.is_valid((3,2,-10), 7, 1)
    if expected == actual:
        print("Valid test for negative multi-value lamda: Passed")
    else:
        print("Invalid test for negative multi-value lamda: Failed")

    actual = q.is_valid(-10, 7, 1)
    if expected == actual:
        print("Valid test for negative scalar lamda: Passed")
    else:
        print("Invalid test for negative scalar lamda: Failed")

    actual = q.is_valid(10, 0, 1)
    if expected == actual:
        print("Valid test for out of range mu: Passed")
    else:
        print("Invalid test for out of range mu: Failed")

    actual = q.is_valid(10, -1, 1)
    if expected == actual:
        print("Valid test for negative mu: Passed")
    else:
        print("Invalid test for negative mu: Failed")

    actual = q.is_valid(10, 12, -1)
    if expected == actual:
        print("Valid test for negative c: Passed")
    else:
        print("Invalid test for negative c: Failed")

def tests_is_feasible():
    """
    Tests is_feasible(lamda, mu, c) function in queues.py
    Returns: None
    """
    # All values are valid
    expected = True
    actual = q.is_feasible(10, 12, 1)
    if actual == expected:
        print("Valid test for lamda, mu, c: Passed")
    else:
        print("Invalid test for lamda, mu, c: Failed")

    #Double value for lamda
    actual = q.is_feasible(10.3, 12, 1)
    if actual == expected:
        print("Valid test for int lamda, mu, c: Passed")
    else:
        print("Invalid test for int lamda, mu, c: Failed")

    # Lamda is iterable
    actual = q.is_feasible((10, 5), 20, 1)
    if expected == actual:
        print("Valid test for sum lamda: Passed")
    else:
        print("Invalid test for sum lamda: Failed")

    # int in lamda
    actual = q.is_feasible((10.3, 5), 20, 1)
    if expected == actual:
        print("Valid test for int sum lamda: Passed")
    else:
        print("Invalid test for int sum lamda: Failed")

    # rho calculation
    expected = True
    actual = q.is_feasible(10, 11, 1)
    if expected == actual:
        print("Valid test for valid rho calculation: Passed")
    else:
        print("Invalid test for valid rho calculation: Failed")

    #Test for invlaid cases
    # String in lamda
    expected = False
    actual = q.is_feasible(("hi", 5), 20, 1)
    if expected == actual:
        print("Valid test for sum string: Passed")
    else:
        print("Invalid test for sum string: Failed")

    # rho = 0
    expected = False
    actual = q.is_feasible(0, 2, 1)
    if expected == actual:
        print("Valid test for rho <=0: Passed")
    else:
        print("Invalid test for rho <=0: Failed")

    # rho < 0
    expected = False
    actual = q.is_feasible(-2, 2, 1)
    if expected == actual:
        print("Valid test for negative rho: Passed")
    else:
        print("Invalid test for negative rho: Failed")

    # rho > 1
    expected = False
    actual = q.is_feasible(10, 2, 1)
    if expected == actual:
        print("Valid test for rho >1: Passed")
    else:
        print("Invalid test for rho >1: Failed")


def tests_calc_p0():
    """
    Tests calc_p0(lamda, mu, c = 1) function in queues.py
    Returns: None
    """
    #Test for valid inputs
    #Single server tests
    # Single lamda
    expected = 0.16666666666666663
    actual = q.calc_p0(10, 12, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & single lamda: Passed")
    else:
        print("Invalid test for valid input, single server & single lamda: Failed")

    # Multiple lamda
    actual = q.calc_p0((3, 2, 5), 12, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & multiple lamda: Passed")
    else:
        print("Invalid test for valid input, single server & multiple lamda: Failed")
    #Multi server tests
    #Single lamda
    expected = 0.17647058823529413
    actual = q.calc_p0(35,25,2)
    if isclose(expected,actual):
        print("Valid test for valid input, multi server & single lamda: Passed")
    else:
        print("Invalid test for valid input, multi server & single lamda: Failed")

    #Multiple lamda
    actual = q.calc_p0((10,11,14),25,2)
    if isclose(expected,actual):
        print("Valid test for valid input, multi server & multiple lamda: Passed")
    else:
        print("Invalid test for valid input, multi server & multiple lamda: Failed")

    #Test for invalid cases
    #Invalid values, just to ensure that is_valid is called in is_feasible
    actual = q.calc_p0(-10,-12,1)
    if math.isnan(actual):
        print("Valid test for invalid input: Passed")
    else:
        print("Invalid test for invalid input: Failed")

    #Valid values but infeasible rho
    expected = math.inf
    actual = q.calc_p0(10,2,1)
    if isclose(expected,actual):
        print("Valid test for infeasible input: Passed")
    else:
        print("Invalid test for infeasible input: Failed")

def tests_calc_lq_mmc():
    """
    Tests calc_lq_mmc(lamda, mu, c = 1) function in queues.py
    Returns: None
    """
    #Test for valid inputs
    #Single server
    #Single lamda
    expected = 4.166666666666668
    actual = q.calc_lq_mmc(10, 12, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & single lamda: Passed")
    else:
        print("Invalid test for valid input, single server & single lamda: Failed")

    # Multiple lamda
    actual = q.calc_lq_mmc((2, 3, 5), 12, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & multiple lamda: Passed")
    else:
        print("Invalid test for valid input, single server & multiple lamda: Failed")

    # Multi server tests
    # Single lamda
    expected = 1.3450980392156857
    actual = q.calc_lq_mmc(35, 25, 2)
    if isclose(expected, actual):
        print("Valid test for valid input, multi server & single lamda: Passed")
    else:
        print("Invalid test for valid input, multi server & single lamda: Failed")

    # Multiple lamda
    actual = q.calc_lq_mmc((10, 11, 14), 25, 2)
    if isclose(expected, actual):
        print("Valid test for valid input, multi server & multiple lamda: Passed")
    else:
        print("Invalid test for valid input, multi server & multiple lamda: Failed")

    #Test for invalid cases
    # Invalid values, just to ensure that is_valid is called in is_feasible
    actual = q.calc_p0(-10, -12, 1)
    if math.isnan(actual):
        print("Valid test for invalid input: Passed")
    else:
        print("Invalid test for invalid input: Failed")

    # Valid values but infeasible rho
    expected = math.inf
    actual = q.calc_p0(10, 2, 1)
    if isclose(expected, actual):
        print("Valid test for infeasible input: Passed")
    else:
        print("Invalid test for infeasible input: Failed")

def tests_calc_bk_mmc():
    """
    Tests calc_bk_mmc(k, lamda, mu, c=1) function in queues.py
    Returns: None

    """
    #test for valid inputs
    #single lamda
    expected = .6
    actual = q.calc_bk_mmc(1, 2, 5, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & single lamda: Passed")
    else:
        print("Invalid test for valid input, single server & single lamda: Failed")

    #tests multiple lamda
    expected = .8
    actual = q.calc_bk_mmc(1,(1,1), 5, 1)
    if isclose(expected, actual):
        print("Valid test for valid input, single server & multiple lamda: Passed")
    else:
        print("Invalid test for valid input, single server & multiple lamda: Failed")

    #test k not a number
    expected = math.nan
    actual = q.calc_bk_mmc("hi", 12, 1, 1)
    if math.isnan(actual):
        print("Valid test for valid k not a number: Passed")
    else:
        print("Invalid test for valid k not a number: Failed")

    #test k = -1
    expected = math.nan
    actual = q.calc_bk_mmc(-1, 12, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid k = -1: Passed")
    else:
        print("Invalid test for invalid k = -1: Failed")

    #test for invalid cases
    #check to see if is_valid is passed to is_feasible
    actual = q.calc_bk_mmc(2, -12, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input: Passed")
    else:
        print("Invalid test for invalid input: Failed")

    #test lamda iterable
    expected = .6
    actual = q.calc_bk_mmc(1, (2,3), 5, 1)
    if isclose(expected, actual):
        print("Valid test for lamda iterable: Passed")
    else:
        print("Invalid test for lamda iterable: Failed")

    #test k < len(lamda)
    expected = math.nan
    actual = q.calc_bk_mmc(5, 2,5,1)
    if math.isnan(actual):
        print("Valid test for k > len(lamda): Passed")
    else:
        print("Invalid test for k > len(lamda): Failed")

    #test k == 0
    expected = 1
    actual = q.calc_bk_mmc(0, 2,5,1)
    if expected ==actual:
        print("Valid test for k = 0: Passed")
    else:
        print("Invalid test for k = 0: Failed")

def tests_calc_wqk_mmc():
    """
    Tests calc_wqk_mmc(k, lamda, mu, c=1) function in queues.py
    Returns: None

    """

def tests_calc_lqk_mmc():
    """
    Tests calc_lqk_mmc(k, lamda, mu, c=1) function in queues.py
    Returns: None

    """
    #Test for valid cases for each priority class
    #Tuple lamda
    expected = 0.2
    actual = q.calc_lqk_mmc(1, (5,10,5), 0.04)
    if isclose(expected, actual):
        print("Valid test for valid input, tuple lamda class 1: Passed")
    else:
        print("Invalid test for valid input, tuple lamda class 1: Failed")

    expected = 1
    actual = q.calc_lqk_mmc(2, (5,10,5), 0.1)
    if isclose(expected, actual):
        print("Valid test for valid input, tuple lamda class 2: Passed")
    else:
        print("Invalid test for valid input, tuple lamda class 2: Failed")

    expected = 2
    actual = q.calc_lqk_mmc(3, (5,10,5), 0.4)
    if isclose(expected, actual):
        print("Valid test for valid input, tuple lamda class 3: Passed")
    else:
        print("Invalid test for valid input, tuple lamda class 3: Failed")

    #Single tuple lamda
    actual = q.calc_lqk_mmc(1, (20,), 0.1)
    if isclose(expected, actual):
        print("Valid test for valid input, single tuple lamda: Passed")
    else:
        print("Invalid test for valid input, single tuple lamda: Failed")

    #Scalar lamda
    actual = q.calc_lqk_mmc(1, 20, 0.1)
    if isclose(expected, actual):
        print("Valid test for valid input, scalar lamda: Passed")
    else:
        print("Invalid test for valid input, scalar lamda: Failed")

    #Test for invalid cases
    #String inputs for all arguments
    actual = q.calc_lqk_mmc("1", (5,10,5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, string input for k: Passed")
    else:
        print("Invalid test for invalid input, string input for k: Failed")

    actual = q.calc_lqk_mmc(1, ("5", 10, 5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, string input for lamda class 1: Passed")
    else:
        print("Invalid test for invalid input, string input for lamda class 1: Failed")

    actual = q.calc_lqk_mmc(2, (5,"10",5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, string input for lamda class 2: Passed")
    else:
        print("Invalid test for invalid input, string input for lamda class 2: Failed")

    actual = q.calc_lqk_mmc(3, (5, 10, "5"), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, string input for lamda class 3: Passed")
    else:
        print("Invalid test for invalid input, string input for lamda class 3: Failed")

    actual = q.calc_lqk_mmc(1, (5,10,5), "0.4")
    if math.isnan(actual):
        print("Valid test for invalid input, string input for wqk: Passed")
    else:
        print("Invalid test for invalid input, string input for wqk: Failed")

    #Args out of range
    actual = q.calc_lqk_mmc(4, (5,10,5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, k too large iterable lamda: Passed")
    else:
        print("Invalid test for invalid input, k too large iterable lamda: Failed")

    actual = q.calc_lqk_mmc(2, 20, 0.1)
    if math.isnan(actual):
        print("Valid test for invalid input, k too large scalar lamda: Passed")
    else:
        print("Invalid test for invalid input, k too large scalar lamda: Failed")

    actual = q.calc_lqk_mmc(-1, (5,10,5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, negative k: Passed")
    else:
        print("Invalid test for invalid input, negative k: Failed")

    actual = q.calc_lqk_mmc(0, (5,10,5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, k = 0: Passed")
    else:
        print("Invalid test for invalid input, k = 0: Failed")

    actual = q.calc_lqk_mmc(1, (-5, 10, 5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, negative lamda class 1: Passed")
    else:
        print("Invalid test for invalid input, negative lamda class 1: Failed")

    actual = q.calc_lqk_mmc(2, (5, -10, 5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, negative lamda class 2: Passed")
    else:
        print("Invalid test for invalid input, negative lamda class 2: Failed")

    actual = q.calc_lqk_mmc(3, (5, 10, -5), 0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, negative lamda class 3: Passed")
    else:
        print("Invalid test for invalid input, negative lamda class 3: Failed")

    actual = q.calc_lqk_mmc(1, (5, 10, 5), -0.4)
    if math.isnan(actual):
        print("Valid test for invalid input, negative wqk: Passed")
    else:
        print("Invalid test for invalid input, negative wqk: Failed")

def tests_use_littles_law():
    """
    Tests use_littles_law(lamda, mu, c=1, **kwargs) in queues.py
    Returns: None

    """
    # Test valid cases
    # Try every kwarg for non-priority queue (scalar lamda)
    actual = {"r": 0.8,
              "ro": 0.8,
              "lq": 3.2,
              "wq": 0.16,
              "l": 4,
              "w": 0.2}
    expected = q.use_littles_law(20, 25, 1, lq=3.2)
    if actual == expected:
        #This also checks to see if "wqk" and "lqk" are NOT created, bc the == operator checks to see
        # if all keys and values are equal
        print("Valid test for valid input, lq kwarg: Passed")
    else:
        print("Invalid test for valid input, lq kwarg: Failed")

    expected = q.use_littles_law(20,25,1,wq=0.16)
    if actual == expected:
        print("Valid test for valid input, wq kwarg: Passed")
    else:
        print("Invalid test for valid input, wq kwarg: Failed")

    expected = q.use_littles_law(20, 25, 1, l=4)
    if actual == expected:
        print("Valid test for valid input, l kwarg: Passed")
    else:
        print("Invalid test for valid input, l kwarg: Failed")

    expected = q.use_littles_law(20, 25, 1, w=0.2)
    if actual == expected:
        print("Valid test for valid input, w kwarg: Passed")
    else:
        print("Invalid test for valid input, w kwarg: Failed")

    #Try every kwarg for priority queue
    actual = {"r": 0.8,
              "ro": 0.8,
              "lq": 3.2,
              "wq": 0.16,
              "l": 4,
              "w": 0.2}
    actual_qk = { "lqk":(0.2,1,2),
                  "wqk":(0.04,0.1,0.4)}
    expected = q.use_littles_law((5,10,5), 25, 1, lq=3.2)
    if ([isclose(actual[keys],expected[keys]) for keys in actual]
            and [isclose(actual_qk["lqk"][i],expected["lqk"][i]) for i in range(3)]
            and [isclose(actual_qk["wqk"][i],expected["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, lq kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, lq kwarg iterable lamda: Failed")

    expected = q.use_littles_law((5, 10, 5), 25, 1, wq=0.16)
    if ([isclose(actual[keys], expected[keys]) for keys in actual]
            and [isclose(actual_qk["lqk"][i], expected["lqk"][i]) for i in range(3)]
            and [isclose(actual_qk["wqk"][i], expected["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, wq kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, wq kwarg iterable lamda: Failed")

    expected = q.use_littles_law((5, 10, 5), 25, 1, l=4)
    if ([isclose(actual[keys], expected[keys]) for keys in actual]
            and [isclose(actual_qk["lqk"][i], expected["lqk"][i]) for i in range(3)]
            and [isclose(actual_qk["wqk"][i], expected["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, l kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, l kwarg iterable lamda: Failed")

    expected = q.use_littles_law((5, 10, 5), 25, 1, w=0.2)
    if ([isclose(actual[keys], expected[keys]) for keys in actual]
            and [isclose(actual_qk["lqk"][i], expected["lqk"][i]) for i in range(3)]
            and [isclose(actual_qk["wqk"][i], expected["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, w kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, w kwarg iterable lamda: Failed")



#tests_is_valid()
#tests_is_feasible()
#tests_calc_p0()
#tests_calc_lq_mmc()
#tests_calc_bk_mmc()
#tests_calc_wqk_mmc()
#tests_calc_lqk_mmc()
tests_use_littles_law()