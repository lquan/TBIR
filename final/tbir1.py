#!/usr/bin/env python

from my_pagerank import pagerank
import networkx as nx

def main():
    #read the graph using tab delimiter as an directed graph
    G = nx.read_adjlist("sample-tiny.txt", delimiter='\t', create_using=nx.DiGraph())
    #calculate PageRank with no damping factor
    #pr, it = pagerank(G,alpha=1.0,max_iter=50)
    #pr = nx.pagerank_scipy(G,alpha=1)
    #print "pagerank scipy", pr
    start = dict.fromkeys(G.nodes(),0)
    start['0'] = 0.3
    start['1']= 0.1
    start['2'] =0.1
    start['3'] = 0.1
    start['4'] = 0.4
    pr2 = pagerank(G,alpha=0.85,x_start=None)

    print "pagerank", pr2
    
    
if __name__ == "__main__":
    main()