import os
import sys
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import wordnet as wn

from src import config

class ConceptGraph:

    def __init__(self, top_node):
        self.G = nx.DiGraph()
        self.edge_label_dict = {}
        self.G.add_node(top_node)

    def add_concept(self, parent, concept):
        if parent in self.G:
            self.G.add_node(concept)
            self.G.nodes[concept]['parent'] = parent
            self.G.add_edge(parent, concept, edge_type='IS_A')
            self.edge_label_dict[(parent,concept)] = 'IS_A'
        else:
            print('ERROR: parent {} not in concept graph'.format(parent))
            sys.exit()

    def add_concepts(self, start_node, depth=1):
        pass
        #synset_list =
        # if len(synset_list) == 0:
        #     print("Start node has no synsets")
        #     sys.exit(0)

        #print(synset_list)


    def output_graph(self):
        print(self.G.nodes.data())

    def plot_graph(self):
        pos = graphviz_layout(self.G, prog='dot')
        plt.figure(figsize=(30,6))
        nx.draw_networkx(self.G,
                         pos,
                         with_labels=True,
                         arrows=True,
                         font_size=8)
        nx.draw_networkx_edge_labels(self.G,
                                     pos,
                                     label_pos=0.5,
                                     font_size=8,
                                     edge_labels=self.edge_label_dict)
        plt.show()
        plt.savefig('nx_test.png')

