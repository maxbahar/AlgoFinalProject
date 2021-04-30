# CSCI3383 Algorithms Final Project
Author: Maximilian Bahar

I will work on the **default final project** and extend homework 5's graph API.

The following graph operations will be added:
* Strongly Connected Components (SCC) for directed graphs using Kosaraju
* Minimum Spanning Tree (MST) for weighted, connected, undirected graphs using Prim
* Single-source Shortest Path (SSSP) for weighted, directed graphs using Bellman-Ford or Dijkstra 

## Documentation

The graph API is implemented in myGraphs.py.
myTests.py imports the graph API and runs a few tests using the API.
View the tests run in the Examples section of this README.
The following classes are used in the graph API.

### Important Functions

The following functions assume that a Graph is declared using the following line of code:
> `G = UndirectedGraph()` or `G = DirectedGraph()`

To add a vertex, pass a Vertex object `v` to the following function:
> `G.add_vertex(v)`

To add an edge, pass two Vertex objects `v1` and `v2` to the following function:
> `G.add_edge(v1,v2)`

To add weights to a graph, declare a Weights object with the following:
> `W = Weights()`

Then, call the following function passing an integer `weight` and two vertex objects `v1` and `v2`:
> `G.set_weight(self,W,v1,v2,weight)`

### Graph Algorithms

The Breadth First Search (BFS) function starting at vertex `v` will return a list of vertex identifiers in order of visitation. Run BFS with the following function:
> `G.BFS(v)`

The Depth First Search (DFS) function will run depth first search for the entire graph (even without being connected) and marks the vertices with discovery and finish time.
> `G.DFS()`

The Strongly Connected Components (SCC) function will return a list of strongly connected components represented as lists of vertex identifiers. This function only works for directed graphs.
> `G.SCC()`

The Minimum Spanning Tree (MST) function returns nothing. It adds an attribute `'pi'` to each vertex representing the parent's identifier in the minimum spanning tree. This function only works for connected, weighted, undirected graphs.
> `G.MST(W,r)`

*Single Source Shortest Path still needs implementation using Dijkstra's*

## Examples

*Needs implementation*