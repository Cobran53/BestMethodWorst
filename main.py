import numpy as np
from scipy.optimize import linprog
import importlib

data = importlib.import_module("data")

def bwm(criteria, best_criterion, worst_criterion, best_to_others, others_to_worst):

    n = len(criteria)
    
    # minmum ξ
    c = np.zeros(n + 1)
    c[-1] = 1  

    A = []
    b = []

    # Best-to-Others limit
    best_index = criteria.index(best_criterion)
    for j in range(n):
        if j != best_index:
            row = np.zeros(n + 1)
            row[best_index] = 1
            row[j] = -best_to_others[j];
            row[-1] = -1
            A.append(row)
            b.append(0)

    # Others-to-Worst limit
    worst_index = criteria.index(worst_criterion)
    for j in range(n):
        if j != worst_index:
            row = np.zeros(n + 1)
            row[j] = 1
            row[worst_index] = -others_to_worst[j]
            row[-1] = -1
            A.append(row)
            b.append(0)

   
    sum_row = np.ones(n + 1)
    sum_row[-1] = 0  
    A.append(sum_row)
    b.append(1)

    # make sure all the weights aren't negative
    bounds = [(0, None) for _ in range(n)] + [(None, None)]  

    # linear to solve 
    res = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method='highs-ipm')

    if res.success:
        weights = res.x[:-1]
        xi = res.x[-1]
        return weights, xi
    else:
        print("❌ error information:", res.message)
        return None, None

# **get data from data.py**
criteria = data.criteria
best_criterion = data.best_criterion
worst_criterion = data.worst_criterion
best_to_others = data.best_to_others
others_to_worst = data.others_to_worst

# **print information**
print("\n📌 load dataset:")
print(f"✅ standard: {criteria}")
print(f"✅ best standard: {best_criterion}")
print(f"✅ worst standard: {worst_criterion}")
print(f"✅ Best-to-Others: {best_to_others}")
print(f"✅ Others-to-Worst: {others_to_worst}")

# **run BWM **
weights, xi = bwm(criteria, best_criterion, worst_criterion, best_to_others, others_to_worst)

# **out the result**
if weights is not None:
    print("\n✅ success! BWM weights:")
    for crit, weight in zip(criteria, weights):
        print(f"{crit}: {weight:.4f}")
    print(f"\n✅ consist index ξ: {xi:.4f}")
else:
    print("\n❌ failed, program terminated!")
