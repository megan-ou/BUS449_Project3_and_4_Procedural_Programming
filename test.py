print("helo")

#Please please please add comments and headers to your code

def calc_bk_mmc(k, lamda, mu, c=1):
    #TODO: is_valid() arguments are lamda, mu, and c. They have to be passed in that order or else the program will
    # think k is lamda, lamda is mu, and mu is c. is_valid is not equipped to handle the 'k' argument.
    if not is_valid(k, lamda, mu):
        return math.nan
    # See above note
    if not is_feasible(k, lamda, mu):
        return math.inf

    rho_agg = 0
    #TODO: this was meant to be a list comprehension as specified by the instructions
    for j in range(k):
        rho_agg += lamda[j]/(c*mu)

    #TODO: mini note, but variable names are typically lowercase
    Bk = 1 - rho_agg

    return Bk

def calc_wqk_mmc(k, lamda, mu, c=1):
    #See above note about arguments
    if not is_valid(lamda, mu, k):
        return math.nan
    #TODO: c=1 is not an argument you want to pass because this implies that this is a keyword argument and the
    # function does not ask for one. In addition by putting in c = 1, you are reassigning the value of c when it could
    # be 2 or 3. c itself has a value and should just be passed in as c.
    if not is_feasible(lamda, mu, c=1):
        return math.inf

    #TODO: Because we are working with wqk; wq for one class group, then aggregating lamda would not make sense at all
    # since it would apply to all classes. Instead, if lamda is iterable, we need to access lamda_k by taking lamda[k]
    # Also, if lamda is not iterable, assign the value of lamda to lamda_k
    if isiterable(lamda):
        lamda_agg = sum(lamda)

    #TODO: rho is a variable that has not been defined anywhere
    #TODO pt 2: It looks look you misread the formula and read Lq as lamda,,, which means you need 2 lamdas
    # a lamda aggregate and a lamda k; good news: calc_lq_mmc aggregates lamda for you so you can just pass lamda in
    # as an argument
    Numerator = (1 - rho) * lamda

    #TODO: bk should be lowercased. It is also an undefined variable. You need to call the function that you wrote
    # previously, calc_bk_mmc() and pass in the correct arguments to calculate Bk AND B_k-1
    # (it is b sub k-1, not bk - 1; those are two very different things)
    Denominator = lamda * (Bk - 1) * Bk

    Wqk = Numerator / Denominator

    return Wqk
