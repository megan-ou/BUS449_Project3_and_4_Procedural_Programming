print("helo")

def calc_bk_mmc(k, lamda, mu, c=1):
    if not is_valid(k, lamda, mu):
        return math.nan

    if not is_feasible(k, lamda, mu):
        return math.inf

    rho_agg = 0
    for j in range(k):
        rho_agg += lamda[j]/(c*mu)

    Bk = 1 - rho_agg

    return Bk

def calc_wqk_mmc(k, lamda, mu, c=1):
    if not is_valid(lamda, mu, k):
        return math.nan

    if not is_feasible(lamda, mu, c=1):
        return math.inf

    if isiterable(lamda):
        lamda_agg = sum(lamda)

    Numerator = (1 - rho) * lamda

    Denominator = lamda * (Bk - 1) * Bk

    Wqk = Numerator / Denominator

    return Wqk
