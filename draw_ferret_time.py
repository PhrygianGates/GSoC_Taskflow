import numpy as np
import matplotlib.pyplot as plt

t = [1, 2, 4, 8]
tf_time = [214.831, 133.153, 83.385, 52.673]
tbb_inorder_time = [214.112, 131.828, 82.604, 52.097]
pthreads_time = [168.799, 84.379, 42.459, 28.252]
tbb_outoforder_time = [214.298, 107.989, 54.105, 27.912]

plt.figure()
plt.plot(t, tf_time, t, tbb_inorder_time, t, tbb_outoforder_time, t, pthreads_time)
plt.legend(["taskflow", "tbb_in_order", "tbb_out_of_order", "pthreads"], loc="best")
plt.ylabel("time")
plt.xlabel("threads")
plt.show()