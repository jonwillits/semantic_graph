import sys
from src import network

def main():
    top_node = sys.argv[1]
    my_graph = network.ConceptGraph(top_node)
    my_graph.add_concepts(top_node)
    my_graph.output_graph()
    my_graph.plot_graph()
main()