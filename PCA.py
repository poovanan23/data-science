import pandas as pd 
import numpy as np
wine = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\EXCELR ASSIGN\pca\wine.csv")
wine.describe()
wine.head()


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 

# Considering only numerical data 
wine.data = wine.ix[:,1:]
wine.data.head(4)

# Normalizing the numerical data 
wine_normal = scale(wine.data)

pca = PCA(n_components = 3)

pca_values = pca.fit_transform(wine_normal)
pca1 = pd.DataFrame(data = pca_values, columns = ['principal component 1', 'principal component 2','principal component 3'])


# The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var
sum(var)
pca.components_[0]

# Cumulative variance 

var1 = np.cumsum(np.round(var,decimals = 4))
var1
sum(var1)
# Variance plot for PCA components obtained 
plt.plot(var1,color="red")

# plot between PCA1 and PCA2 
x = pca_values[:,0]
y = pca_values[:,1]
z = pca_values[:,2:3]
plt.scatter(x,y,c='red')
round(np.corrcoef(x,y)[0][1],4)
from mpl_toolkits.mplot3d import Axes3D
Axes3D.scatter(x,y,z,c='red')



################### Kmeans_Clustering  ##########################
new_df =pca1

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 3)
kmeans.fit(new_df)
kmeans.labels_
md=pd.Series(kmeans.labels_)
wine.data['clust']=md

################# heirarchial_clustering #########################

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import linkage
plt.figure(figsize=(10,1));plt.title("Dendogram")

z = linkage(new_df, method="complete",metric="euclidean")

plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()



from	sklearn.cluster	import	AgglomerativeClustering 
h_complete	=	AgglomerativeClustering(n_clusters=3,	linkage='complete',affinity = "euclidean").fit(new_df) 


cluster_labels=pd.Series(h_complete.labels_)


wine.data["Clusster"] = cluster_labels

grop = wine.data.groupby("Clusster").mean()

wine_data = wine.data


