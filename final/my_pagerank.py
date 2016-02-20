#!/usr/bin/env python

import networkx as nx

def pagerank(G, alpha=0.85, max_iter=100, tol=1e-4, x_start=None, personalization=None):
    """
    Compute and return the PageRank in an directed graph (also see networkx documentation).
    The output is a dictionary mapping the node-id to its PageRank value.
    Also, the number of iterations to convergence is returned.    
    """
    # some precondition checking. (we could also convert undirected to directed.)
    if not G.is_directed():
        raise Exception("pagerank() only defined for directed graphs.")

    # to be completely correct we should also remove self-referential nodes,
    # but let's just ignore this for performancy issues at the moment
    # and assume the input does not containt self-referential nodes.
    # G.remove_edges_from(G.selfloop_edges())

    nodes = G.nodes();
    nb_nodes = len(nodes);
    if nb_nodes == 0:
        return {}
    
    # value for nodes without backlinks
    min_value = (1.0-alpha)/nb_nodes

    # initial pagerank dict
    if x_start == None:
    # initialize the PageRank dict with 1/N for all nodes
        x = dict.fromkeys(nodes, 1.0/nb_nodes)
    else:
        x = x_start
        # normalize starting vector to 1                
        s = 1.0/sum(x.values())
        for k in x: x[k]*=s
        
    # assign uniform personalization/teleportation vector if not given
    """if personalization is None:
        p = dict.fromkeys(nodes,1.0/nb_nodes)
    else:
        p = personalization
        # normalize starting vector to 1               
        s = 1.0/sum(p.values())
        for k in p: 
            p[k]*=s
        if set(p)!=set(G):
            raise Exception('Personalization vector must have a value for every node')
    """
        
    # "dangling" nodes, no links out from them; fix them
    out_degree = G.out_degree()
    for dangling in (n for n in nodes if out_degree[n]==0.0):
        for n in nodes:
            G.add_edge(dangling, n)
    
    # create a copy in (right) stochastic form which we will use 
    # to avoid recalculating the number of outgoing links every time  
    W=nx.stochastic_graph(G)
    #W = G
    # now the iterative algorithm 
    # (which is basically a version of the power method, 
    # without using explicit matrix multiplications)
    i = 0
    while True: 
        # uncomment following 2 lines if you want to view each iteration
        #print "iteration %d:" % i
        #print "pagerank:", x 
        i += 1
        # after maximum iterations have been reached, stop
        if i > max_iter:
            print "no convergence after {0} iterations!".format(max_iter)
            break
        
        # some helper variables
        diff = 0 #total difference compared to last iteration
        x_new = dict.fromkeys(nodes, 0) # the dict where we store our new values
        
        # now the pagerank calculations
        for node in nodes:
            rank = min_value
            #print "node", node
            #print "min value", min_value
            for referring_page in W.predecessors_iter(node):
                #print "refered by ", referring_page
                #print "old value", old_pagerank[referring_page]
                #print "G out degree", G.out_degree(referring_page)
                rank += alpha * x[referring_page] * W[referring_page][node]['weight'] # or / G.out_degree(referring_page)
            # the personalization 
            # rank += min_value * p[node]
            diff += abs(rank - x[node]) #accumulate the difference
            x_new[node] = rank
        
        
        x = x_new # our new pagerank
        #print pagerank
                
        #stop if converged
        if diff < tol:
            #print "converged after {0} iterations".format(i)
            break

    #normalize PageRank
    total = sum(x.values())
    if total!=0:
        s = 1.0/total
        for n in x: 
            x[n] *= s 
   
    return x,i


