import numpy as np

class Bar1D:
    """
    1D bar element with 2 nodes.

    Attributes:

    id: int
        Element index.
    
    nid1: int
        Node index 1.
    
    nid2: int
        Node index 2.

    length: float
        Element length.
    
    particles: list
        List of particles in bar.
    """

    def __init__(self):
        self.id = None
        self.nodes = [None, None]
        self.nnodes = 2
        self.size = np.array([0])
        self.particles = []