import math
from math import isclose, isnan
import queues as q

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

    #Test for invalid cases
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

    # test lamda iterable
    expected = .8
    actual = q.calc_bk_mmc(1, (5, 10, 5), 25, 1)
    if isclose(expected, actual):
        print("Valid test for lamda iterable class 1: Passed")
    else:
        print("Invalid test for lamda iterable class 1: Failed")

    expected = .4
    actual = q.calc_bk_mmc(2, (5, 10, 5), 25, 1)
    if isclose(expected, actual):
        print("Valid test for lamda iterable class 2: Passed")
    else:
        print("Invalid test for lamda iterable class 2: Failed")

    expected = .2
    actual = q.calc_bk_mmc(3, (5, 10, 5), 25, 1)
    if isclose(expected, actual):
        print("Valid test for lamda iterable class 3: Passed")
    else:
        print("Invalid test for lamda iterable class 3: Failed")

    # test k == 0
    expected = 1
    actual = q.calc_bk_mmc(0, 2, 5, 1)
    if expected == actual:
        print("Valid test for k = 0: Passed")
    else:
        print("Invalid test for k = 0: Failed")

    #test for invalid cases
    #String inputs
    #test k not a number
    actual = q.calc_bk_mmc("hi", 12, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid k not a number: Passed")
    else:
        print("Invalid test for invalid k not a number: Failed")

    actual = q.calc_bk_mmc(1, "12", 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid lamda not a number: Passed")
    else:
        print("Invalid test for invalid lamda not a number: Failed")

    actual = q.calc_bk_mmc(1, (12,"1",2), 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid iterable lamda not a number: Passed")
    else:
        print("Invalid test for invalid iterable lamda not a number: Failed")

    actual = q.calc_bk_mmc(1, 12, "1", 1)
    if math.isnan(actual):
        print("Valid test for invalid mu not a number: Passed")
    else:
        print("Invalid test for invalid mu not a number: Failed")

    actual = q.calc_bk_mmc(1, 12, 1, "1")
    if math.isnan(actual):
        print("Valid test for invalid c not a number: Passed")
    else:
        print("Invalid test for invalid c not a number: Failed")

    #Negative inputs
    #test k = -1
    actual = q.calc_bk_mmc(-1, 12, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid k = -1: Passed")
    else:
        print("Invalid test for invalid k = -1: Failed")

    actual = q.calc_bk_mmc(2, -1, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid lamda = -1: Passed")
    else:
        print("Invalid test for invalid lamda = -1: Failed")

    actual = q.calc_bk_mmc(2, 1, -1, 1)
    if math.isnan(actual):
        print("Valid test for invalid mu = -1: Passed")
    else:
        print("Invalid test for invalid mu = -1: Failed")

    actual = q.calc_bk_mmc(2, 1, 1, -1)
    if math.isnan(actual):
        print("Valid test for invalid c = -1: Passed")
    else:
        print("Invalid test for invalid c = -1: Failed")

    #test k > len(lamda)
    expected = math.nan
    actual = q.calc_bk_mmc(5, 2,5,1)
    if math.isnan(actual):
        print("Valid test for k > len(lamda): Passed")
    else:
        print("Invalid test for k > len(lamda): Failed")

def tests_calc_wqk_mmc():
    """
    Tests calc_wqk_mmc(k, lamda, mu, c=1) function in queues.py
    Returns: None

    """
    #test for valid inputs
    expected = .16
    actual = q.calc_wqk_mmc(1, 20, 25, 1)
    if expected == actual:
        print("Valid test for valid inputs, scalar lamda: Passed")
    else:
        print("Invalid test for valid inputs, scalar lamda: Failed")

    expected = 0.04
    actual = q.calc_wqk_mmc(1, (5,10,5), 25, 1)
    if isclose(expected,actual):
        print("Valid test for valid inputs, priority class 1: Passed")
    else:
        print("Invalid test for valid inputs, priority class 1: Failed")

    expected = 0.1
    actual = q.calc_wqk_mmc(2, (5, 10, 5), 25, 1)
    if isclose(expected,actual):
        print("Valid test for valid inputs, priority class 1: Passed")
    else:
        print("Invalid test for valid inputs, priority class 1: Failed")

    expected = 0.4
    actual = q.calc_wqk_mmc(3, (5, 10, 5), 25, 1)
    if isclose(expected,actual):
        print("Valid test for valid inputs, priority class 1: Passed")
    else:
        print("Invalid test for valid inputs, priority class 1: Failed")

    # test for invalid cases
    # test k < 0
    actual = q.calc_wqk_mmc(-1, 2, 5, 1)
    if math.isnan(actual):
        print("Valid test for k < 0: Passed")
    else:
        print("Invalid test for k < 0: Failed")

    #Negative values
    actual = q.calc_wqk_mmc(2, -12, 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input, negative scalar lamda: Passed")
    else:
        print("Invalid test for invalid input, negative scalar lamda: Failed")

    actual = q.calc_wqk_mmc(2, (5,-10,5), 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input, negative iterable lamda: Passed")
    else:
        print("Invalid test for invalid input, negative iterable lamda: Failed")

    actual = q.calc_wqk_mmc(2, 12, -1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input, negative mu: Passed")
    else:
        print("Invalid test for invalid input, negative mu: Failed")

    actual = q.calc_wqk_mmc(2, 12, 1, -1)
    if math.isnan(actual):
        print("Valid test for invalid input, negative c: Passed")
    else:
        print("Invalid test for invalid input, negative c: Failed")

    #String inputs
    actual = q.calc_wqk_mmc("1", 2, 5, 1)
    if math.isnan(actual):
        print("Valid test for string k: Passed")
    else:
        print("Invalid test for string k: Failed")

    actual = q.calc_wqk_mmc(2, "12", 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input, string scalar lamda: Passed")
    else:
        print("Invalid test for invalid input, sting scalar lamda: Failed")

    actual = q.calc_wqk_mmc(2, (5, "10", 5), 1, 1)
    if math.isnan(actual):
        print("Valid test for invalid input, string iterable lamda: Passed")
    else:
        print("Invalid test for invalid input, string iterable lamda: Failed")

    actual = q.calc_wqk_mmc(2, 12, "1", 1)
    if math.isnan(actual):
        print("Valid test for invalid input, string mu: Passed")
    else:
        print("Invalid test for invalid input, string mu: Failed")

    actual = q.calc_wqk_mmc(2, 5, 1, "1")
    if math.isnan(actual):
        print("Valid test for invalid input, string c: Passed")
    else:
        print("Invalid test for invalid input, string c: Failed")

    #test k > len(lamda)
    actual = q.calc_wqk_mmc(5, (5,10,5), 25, 1)
    if math.isnan(actual):
        print("Valid test for k > len(lamda): Passed")
    else:
        print("Invalid test for k > len(lamda): Failed")

    #test k != 1
    actual = q.calc_wqk_mmc(5, 2 ,5,1)
    if math.isnan(actual):
        print("Valid test for k != 1 for scalar lamda: Passed")
    else:
        print("Invalid test for k != 1 for scalar lamda: Failed")

    #test for infeasible inputs
    actual = q.calc_wqk_mmc(100, 25, 1)
    if math.isinf(actual):
        print("Valid test for infeasible input, large scalar lamda: Passed")
    else:
        print("Invalid test for infeasible input, large scalar lamda: Failed")

    actual = q.calc_wqk_mmc(1,(25, 50, 75), 25, 1)
    if math.isinf(actual):
        print("Valid test for infeasible input, large iterable lamda: Passed")
    else:
        print("Invalid test for infeasible input, large iterable lamda: Failed")

    actual = q.calc_wqk_mmc(1,20, 25, 0.0000000000000001)
    if math.isinf(actual):
        print("Valid test for infeasible input, small c: Passed")
    else:
        print("Invalid test for infeasible input, small c: Failed")

    actual = q.calc_wqk_mmc(1,20, 0.000000000000000001, 1)
    if math.isinf(actual):
        print("Valid test for infeasible input, small mu: Passed")
    else:
        print("Invalid test for infeasible input, small mu: Failed")

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
    expected = {"r": 0.8,
              "ro": 0.8,
              "lq": 3.2,
              "wq": 0.16,
              "l": 4,
              "w": 0.2}
    actual = q.use_littles_law(20, 25, 1, lq=3.2)
    if actual == expected:
        #This also checks to see if "wqk" and "lqk" are NOT created, bc the == operator checks to see
        # if all keys and values are equal
        print("Valid test for valid input, lq kwarg: Passed")
    else:
        print("Invalid test for valid input, lq kwarg: Failed")

    actual = q.use_littles_law(20,25,1,wq=0.16)
    if actual == expected:
        print("Valid test for valid input, wq kwarg: Passed")
    else:
        print("Invalid test for valid input, wq kwarg: Failed")

    actual = q.use_littles_law(20, 25, 1, l=4)
    if actual == expected:
        print("Valid test for valid input, l kwarg: Passed")
    else:
        print("Invalid test for valid input, l kwarg: Failed")

    actual = q.use_littles_law(20, 25, 1, w=0.2)
    if actual == expected:
        print("Valid test for valid input, w kwarg: Passed")
    else:
        print("Invalid test for valid input, w kwarg: Failed")

    #Try every kwarg for priority queue
    expected = {"r": 0.8,
              "ro": 0.8,
              "lq": 3.2,
              "wq": 0.16,
              "l": 4,
              "w": 0.2}
    expected_qk = { "lqk":(0.2,1,2),
                  "wqk":(0.04,0.1,0.4)}
    actual = q.use_littles_law((5,10,5), 25, 1, lq=3.2)
    if ([isclose(actual[keys],expected[keys]) for keys in expected]
            and [isclose(expected_qk["lqk"][i],actual["lqk"][i]) for i in range(3)]
            and [isclose(expected_qk["wqk"][i],actual["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, lq kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, lq kwarg iterable lamda: Failed")

    actual = q.use_littles_law((5, 10, 5), 25, 1, wq=0.16)
    if ([isclose(actual[keys], expected[keys]) for keys in expected]
            and [isclose(expected_qk["lqk"][i], actual["lqk"][i]) for i in range(3)]
            and [isclose(expected_qk["wqk"][i], actual["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, wq kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, wq kwarg iterable lamda: Failed")

    actual = q.use_littles_law((5, 10, 5), 25, 1, l=4)
    if ([isclose(actual[keys], expected[keys]) for keys in expected]
            and [isclose(expected_qk["lqk"][i], actual["lqk"][i]) for i in range(3)]
            and [isclose(expected_qk["wqk"][i], actual["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, l kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, l kwarg iterable lamda: Failed")

    actual = q.use_littles_law((5, 10, 5), 25, 1, w=0.2)
    if ([isclose(actual[keys], expected[keys]) for keys in expected]
            and [isclose(expected_qk["lqk"][i], actual["lqk"][i]) for i in range(3)]
            and [isclose(expected_qk["wqk"][i], actual["wqk"][i]) for i in range(3)]):
        print("Valid test for valid input, w kwarg iterable lamda: Passed")
    else:
        print("Invalid test for valid input, w kwarg iterable lamda: Failed")

    #Test invalid inputs
    #No kwargs passed
    expected = None
    actual =q.use_littles_law(20, 25, 1)
    if actual == expected:
        print("Valid test for invalid input, no kwargs: Passed")
    else:
        print("Invalid test for invalid input, no kwargs: Failed")

    #Invalid lamda, mu, c
    #String values
    actual =q.use_littles_law("20", 25, 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, string scalar lamda: Passed")
    else:
        print("Invalid test for invalid input, string scalar lamda: Failed")

    actual = q.use_littles_law((5,"10",5), 25, 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, string iterable lamda: Passed")
    else:
        print("Invalid test for invalid input, string iterable lamda: Failed")

    actual = q.use_littles_law(20, "25", 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, string mu: Passed")
    else:
        print("Invalid test for invalid input, string mu: Failed")

    actual = q.use_littles_law(20, 25, "1", lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, string c: Passed")
    else:
        print("Invalid test for invalid input, string c: Failed")

    actual = q.use_littles_law(-20, 25, 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, negative scalar lamda: Passed")
    else:
        print("Invalid test for invalid input, negative scalar lamda: Failed")

    actual = q.use_littles_law((5,-10,5), 25, 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, negative iterable lamda: Passed")
    else:
        print("Invalid test for invalid input, negative iterable lamda: Failed")

    actual = q.use_littles_law(20, -25, 1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, negative mu: Passed")
    else:
        print("Invalid test for invalid input, negative mu: Failed")

    actual = q.use_littles_law(20, 25, -1, lq=3.2)
    if isnan(actual):
        print("Valid test for invalid input, negative c: Passed")
    else:
        print("Invalid test for invalid input, negative c: Failed")

    #Invalid kwarg
    actual = q.use_littles_law(20, 25, 1, rho=0.8)
    if isnan(actual):
        print("Valid test for invalid input, invalid kwarg key: Passed")
    else:
        print("Invalid test for invalid input, invalid kwarg key: Failed")

    actual = q.use_littles_law(20, 25, 1, lq=-3.2)
    if isnan(actual):
        print("Valid test for invalid input, out of range kwarg value: Passed")
    else:
        print("Invalid test for invalid input, out of range kwarg value: Failed")

    #Test infeasible values
    actual = q.use_littles_law(100, 25, 1, lq=3.2)
    if math.isinf(actual):
        print("Valid test for infeasible input, large scalar lamda: Passed")
    else:
        print("Invalid test for infeasible input, large scalar lamda: Failed")

    actual = q.use_littles_law((25,50,75), 25, 1, lq=3.2)
    if math.isinf(actual):
        print("Valid test for infeasible input, large iterable lamda: Passed")
    else:
        print("Invalid test for infeasible input, large iterable lamda: Failed")

    actual = q.use_littles_law(20, 25, 0.0000000000000001, lq=3.2)
    if math.isinf(actual):
        print("Valid test for infeasible input, small c: Passed")
    else:
        print("Invalid test for infeasible input, small c: Failed")

    actual = q.use_littles_law(20, 0.000000000000000001, 1, lq=3.2)
    if math.isinf(actual):
        print("Valid test for infeasible input, small mu: Passed")
    else:
        print("Invalid test for infeasible input, small mu: Failed")


tests_is_valid()
tests_is_feasible()
tests_calc_p0()
tests_calc_lq_mmc()
tests_calc_bk_mmc()
tests_calc_wqk_mmc()
tests_calc_lqk_mmc()
tests_use_littles_law()