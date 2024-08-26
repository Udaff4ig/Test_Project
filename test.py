import networkx as nx
import matplotlib.pyplot as plt

weighted_graph = {
   'A': {'B': 5, 'C': 2},
   'B': {'A': 5, 'D': 4, 'E': 3},
   'C': {'A': 2, 'F': 7},
   'D': {'B': 4},
   'E': {'B': 3, 'F': 6},
   'F': {'C': 7, 'E': 6}
}

# Создаем направленный граф
G = nx.DiGraph()

# Добавляем узлы и ребра в граф
for node, edges in weighted_graph.items():
   G.add_node(node)
   for neighbor, weight in edges.items():
       G.add_edge(node, neighbor, weight=weight)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()