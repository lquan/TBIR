#!/usr/bin/env python

from my_pagerank import pagerank
import numpy as num
import matplotlib.pyplot as plt
import time
import networkx as nx

def main():
    #read the graph using tab delimiter as an directed graph
    Gsmall = nx.read_adjlist("sample-tiny.txt", 
                        delimiter='\t', 
                        create_using=nx.DiGraph())
    Glarge = nx.read_adjlist("sample-large2.txt", 
                        delimiter='\t', 
                        create_using=nx.DiGraph())
    # "dangling" nodes, no links out from them; fix them
    #out_degree = G.out_degree()
    #for dangling in (n for n in G if out_degree[n]==0.0):
    #    for n in G:
    #        G.add_edge(dangling, n)
    #nx.stochastic_graph(G,False)              
    #calculate PageRank with
    #various damping values from 0 to 1 in increments of 0.05
    damping_values = num.arange(0.,1.05,0.05)
    
    times_small = []
    timesbig = []
    for damping in damping_values:
        print "calculating pagerank with alpha=%f ..." % damping  
        tic = time.clock()
        pr, it = pagerank(Glarge,alpha=damping,tol=1e-4)
        toc = time.clock()

        timesbig.append(toc-tic)
        
        tic = time.clock()
        pr, it = pagerank(Gsmall,alpha=damping,tol=1e-4)
        toc = time.clock()
        
        times_small.append(toc-tic)

    #plot the std, iterations and times
    
    plt.figure()
    plt.plot(damping_values, times_small, 'o-', label = 'small')
    plt.xlabel("damping factor")
    plt.ylabel("time (s)")
    
    plt.grid()
    plt.savefig("times1.pdf")
    
    plt.figure()
    plt.xlabel("damping factor")
    plt.ylabel("time (s)")
    plt.grid()
    plt.plot( damping_values, timesbig ,'o-', label = 'large')
    plt.savefig("times2.pdf")

if __name__ == "__main__":
    main()
