import h5py
import numpy as np

mat_file = h5py.File('../data/Houston13.mat', 'r')
# 打印文件的结构
# for key, value in mat_file.items():
#     print(key, value)
dataset = mat_file['ori_data']
data = dataset[:, :, :]
print(dataset)
print(data)

label = h5py.File('../data/Houston13_7gt.mat', 'r')
# 打印文件的结构
# for key, value in label.items():
#     print(key, value)
label_data = label['map']
label = label_data[()]
print(label_data)
print(label)
