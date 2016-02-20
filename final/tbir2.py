#!/usr/bin/env python

from my_pagerank import pagerank
import numpy as num
import matplotlib.pyplot as plt
import time
import networkx as nx

def main():
    #read the graph using tab delimiter as an directed graph
    G = nx.read_adjlist("sample-large2.txt", 
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
    standard_deviations = []
    iterations = []
    times = []
    for damping in damping_values:
        print "calculating pagerank with alpha=%f ..." % damping  
        tic = time.clock()
        pr, it = pagerank(G,alpha=damping,tol=1e-4)
        toc = time.clock()
        
        """print "damping:", damping
        print "standard deviation:", num.std(pr.values())
        print "iterations:", it"""
        standard_deviations.append(num.std(pr.values()))
        iterations.append(it)
        times.append(toc-tic)

    #plot the std, iterations and times
    
    plt.figure()
    plt.plot(damping_values, standard_deviations, 'o-')
    plt.grid()
    plt.xlabel("damping factor")
    plt.ylabel("standard deviation")
    plt.savefig("standard_deviation.pdf")
    
    plt.figure()
    plt.plot(damping_values, iterations, 'o-', label = 'iterations')
    plt.xlabel("damping factor")
    plt.ylabel("iterations")
    plt.twinx()
    plt.ylabel("time (s)")
    plt.plot(damping_values, times, 'og-', label = 'time')
    plt.grid()
    plt.savefig("iterations.pdf")

    #plt.figure()
    #plt.plot(damping_values, times, 'o-')
    #plt.grid()
    #plt.ylabel("time (s)")
    #plt.xlabel("damping factor")
    #plt.savefig("times.pdf")


    #my_pr,iterations = pagerank(G)
    """pr = nx.pagerank(G)
    pr_numpy=nx.pagerank_numpy(G)
    pr_scipy= nx.pagerank_scipy(G)
    """
    
    """x = "10936880" #'8614504'
    print my_pr[x]
    print pr[x]
    print pr_numpy[x]
    print pr_scipy[x]
    #print sum(abs(num.array(my_pr.values())- num.array(pr_scipy.values())))
    """
    """
    pr, i = pagerank(G)
    print "pagerank vector:", pr.values()
    print "iterations:", i
    """
    #print "pagerank numpy:", pr_numpy.values()
    #print "pagerank scipy:", pr_scipy.values()


if __name__ == "__main__":
    main()
