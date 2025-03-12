import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

def test_disjoint_set():
    """Test the DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Initial state: each vertex is in its own set
    for i in range(5):
        assert ds.find(i) == i
    
    # Test union operation
    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(0, 2)
    
    # Check if vertices are in the same set after union
    assert ds.find(0) == ds.find(1)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)

def test_boruvka_mst_simple_graph():
    """Test Boruvka's algorithm on a simple connected graph."""
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    # MST should have vertices - 1 edges
    assert len(mst) == vertices - 1
    
    # Total weight of MST
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 19  # 5 + 6 + 8

def test_boruvka_mst_error_cases():
    """Test error cases for Boruvka's algorithm."""
    # Zero vertices
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(0, [(0, 1, 1)])
    
    # Insufficient edges
    with pytest.raises(ValueError, match="Insufficient edges to form a spanning tree"):
        boruvka_mst(4, [(0, 1, 1)])

def test_boruvka_mst_multiple_components():
    """Test Boruvka's algorithm with disconnected graph."""
    vertices = 6
    edges = [
        (0, 1, 5),
        (1, 2, 3),
        (3, 4, 7),
        (4, 5, 2)
    ]
    
    with pytest.raises(ValueError, match="Insufficient edges to form a spanning tree"):
        boruvka_mst(vertices, edges)

def test_boruvka_mst_complex_graph():
    """Test Boruvka's algorithm on a more complex graph."""
    vertices = 5
    edges = [
        (0, 1, 4),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 3),
        (1, 4, 1),
        (2, 3, 5),
        (3, 4, 7)
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    # MST should have vertices - 1 edges
    assert len(mst) == vertices - 1
    
    # Verify total cost
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 10  # Optimal MST sum