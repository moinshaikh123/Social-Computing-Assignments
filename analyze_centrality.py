import snap 
import sys
import matplotlib.pyplot as plt 



Rnd = snap.TRnd(42)
Rnd.Randomize()



soc_Epinions1_subgraph = snap.LoadEdgeList(snap.PUNGraph, "soc-Epinions1-subgraph.elist", 0, 1)
cit_HepPh_subgraph = snap.LoadEdgeList(snap.PUNGraph, "cit-HepPh-subgraph.elist", 0, 1)
email_Enron_subgraph = snap.LoadEdgeList(snap.PUNGraph, "email-Enron-subgraph.elist", 0, 1)
p2p_Gnutella04_subgraph = snap.LoadEdgeList(snap.PUNGraph, "p2p-Gnutella04-subgraph.elist", 0, 1)



def intersection(lst1, lst2): 
   	lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = [0,0]
          
        for j in range(len(list1)):      
            if list1[j][1] > max1[1]: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
     return final_list


def func(cc,cc_,bc,bc_,closeness_cent,G):
	closeness_cent = {}
    for i in G.Nodes():
        node = i.GetId()
        closeness_cent[node] = snap.GetClosenessCentr(G, node)
    closeness_cent_sort = sorted(closeness_cent.iteritems(), key = lambda x : x[1])
    cc_ = []
    for i in range(len(closeness_cent_sort)-1, len(closeness_cent_sort)-11, -1):
        cc_.append(closeness_cent_sort[i][0])
    
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(G, Nodes, Edges, 0.8)
    betweenness_cent = {}

    for node in Nodes:
        betweenness_cent[node] = Nodes[node]


    betweenness_cent_sort = sorted(betweenness_cent.iteritems(), key = lambda x : x[1])
    bc_ = []

    
    for i in range(len(betweenness_cent_sort)-1, len(betweenness_cent_sort)-11, -1):
        bc_.append(betweenness_cent_sort[i][0])

    return [intersection(cc, cc_),intersection(bc, bc_)]

def get_compare(G, name):
    f1 = open(name+'_closeness_centrality.txt', 'r')
    f = f1.readlines()
    cc = []

    ind  = 0

    for i in f:
        node = i.strip().split()[0]
        value= i.strip().split()[1]
        cc.append([node,value])            
    
    f1.close()

    tc=Nmaxelements(cc,10)
    cc=[]
    for i in tc:
    	cc.append(i[0])

    f1 = open(name+'_betweenness_centrality.txt', 'r')
    
    f = f1.readlines()
    bc = []
    ind  = 0
    for i in f:
        node = i.strip().split()[0]
        value= i.strip().split()[1]
        bc.append([node,value])            
    
    f1.close()

    tc=Nmaxelements(bc,10)
    
    bc=[]
    for i in tc:
    	bc.append(i[0])
    
    
    [x,y]=func(cc,cc_,bc,bc_,closeness_cent,G)

    print('For : '+name)
    print('Number of overlaps for Closeness Centrality: '+str(len(x)))
    print('Number of overlaps for Betweenness Centrality: '+str(len(y))


# In[10]:

