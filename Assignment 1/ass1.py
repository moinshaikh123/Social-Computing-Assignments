import snap


print "hello world"


G5 = snap.LoadEdgeList(snap.PUNGraph, "soc-Epinions1.txt", 0, 1)
G6 = snap.LoadEdgeList(snap.PUNGraph, "Cit-HepPh.txt", 0, 1)
G7 = snap.LoadEdgeList(snap.PUNGraph, "Email-Enron.txt", 0, 1)
G8 = snap.LoadEdgeList(snap.PUNGraph, "p2p-Gnutella04.txt", 0, 1)
dic1={}
dic2={}
dic3={}



G1 = snap.TUNGraph.New()
G2 = snap.TUNGraph.New()
G3 = snap.TUNGraph.New()


for EI in G5.Edges():
    a=EI.GetSrcNId()
    b=EI.GetDstNId()
    if((a%2)==1 and (b%2)==1):
        if(a not in dic1.keys()):
            G1.AddNode(a)
            dic1[a]=1
        if(b not in dic1.keys()):
            G1.AddNode(b)
            dic1[b]=1
        G1.AddEdge(a,b)
        # print(" ")
    else:
        pass

for EI in G6.Edges():
    a=EI.GetSrcNId()
    b=EI.GetDstNId()
    if((a%2)==0 and (b%2)==0):
        if(a not in dic2.keys()):
            G2.AddNode(a)
            dic2[a]=1
        if(b not in dic2.keys()):
            G2.AddNode(b)
            dic2[b]=1
        G2.AddEdge(a,b)
    else:
        pass
        # print(" ")

for EI in G7.Edges():
    a=EI.GetSrcNId()
    b=EI.GetDstNId()
    if((a%3)==0 and (b%3)==0):
        if(a not in dic3.keys()):
            G3.AddNode(a)
            dic3[a]=1
        if(b not in dic3.keys()):
            G3.AddNode(b)
            dic3[b]=1
        G3.AddEdge(a,b)
    else:
        pass
        # print(" ")



        


snap.SaveEdgeList(G1, "soc-Epinions1-subgraph.elist", "Save as tab-separated list of edges")
snap.SaveEdgeList(G2, "cit-HepPh-subgraph.elist", "Save as tab-separated list of edges")
snap.SaveEdgeList(G3, "email-Enron-subgraph.elist", "Save as tab-separated list of edges")
snap.SaveEdgeList(G8, "p2p-Gnutella04-subgraph.elist", "Save as tab-separated list of edges")

































