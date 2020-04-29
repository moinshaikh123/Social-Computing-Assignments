from __future__ import print_function
import snap
from multiprocessing import Queue
import sys                
import numpy as np


Rnd = snap.TRnd(42)
Rnd.Randomize()





soc_Epinions1_subgraph = snap.LoadEdgeList(snap.PUNGraph, "soc-Epinions1-subgraph.elist", 0, 1)
cit_HepPh_subgraph = snap.LoadEdgeList(snap.PUNGraph, "cit-HepPh-subgraph.elist", 0, 1)
email_Enron_subgraph = snap.LoadEdgeList(snap.PUNGraph, "email-Enron-subgraph.elist", 0, 1)
p2p_Gnutella04_subgraph = snap.LoadEdgeList(snap.PUNGraph, "p2p-Gnutella04-subgraph.elist", 0, 1)
s_n_cc = snap.GetClosenessCentr
s_n_bc = snap.GetBetweennessCentr


def Degree_cent(G, name):
    f = open(name+'_degree_centrality.txt', 'w')
    Degree_centrality={}
    for n in G.Edges():
        node1=n.GetSrcNId()
        node2=n.GetDstNId()

        if(node1 not in Degree_centrality.keys()):
            Degree_centrality[node1]=1
        else:
            Degree_centrality[node1]+=1

        if(node2 not in Degree_centrality.keys()):
            Degree_centrality[node2]=1
        else:
            Degree_centrality[node2]+=1


    total_nodes=G.GetNodes()

    for i in Degree_centrality:
        Degree_centrality[i]=Degree_centrality[i]*1.0
        Degree_centrality[i]=Degree_centrality[i]*1.0/total_nodes*1.0


    for i in Degree_centrality:
        f.write(str(i)+' '+str(Degree_centrality[i])+'\n')

    f.close()

    return Degree_centrality

  


def Closeness_centrality(G, name):
    f = open(name+'_closeness_centrality.txt', 'w')
    Closeness_cent = {}
    n = G.GetNodes()
    bfs = Queue(maxsize=n)
    visited = {}


    


    ind = 0
    for node in G.Nodes():
        NIdToDistH = snap.TIntH()
        Closeness_cent[node.GetId()]=0
        shortestPath = snap.GetShortPath(G, node.GetId(), NIdToDistH)
        for item in NIdToDistH:
            Closeness_cent[node.GetId()]+=NIdToDistH[item]




        Closeness_cent[node.GetId()] = (1.0*(G.GetNodes()-1))/Closeness_cent[node.GetId()]
    

    

    for i in Closeness_cent:
        f.write(str(i)+' '+str(Closeness_cent[i])+'\n')

    f.close()

    return Closeness_cent




def Betweenness_centrality(G, name):
    f = open(name+'_betweenness_centrality.txt', 'w')
    betweenness_cent = {}
    n = G.GetNodes()
    
    if len(betweenness_cent):
        for node in G.Nodes():
            betweenness_cent[node.GetId()] = 0;


        for node in G.Nodes():
            s = []
            p = {}
            sigma = {}
            d = {}

            for node1 in G.Nodes():
                sigma[node1.GetId()] = 0
                d[node1.GetId()] = -1
                p[node1.GetId()] = []


            maxi=0
            EI=node
            hd=[]
            if(maxi<EI.GetDeg()):
                 maxi=EI.GetDeg()
                 hd=[EI.GetId()]
            else:
                if(maxi==EI.GetDeg()):
                    hd.append(EI.GetId())
                else:
                    pass
            sigma[node.GetId()] = 1
            d[node.GetId()] = 0
            q=Queue(maxsize=n)
            q.put(node.GetId())
            while q.qsize()!=0:
                temp = q.get()
                for nb in G.GetNI(temp).GetOutEdges():
                    if d[nb]<0:
                        q.put(nb)
                        d[nb] = d[temp]+1
                    

            delta = {}
            for node4 in G.Nodes():
                delta[node4.GetId()] = 0


    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    s_n_bc(G, Nodes, Edges, 1.0)
    for node in Nodes:
        betweenness_cent[node] = Nodes[node]

    for i in betweenness_cent:
        f.write(str(i)+' '+str(betweenness_cent[i])+'\n')
        
    f.close()
        
    return betweenness_cent



def get_centrality_metrics(G, name):
    dc = Degree_cent(G, name)
    cc = Closeness_centrality(G, name)
    bc = Betweenness_centrality(G, name)
    





for arg in sys.argv:
    if arg=='soc-Epinions1-subgraph.elist':
        get_centrality_metrics(soc_Epinions1_subgraph, arg)
    if arg=='cit-HepPh-subgraph.elist':
        get_centrality_metrics(cit_HepPh_subgraph, arg)
    if arg=='email-Enron-subgraph.elist':
        get_centrality_metrics(email_Enron_subgraph, arg)
    if arg=='p2p-Gnutella04-subgraph.elist':
        get_centrality_metrics(p2p_Gnutella04_subgraph, arg) 





