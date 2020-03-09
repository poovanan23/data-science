import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\EXCELR ASSIGN\ARM\my_movies.csv")
    

data.info()

data.columns

new_data = data.drop(['V1', 'V2', 'V3', 'V4', 'V5'], axis = 1)

apri = apriori(new_data, max_len = 3, min_support = 0.20, use_colnames = True)
rules = association_rules(apri, metric='confidence', min_threshold=0.5)

help(association_rules)

import matplotlib.pyplot as plt

def draw_graph(rules, rules_to_show):
    import networkx as nx
    G1 = nx.DiGraph()
    
    color_map = []
    N = 50
    colors = np.random.rand(N)
    strs = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11']
    for i in range(rules_to_show):
        G1.add_nodes_from(["R" + str(i)])
        for a in rules.iloc[i]['antecedents']:
            G1.add_nodes_from([a])
            G1.add_edge(a, "R"+str(i), color = colors[i], weight = 2)
        for c in rules.iloc[i]['consequents']:
            G1.add_nodes_from([c])
            G1.add_edge("R" + str(i), c, color = colors[i], weight =2)
    for node in G1:
        found_a_string = False
        for item in strs:
            if node == item:
                found_a_string = True
        if found_a_string:
            color_map.append('yellow')
        else:
            color_map.append('green')
    edges = G1.edges()
    colors = [G1[u][v]['color'] for u,v in edges]
    weight = [G1[u][v]['weight'] for u,v in edges]
    
    pos = nx.spring_layout(G1, k =16, scale =1)
    nx.draw(G1, pos, edges = edges, node_color = color_map, edge_color = colors, weight= weight, font_size = 16, with_labels = False)
    
    for p in pos:
        pos[p][1] +=0.07
    nx.draw_networkx_labels(G1, pos)
    plt.show()
    
import seaborn as sns

sns.set()
draw_graph(rules, 3)
