import pandas as pd
import numpy as np
import matplotlib.pylab as plt
Crime=pd.read_csv("C://Users//POOVAYUVA//Desktop//EXCELR ASSIGN//CLUSTERING//crime_data.csv")
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)
df_norm = norm_func(Crime.iloc[:,[1,2,3,4]])


from scipy.cluster.hierarchy import linkage

import scipy.cluster.hierarchy as sch # for creating dendrogram 

type(df_norm)

z = linkage(df_norm, method="complete",metric="euclidean")

plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')

sch.dendrogram(
    z,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

from	sklearn.cluster	import	AgglomerativeClustering 

h_complete	=	AgglomerativeClustering(n_clusters=3,	linkage='complete',affinity = "euclidean").fit(df_norm) 



cluster_labels=pd.Series(h_complete.labels_)

Crime['clust']=cluster_labels # creating a  new column and assigning it to new column 

Crime = Crime.iloc[:,[5,1,2,3,4]]

Crime.head()

Crime.iloc[:,:].groupby(Crime.clust).median()

# creating a csv file 
Crime.to_csv("Crime.csv",encoding="utf-8")
