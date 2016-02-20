#/bin/env python

"""Script to convert the file appriopriately """
""" tbir2.py INFILE OUTFILE """
__author__ = "Li Quan"

import sys
import networkx as nx

def main():
  #the file we are using
  working = sys.argv[1]
  #read the graph using tab delimiter as an directed graph
  G =nx.read_adjlist(working, delimiter='\t', create_using=nx.DiGraph())

  #we relabel the nodes, +1 for matlab indexing
  nb_nodes = len(G.nodes());
  mapping = dict( zip(sorted(G.nodes()), range(1,nb_nodes+1)) ) 
  Gnew = nx.relabel_nodes(G,mapping)
  #now write them in the new text file
  with open(sys.argv[2], 'w') as f:
    #print Gnew.node_labels 
    for edge in Gnew.edges_iter():
      f.write("%d %d 1\n" % (edge[0], edge[1]))
    #print the total
    f.write("%d %d 0" % (nb_nodes, nb_nodes))
# boilerplate main
if __name__ == "__main__":
    main()
