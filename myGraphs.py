from math import inf

# Vertex class with attributes (dict)
class Vertex:
    
    def __init__(self,id):
        self.attributes = {}

        # unique id
        self.attributes['id'] = id
        
        # discovery time
        self.attributes['disc'] = -1
        
        # finishing time
        self.attributes['fin'] = -1
        
        # status = 
        # 'u' unvisited
        # 'p' processing
        # 'f' finished
        self.attributes['status'] = 'u'
        
    def __str__(self):
        return str(self.attributes)
        
    def set(self,key,value):
        self.attributes[key] = value
        
    def get(self,key):
        return self.attributes[key]

# Weights class that accompany graphs to implement edge weights to any graph
class Weights:

    def __init__(self):
        self.edge_dict = {}

    def __str__(self):
        string = ''
        for (v1,v2), w in self.edge_dict.items():
            string += '(' + v1.get('id') + ',' + v2.get('id') + ') : ' + str(w) + '\n'
        return string
    
    def add_weight(self, v1, v2, w):
        self.edge_dict[(v1,v2)] = w

    def get_weight(self, v1, v2):
        return self.edge_dict[(v1,v2)]

# Graph class that implements BFS and DFS generally
# Uses adjacency list to implement edges
class Graph:
    
    def __init__(self):
        # id to v translates unique ID's to vertex objects
        self.id_to_v = {}
        self.adj_list = {}
        
    # Returns a string of vertices
    def __str__(self):
        string = ''
        for v in self.id_to_v.values():
            string += str(v) + '\n'
        return string
    
    # Returns a string of edges
    def str_edges(self):
        string = ''
        for u, arr_v in self.adj_list.items():
            string += u.get('id') + ' : '
            for v in arr_v:
                if isinstance(v, dict):
                    string += '(' + v[v].get('id') + ',' + v[w] +') '
                else:
                    string += v.get('id') + ' '
            string += '\n'
        return string
                    
    def add_vertex(self,v):
        self.id_to_v[v.get('id')] = v
        self.adj_list[v] = []
    
    # Sets the status of all vertices to unvisited
    def clear_status(self):
        for v in self.id_to_v.values():
            v.set('status','u')
    
    # Starting vertex v is given, function returns list of vertices in order of search
    def BFS(self, v): 
        
        self.clear_status()
        queue = [v]
        
        visited_order = []
        v.set('disc', 0)
        
        # O(|V|) visit every vertex
        while len(queue) > 0:
            
            current_v = queue.pop(0)
            
            # O(|E|) traverse every edge
            # Nested for loop does not multiply complexity
            # Vertices are processed only if they are unvisited
            for u in self.adj_list[current_v]:
                
                if u.get('status') == 'u':
                    
                    u.set('status','p')
                    u.set('disc', current_v.get('disc') + 1)
                    queue.append(u)
                    visited_order.append(u.get('id'))
                    
            current_v.set('status','f')
            
        return visited_order

    # DFSVisit runs DFS starting at vertex v
    # Flag scc is used to determine if DFSVisit is called for SCC
    # scc_list is used to store SCCs
    def DFSVisit(self, v, time, scc=False, scc_list=None):

        time += 1
        v.set('status', 'p')
        if scc == False:
            v.set('disc', time)
        else:
            scc_list.append(v.get('id'))

        # O(|E|) traverse every edge
        for u in self.adj_list[v]:
            if u.get('status') == 'u':
                time = self.DFSVisit(u, time, scc, scc_list)
        
        time += 1
        v.set('status','f')
        if scc == False:
            v.set('fin', time)

        return time
    
    # Runs DFS, making sure to visit all vertices in the graph
    def DFS(self):
    
        self.clear_status()
        time = 0
            
        # O(|V|) visit every vertex
        for current_v in self.id_to_v.values():
            if current_v.get('status') == 'u':
                # Running DFSVisit it for loop does not multiply complexity
                # Vertices are processed only if they are unvisited
                time = self.DFSVisit(current_v, time)

