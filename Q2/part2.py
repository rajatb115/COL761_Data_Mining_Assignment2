import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
from sklearn.decomposition import PCA
import scipy 
import time as t
import mtree
import math
import sys
from sklearn.preprocessing import StandardScaler

data = np.loadtxt(sys.argv[1])

data = StandardScaler().fit_transform(data)

pca_2 = PCA(n_components=2)
data_2 = pca_2.fit_transform(data)

pca_4 = PCA(n_components=4)
data_4 = pca_4.fit_transform(data)

pca_10 = PCA(n_components=10)
data_10 = pca_10.fit_transform(data)

pca_20 = PCA(n_components=20)
data_20 = pca_20.fit_transform(data)

tree_2 = KDTree(data_2,leafsize=1)
tree_4 = KDTree(data_4,leafsize=1)
tree_10 = KDTree(data_10,leafsize=1)
tree_20 = KDTree(data_20,leafsize=1)

random_query_2 = np.random.randint(low=1, high=100, size=(100,2), dtype=int)
random_query_4 = np.random.randint(low=1, high=100, size=(100,4), dtype=int)
random_query_10 = np.random.randint(low=1, high=100, size=(100,10), dtype=int)
random_query_20 = np.random.randint(low=1, high=100, size=(100,20), dtype=int)

time_2_kd = []
for point in random_query_2:
    begin = t.time()
    store = tree_2.query(point, k=5)
    end = t.time()
    time_2_kd.append(end-begin)

time_2_kd = np.array(time_2_kd)
mean_2_kd = np.mean(time_2_kd)
var_2_kd = np.std(time_2_kd)

time_4_kd = []
for point in random_query_4:
    begin = t.time()
    store = tree_4.query(point, k=5)
    end = t.time()
    time_4_kd.append(end-begin)
    
time_4_kd = np.array(time_4_kd)
mean_4_kd = np.mean(time_4_kd)
var_4_kd = np.std(time_4_kd)

time_10_kd = []
for point in random_query_10:
    begin = t.time()
    store = tree_10.query(point, k=5)
    end = t.time()
    time_10_kd.append(end-begin)

time_10_kd = np.array(time_10_kd)
mean_10_kd = np.mean(time_10_kd)
var_10_kd = np.std(time_10_kd)

time_20_kd = []
for point in random_query_20:
    begin = t.time()
    store = tree_20.query(point, k=5)
    end = t.time()
    time_20_kd.append(end-begin)

time_20_kd = np.array(time_20_kd)
mean_20_kd = np.mean(time_20_kd)
var_20_kd = np.std(time_20_kd)


def d_int(x, y):     
    return abs(x - y)

def euclidean_distance(data1, data2):
    distance = 0
    for v1, v2 in zip(data1, data2):
        diff = v1 - v2
        distance += diff * diff
    distance = math.sqrt(distance)
    return distance

tree_2 = mtree.MTree(euclidean_distance, max_node_size=4)
for n, point in enumerate(data_2, 1):
    tree_2.add(tuple(point))

tree_4 = mtree.MTree(euclidean_distance, max_node_size=4)
for n, point in enumerate(data_4, 1):
    tree_4.add(tuple(point))

tree_10 = mtree.MTree(euclidean_distance, max_node_size=4)
for n, point in enumerate(data_10, 1):
    tree_10.add(tuple(point))

tree_20 = mtree.MTree(euclidean_distance, max_node_size=4)
for n, point in enumerate(data_20, 1):
    tree_20.add(tuple(point))

time_2_mt = []
for point in random_query_2:
    store = tuple(point)
    begin = t.time()
    results = list(tree_2.search(store, 5))
    end = t.time()
    time = end - begin
    time_2_mt.append(time)
time_2_mt = np.array(time_2_mt)
mean_2_mt = np.mean(time_2_mt)
var_2_mt = np.std(time_2_mt)

