from time import process_time_ns

import queues
print(queues.calc_p0((5, 10, 5), 25, 1))

def tests_is_valid():
    """
    Test to see if function is_valid is working properly
    """

    #checks lamda is iterable
    lamda_expected = "hi"
    lamda_actual = type(lamda)
    if lamda_expected == lamda_actual:
        print("tuple is valid")
    else:
        print("tuple is not valid")

    lamda_expected = type(str)
    lamda_actual = type(lamda)
    if lamda_expected == lamda_actual:
        print("number is valid")
    else:
        print("number is not valid")



def tests_is_feasible():



tests_is_valid()