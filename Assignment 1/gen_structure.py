import snap 
import sys
import numpy as np
import matplotlib.pyplot as plt 



Rnd = snap.TRnd(42)
Rnd.Randomize()



name='none'

for arg in sys.argv:
    if arg=="p2p-Gnutella04-subgraph.elist":
        name="p2p-Gnutella04-subgraph.elist"
    if arg=='cit-HepPh-subgraph.elist':
    	name='cit-HepPh-subgraph.elist'
    if arg=='email-Enron-subgraph.elist':
        name='email-Enron-subgraph.elist'
    if arg=='soc-Epinions1-subgraph.elist':
        name='soc-Epinions1-subgraph.elist' 








# Take the name as an argument 


G1 = snap.LoadEdgeList(snap.PUNGraph, name, 0, 1)


print("Number of nodes in"+name+":"+str(G1.GetNodes()))

print("Number of edges in"+name+":"+str(G1.GetEdges()))


degree_7=0
maxi=-10000000

hd=[]

for EI in G1.Nodes():
	if(EI.GetDeg()==7):
		degree_7+=1

	if(maxi<EI.GetDeg()):
		maxi=EI.GetDeg()
		hd=[EI.GetId()]
	else:
		if(maxi==EI.GetDeg()):
			hd.append(EI.GetId())
		else:
			pass


print("Node id with highest degree in"+name+":"+str(hd))


DegToCntV = snap.TIntPrV()
deg = []
count = []
snap.GetDegCnt(G1, DegToCntV)
for item in DegToCntV:
    deg.append(item.GetVal1())
    count.append(item.GetVal2())
plt.plot(deg, count)
plt.xlabel('degree')
plt.ylabel('count')
plt.legend()
plt.savefig(name+'_deg_distr.png')
plt.show()    
print('Degree distribution of '+name+' is in: '+name+'_deg_distr.png')


#PAths in the network

n=G1.GetNodes()

diam1 = snap.GetBfsFullDiam(G1, 10, False)
diam2 = snap.GetBfsFullDiam(G1, 100, False)
diam3 = snap.GetBfsFullDiam(G1, 1000, False)

print("Approximate full diameter in"+name+" with sampling 10 nodes:"+str(diam1))
print("Approximate full diameter in"+name+" with sampling 100 nodes:"+str(diam2))
print("Approximate full diameter in"+name+" with sampling 1000 nodes:"+str(diam3))

l=[diam1,diam2,diam3]

mean=(diam1+diam2+diam3)/3
var=np.var(l)

print("Approximate full diameter in"+name+" with sampling nodes (mean and variance):"+str(mean)+","+str(var))




diam1 = snap.GetBfsEffDiam(G1, 10, False)
diam2 = snap.GetBfsEffDiam(G1, 100, False)
diam3 = snap.GetBfsEffDiam(G1, 1000, False)

print("Approximate full diameter in"+name+" with sampling 10 nodes:"+str(diam1))
print("Approximate full diameter in"+name+" with sampling 100 nodes:"+str(diam2))
print("Approximate full diameter in"+name+" with sampling 1000 nodes:"+str(diam3))

l=[diam1,diam2,diam3]

mean=(diam1+diam2+diam3)/3
var=np.var(l)

print("Approximate full diameter in"+name+" with sampling nodes (mean and variance):"+str(mean)+","+str(var))





snap.PlotShortPathDistr(G1, name+'_shortest_path_length_distr', 'Undirected graph - shortest path')
print('Shortest path distribution of '+name+' is in: '+str(name+'_shortest_path_length_distr.png'))


#. Components of the network 



G1 = snap.LoadEdgeList(snap.PUNGraph, name, 0, 1)


print("Fraction of nodes in largest connected component in "+name+" is "+ str(snap.GetMxSccSz(G1)))



EdgeV = snap.TIntPrV()
snap.GetEdgeBridges(G1, EdgeV)

count=0
for edge in EdgeV:
	count=count+1

print("Number of edge bridges in "+name+" is "+str(count))

ArtNIdV = snap.TIntV()
snap.GetArtPoints(G1, ArtNIdV)

count=0
for i in ArtNIdV:
	count=count+1

print("Number of articluation points bridges in "+name+" is "+str(count))

snap.PlotSccDistr(G1, name+'_sizes_connected_components_distr', "Undirected graph - scc distribution")
print('Component size distribution of '+name+' is in: '+str(name+'_sizes_connected_components_distr.png'))


#Connectivity and clustering in the network 




G1 = snap.LoadEdgeList(snap.PUNGraph, name, 0, 1)


GraphClustCoeff = snap.GetClustCf (G1, -1)
print ("Average Clustering coefficient in "+name+": %f" % GraphClustCoeff)



NumTriads = snap.GetTriads(G1, -1)


print ("No of triads in "+name+": %d" % NumTriads)


#Put random node id in here
Rnd.Randomize()
node_id = G1.GetRndNId(Rnd)
# node_id = snap.TIntFltH()

# node_id = 12

print("The clustering coefficient of the node "+str(node_id)+" is "+str(snap.GetNodeClustCf(G1, node_id)))


Rnd.Randomize()
node_id = G1.GetRndNId(Rnd)

print ("Number of triads random node %d is %d" % (node_id, snap.GetNodeTriads(G1, node_id)))

Numtriedges = snap.GetTriadEdges(G1)
print('Number of edges that participate in at least one triad in '+name+': '+str(Numtriedges))


snap.PlotClustCf(G1, name+'_clustering_coeff_distr.png', "Undirected graph - clustering coefficient")
print('Clustering coefficient distribution of '+name+' is in: '+str(name+'_clustering_coeff_distr.png'))

















