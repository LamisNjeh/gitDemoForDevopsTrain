import numpy as np 

a = np.array(3,3)
for i in range(3) :
    for j in range(3) :
        a[i][j] = i+j
print('Done')