# UndirectedGraph class, inherits Graph methods
# add edge and set weight makes sure to add the edge/weight both directions
class UndirectedGraph(Graph):
        
    def add_edge(self,v1,v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def set_weight(self, W, v1, v2, weight):
        W.add_weight(v1, v2, weight)
        W.add_weight(v2, v1, weight)

    # Returns nothing, 'pi' attribute of each vertex is the parent's id in the MST
    def MST(self, W, r):
        Q = []
        # Adds all vertices to the Min Queue
        for u in self.id_to_v.values():
            u.set('key', inf)
            u.set('pi', None)
            Q.append(u)
        # Set the key for the root to 0
        r.set('key',0)
        # Remove vertices from the Min Queue
        # Find the adjacent edge with the lowest weight
        while len(Q) != 0:
            u = min(Q, key=lambda v : v.get('key'))
            Q.remove(u)
            for v in self.adj_list[u]:
                if v in Q and W.get_weight(u,v) < v.get('key'):
                    v.set('pi',u.get('id'))
                    v.set('key',W.get_weight(u,v))

# DirectedGraph class that inherits Graph
# add edge and set weight only do so in one direction
class DirectedGraph(Graph):
        
    def add_edge(self,v1,v2):
        self.adj_list[v1].append(v2)
        
    def set_weight(self, W, v1, v2, weight):
        W.add_weight(v1, v2, weight)

    # Checks discovery and finish time to determine if back edge
    def isBackEdge(self,u,v):
        return (v.get('disc') <= u.get('disc')) and (u.get('disc') < u.get('fin')) and (u.get('fin') <= v.get('fin'))
    
    # Scans the graph for a back edge
    def acyclic(self):
        self.DFS()
        for u, arr_v in self.adj_list.items():
            for v in arr_v:
                if self.isBackEdge(u,v) == True:
                    return False
        return True
    
    # Returns a list of vertex id's in topological order
    def topological_sort(self):
        
        self.DFS()
        
        if self.acyclic():
            result = sorted(self.adj_list ,reverse=True, key=lambda v : v.get('fin'))
            return list(map(lambda v: v.get('id'), result))
        else:
            return None

    # Returns a new transposed graph
    def transpose(self):
        GT = DirectedGraph()

        for v in self.id_to_v.values():
            GT.add_vertex(v)

        for u, arr_v in self.adj_list.items():
            for v in arr_v:
                GT.add_edge(v,u)

        return GT

    # Returns a list of SCCs
    def SCC(self):
        # First DFS to compute finishing times for all vertices
        self.DFS()
        # Transpose Graph
        GT = self.transpose()
        # Set all vertices in transposed graph to unvisited
        GT.clear_status()
        time = 0
        # Stores ssc in scc_tab as separate lists
        scc_tab = []
        # Second DFS by descending order of finish time
        sorted_v_list = sorted(GT.id_to_v.values(), reverse=True, key=lambda x : x.get('fin'))
        for current_v in sorted_v_list:
            if current_v.get('status') == 'u':
                scc_tab.append([])
                time = GT.DFSVisit(current_v, time, scc=True, scc_list=scc_tab[len(scc_tab) - 1])
        # Output vertices in each tree of the DF forest as a SCC
        return scc_tab

    # Initializes the graph for a SSSP execution
    def init_SS(self, s):
        for v in self.id_to_v.values():
            v.set('d',inf)
            v.set('pi',None)
        s.set('d',0)

    # Checks the current shortest path and replaces with new weight if smaller
    def relax(self, u, v, w):
        if v.get('d') > (u.get('d') + w):
            v.set('d',u.get('d') + w)
            v.set('pi',u.get('id'))

    # Returns True if the SSSP algorithm suceeded
    # Returns False if the graph has a negative cycle and SSSP is invalid
    # Adds 'pi' (parent vertex) and 'd' (shortest path weight) attributes to all vertices
    def SSSP(self, W, s):
        self.init_SS(s)
        for i in range(len(self.id_to_v.values())):
            for u, arr_v in self.adj_list.items():
                for v in arr_v:
                    self.relax(u,v,W.get_weight(u,v))
        for u, arr_v in self.adj_list.items():
            for v in arr_v:
                if v.get('d') > (u.get('d') + W.get_weight(u,v)):
                    return False
        return True