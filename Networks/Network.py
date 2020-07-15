import numpy as np

Class Network(object):
    
    def __init__(self, sizes):
        self.num_layer = len(size)
        self.sizes = sizes
        self.bias = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
