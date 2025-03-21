# https://colab.research.google.com/drive/1XkacTmtSBvZmx_5K9cfz8t1Ao5j-D-bZ?usp=sharings
# https://www.arxiv.org/pdf/2404.06370
# Enhancing decision analysis with a large language model: pydecision a comprehensive library of MCDA methods in python
# V Pereira, MP Basilio, CHTSCHT Santos
# arXiv preprint arXiv:2404.06370, 2024•arxiv.org



###### Exemple fonctionnel
import numpy as np

from pyDecision.algorithm import bw_method #

# BWM

# Intensity Scale = 1, 2, 3, 4, 5, 6, 7, 8, 9

# Most Important Criteria (The Second Criterion is the Best)
mic = np.array([2, 1, 4, 3, 8])

# Least Important Criteria (The Fifth Criterion is the Worst)
lic = np.array([4, 8, 2, 3, 1])

# Call BWM Function
weights = bw_method(mic, lic, eps_penalty = 1, verbose = True)

# Weigths
for i in range(0, weights.shape[0]):
    print('w(g'+str(i+1)+'): ', round(weights[i], 8))


# Generate fake data
np.random.seed(43)  # For reproducibility
data = np.round(np.random.rand(10, len(mic)) * 100) / 10  # 10 rows of data with the same number of columns as criteria, rounded to the nearest 0.1

# Apply weights to the data
weighted_data = data * weights

# Sum the weighted data for each row to get a score
scores = np.sum(weighted_data, axis=1)

# Find the row with the highest score
best_row_index = np.argmax(scores)
print(data)
print(f'The row with the highest score is row {best_row_index} with a score of {scores[best_row_index]:.8f}')