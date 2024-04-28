M = []
VALUE = []

def find_opt_schedule(j):
    # Define an array M where M[i] = optimal weight based on set {1,...,i}
    M = [None] * (len(j)+1)
    M[0] = 0

    optimal_weight = OPT(j)
    optimal_schedule = get_schedule(j)

def OPT(j):
    if j == 0:
        return 0
    else:
        if M[j]:
            return M[j]
        else:
            M[j] = max(VALUE[j] + OPT(p(j)), OPT(j-1))
            return M[j]


def get_schedule(j):
    if j == 0:
        return 0
    else:
        if VALUE[j] + M[p(j)] >= OPT(j-1):
            return [j] + get_schedule(p(j))
        else:
            return get_schedule(j-1)

# Returns the index of the request that is closest to j's starting time and disjoint from j
def p(j):
    return