time_4_mt = []
for point in random_query_4:
    store = tuple(point)
    begin = t.time()
    results = list(tree_4.search(store, 5))
    end = t.time()
    time = end - begin
    time_4_mt.append(time)
time_4_mt = np.array(time_4_mt)
mean_4_mt = np.mean(time_4_mt)
var_4_mt = np.std(time_4_mt)

time_10_mt = []
for point in random_query_10:
    store = tuple(point)
    begin = t.time()
    results = list(tree_10.search(store, 5))
    end = t.time()
    time = end - begin
    time_10_mt.append(time)
time_10_mt = np.array(time_10_mt)
mean_10_mt = np.mean(time_10_mt)
var_10_mt = np.std(time_10_mt)

time_20_mt = []
for point in random_query_20:
    store = tuple(point)
    begin = t.time()
    results = list(tree_20.search(store, 5))
    end = t.time()
    time = end - begin
    time_20_mt.append(time)
time_20_mt = np.array(time_20_mt)
mean_20_mt = np.mean(time_20_mt)
var_20_mt = np.std(time_20_mt)

def kNN_brute(dataset,query_point,k):
    index = []
    for i in range(0,len(dataset)):
        index.append(i)
    dist= []
    result = []
    for point in dataset:
        dist.append(np.dot(point-query_point,(point-query_point).T))
                    
    for i in range(0,k):
        dist_min = float('inf')
        idx = None
        for j in index:
            if dist[j] < dist_min:
                dist_min = dist[j]
                idx = j
        result.append(dataset[idx])
        index.pop(idx)
    return result

time_2_bf = []
for point in random_query_2:
    begin = t.time()
    store = kNN_brute(data_2,point,5)
    end = t.time()
    time_2_bf.append(end - begin)
time_2_bf = np.array(time_2_bf)
mean_2_bf = np.mean(time_2_bf)
std_2_bf = np.std(time_2_bf)

time_4_bf = []
for point in random_query_4:
    begin = t.time()
    store = kNN_brute(data_4,point,5)
    end = t.time()
    time_4_bf.append(end - begin)
time_4_bf = np.array(time_4_bf)
mean_4_bf = np.mean(time_4_bf)
std_4_bf = np.std(time_4_bf)

time_10_bf = []
for point in random_query_10:
    begin = t.time()
    store = kNN_brute(data_10,point,5)
    end = t.time()
    time_10_bf.append(end - begin)
time_10_bf = np.array(time_10_bf)
mean_10_bf = np.mean(time_10_bf)
std_10_bf = np.std(time_10_bf)

time_20_bf = []
for point in random_query_20:
    begin = t.time()
    store = kNN_brute(data_20,point,5)
    end = t.time()
    time_20_bf.append(end - begin)
time_20_bf = np.array(time_20_bf)
mean_20_bf = np.mean(time_20_bf)
std_20_bf = np.std(time_20_bf)

time_kd = [mean_2_kd,mean_4_kd,mean_10_kd,mean_20_kd]
time_mt = [mean_2_mt,mean_4_mt,mean_10_mt,mean_20_mt]
time_bf = [mean_2_bf,mean_4_bf,mean_10_bf,mean_20_bf]
error_kd = [var_2_kd,var_4_kd,var_10_kd,var_20_kd]
error_mt = [var_2_mt,var_4_mt,var_10_mt,var_20_mt]
error_bf = [std_2_bf,std_4_bf,std_10_bf,std_20_bf]
x_axis = [2,4,10,20]
plt.xlabel('Dimension')
plt.ylabel('Time in seconds')
plt.errorbar(x_axis, time_kd, xerr =0 , yerr = error_kd,label='kd-tree')
plt.errorbar(x_axis, time_mt, xerr =0 , yerr = error_mt,label='mtree')
plt.errorbar(x_axis, time_bf, xerr =0 , yerr = error_bf,label='brute force')
plt.legend()
plt.savefig(sys.argv[2])
