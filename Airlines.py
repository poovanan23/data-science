import pandas as pd
import numpy as np
import matplotlib.pylab as plt
Airlines=pd.read_csv("C://Users//POOVAYUVA//Desktop//EXCELR ASSIGN//CLUSTERING//EastWestAirlines.csv")
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)
df_norm = norm_func(Airlines.iloc[:,[1,2,6,7,8,9,10]])
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

Airlines['clust']=cluster_labels # creating a  new column and assigning it to new column 
Airlines = Airlines.iloc[:,[12,1,2,6,7,8,9,10,11]]
Airlines.head()

# getting aggregate mean of each cluster

Airlines.iloc[:,2:].groupby(Airlines.clust).median()

# creating a csv file 
Airlines. to_csv("Airlines.csv",encoding="utf-8")
Airlines