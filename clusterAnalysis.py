import numpy

class graph():
  """
  This class implements a model of a graph in the union-find paradigm.
  The graph is a set of N nodes numbered from 0,...,N-1. The permitted operations are
  A. union(n1,n2)   : Add a connection between nodes n1, n2 (these nodes are now "connected")
  B. clusterSizes() : Return a list of sizes of all clusters in the graph (a cluster is set of connected nodes)
  """

  def __init__(self,numNodes,connections=[]):
    """
    Initialize a graph with nodeNum nodes, and a list of 
    connnections. The connections list has tupples that indicate
    pairs of nodes that are connected. 
    """
    self.numNodes = numNodes
    self.root = numpy.arange(numNodes) # To begin with, every node is its own root
    for con in connections:
      self.union(con[0],con[1])


  def __findRoot(self,n):
    """
    Return the root of element n, and its distance to the root
    """
    dist = 0
    orgNode = n
    while n != self.root[n]:
      n = self.root[n]
      dist += 1

    self.root[orgNode] = n
    return n, dist

  def __flatten(self):
    """
    Flatten the root array so that the tree height is 1.
    """
    for i in range(self.numNodes):
      self.root[i] = self.__findRoot(i)[0]

  def union(self,n1,n2):
    """
    Update the array "root" to indicate a connection between nodes n1, n2
    """
    if n1 >= self.numNodes or n2 >= self.numNodes or n1 < 0 or n2 < 0:
      raise Exception('Nodes out of range [0,%d)'%(self.numNodes))
    root1, h1 = self.__findRoot(n1)
    root2, h2 = self.__findRoot(n2)

    if root1 != root2:
      if h1 < h2:
	self.root[root1] = root2
      else:
	self.root[root2] = root1

  def clusterCounts(self):
    """
    Return a dictionary of cluster sizes and counts.
    """

    # Polulate a dictionary of cluster roots and corresponding sizes
    rootAndSize = dict()
    for rId in [self.__findRoot(i)[0] for i in range(self.numNodes)]:
      rootAndSize[rId] = rootAndSize.get(rId,0) + 1

    sizeCounts = dict()
    for size in rootAndSize.values():
      if size > 1: # Ignore size 1 clusters...
	sizeCounts[size] = sizeCounts.get(size,0)+1

    return sizeCounts


