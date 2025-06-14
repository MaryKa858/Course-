import numpy as np
import pandas as pd
array = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64], [5, 25, 125], [6, 36, 216], [7, 49, 343]])
index_values = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
column_values = ['number', 'squares', 'cubes']
df = pd.DataFrame(data = array, index = index_values, columns = column_values)
print(df)