from typing import List, Tuple, Dict, Set

class DisjointSet:
    def __init__(self, vertices: int):
        """
        Initialize a Disjoint Set data structure.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of an element with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the given vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> None:
        """
        Union two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def boruvka_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, int]]): List of edges (from_vertex, to_vertex, weight)
    
    Returns:
        List[Tuple[int, int, int]]: Edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If insufficient edges or vertices
    """
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if len(edges) < vertices - 1:
        raise ValueError("Insufficient edges to form a spanning tree")

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Create disjoint set
    ds = DisjointSet(vertices)
    mst = []

    # Continue until we have vertices - 1 edges in MST
    while len(mst) < vertices - 1:
        cheapest = [None] * vertices

        # Find the cheapest edge for each component
        for i, (u, v, weight) in enumerate(edges):
            set_u = ds.find(u)
            set_v = ds.find(v)

            if set_u != set_v:
                if cheapest[set_u] is None or weight < cheapest[set_u][2]:
                    cheapest[set_u] = (u, v, weight)
                
                if cheapest[set_v] is None or weight < cheapest[set_v][2]:
                    cheapest[set_v] = (u, v, weight)

        # Add cheapest edges to MST
        for cheap in cheapest:
            if cheap is not None:
                u, v, weight = cheap
                set_u = ds.find(u)
                set_v = ds.find(v)

                if set_u != set_v:
                    ds.union(u, v)
                    mst.append((u, v, weight))

    return mst