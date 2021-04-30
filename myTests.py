from myGraphs import Graph, UndirectedGraph, DirectedGraph, Vertex, Weights

def create_graph_1():
    G = UndirectedGraph()

    for i in ['r','s','t','u','v','w','x','y']:
        G.add_vertex(Vertex(i))
    
    for (v1,v2) in [('v','r'),('r','s'),('s','w'),
              ('w','t'),('w','x'),('t','x'),
              ('t','u'),('x','u'),('x','y'),('u','y')]:
    
        G.add_edge(G.id_to_v[v1],G.id_to_v[v2])
    
    return G

def create_graph_2():
    G = DirectedGraph()
    
    for i in ['u','v','w','x','y','z']:
        G.add_vertex(Vertex(i))
        
    for (v1,v2) in [('u','x'),('u','v'),('x','v'),('v','y'),
                    ('y','x'),('w','y'),('w','z'),('z','z')]:
        
        G.add_edge(G.id_to_v[v1],G.id_to_v[v2])
        
    return G

def create_graph_3():
    G = DirectedGraph()
    
    for i in ['u','v','w','x','y','z']:
        G.add_vertex(Vertex(i))
        
    for (v1,v2) in [('u','x'),('u','v'),('v','y'),
                    ('y','x'),('w','y'),('w','z')]:
        
        G.add_edge(G.id_to_v[v1],G.id_to_v[v2])
        
    return G    

def create_graph_4():
    G = UndirectedGraph()
    W = Weights()

    for i in ['a','b','c','d','e','f']:
        G.add_vertex(Vertex(i))

    for (v1,v2,w) in [('a','b',1),('a','e',2),('d','e',1),('b','e',5),('b','f',1),('c','e',3),('c','f',1)]:
        G.add_edge(G.id_to_v[v1],G.id_to_v[v2])
        G.set_weight(W,G.id_to_v[v1],G.id_to_v[v2],w)

    return G, W

G4, W4 = create_graph_4()
print(G4.str_edges())
print(W4)
G4.MST(W4,G4.id_to_v['a'])
print(G4)
G4.MST(W4,G4.id_to_v['b'])
print(G4)