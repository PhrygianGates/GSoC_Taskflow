import numpy as np
import matplotlib.pyplot as plt

t = [1, 2, 4, 8]
tf_time = [4.904, 1.443, 0.932, 0.721]
tbb_inorder_time = [4.820, 2.458, 1.315, 0.770]
pthreads_time = [4.284, 2.409, 1.664, 1.510]

plt.figure()
plt.plot(t, tf_time, t, tbb_inorder_time, t, pthreads_time)
plt.legend(["taskflow", "tbb_in_order", "pthreads"], loc="best")
plt.ylabel("time")
plt.xlabel("threads")
plt.show()