import queues as q

#queues_tests.py
#Test valid and invalid cases for queues.py
#@Author Toby Okoji, Megan Ou
#@Version September 2025

def tests_is_valid():
    """
    Test to see if function is_valid is working properly
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

    actual = q.is_valid((3,2,-10), 7, 1)
    if expected == actual:
        print("Valid test for negative lamda: Passed")
    else:
        print("Invalid test for negative lamda: Failed")

    actual = q.is_valid(10, 0, 1)
    if expected == actual:
        print("Valid test for out of range mu: Passed")
    else:
        print("Invalid test for out of range mu: Failed")

    actual = q.is_valid(10, 12, -1)
    if expected == actual:
        print("Valid test for negative c: Passed")
    else:
        print("Invalid test for negative c: Failed")

def tests_is_feasible():
    """
    Test to see if is_feasible() is working correctly
    :return:
    """

tests_is_valid()