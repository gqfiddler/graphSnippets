'''
Digraph: a simple directed graph class adapted from EdX course "Introduction to
Computational Thinking and Data Science" (MIT 6.00.2x), Problem Set 5.
'''

class Digraph(object):
    '''
    A directed graph.  Assumes nodes are unique strings.  Stores nodes as list
    and edges as a dictionary of parent:childList pairs.
    '''
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def connect(self, parent, child):
        src = parent
        dest = child
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def getChildrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for src in self.edges:
            for dest in self.edges[src]:
                res = '{0}{1}->{2}\n'.format(res, src, dest)
        return res[:-1]
