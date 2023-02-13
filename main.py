# from sklearn.datasets import load_digits
# import matplotlib.pylab as plt
# import pandas as pd
# import numpy as np
#
#
# digits = load_digits()
# samples = [0,10,20,30,1,11,22,31]
# d = []
# for i in range(len(samples)):
#     d.append(digits.images[samples[i]])
#
# v = []
# for i in range(8):
#     v.append(d[i].reshape(64, 1))
# print(v[1].shape)
# plt.figure(figsize=(10, 5))
# for i in range(8):
#     plt.subplot(1, 8, i + 1)
#     plt.imshow(v[i], aspect=0.4,
#                interpolation='nearest', cmap=plt.cm.bone_r)
#     plt.grid(False); plt.xticks([]); plt.yticks([])
#     plt.title("Vector {}".format(i + 1))
# plt.suptitle("Vectorized Image", y=1.05)
# plt.tight_layout(w_pad=7)
# plt.show()











