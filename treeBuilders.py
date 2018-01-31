'''
simpleIterative: iterative function that constructs a digraph with any given
    number of nodes

simpleRecursive: recursive function that constructs a digraph with any given
    number of nodes
'''
import string
import math
from graph import Digraph
import timeit

def simpleIterative(nodeCount):
    nodes = []
    graph = Digraph()
    # Digraph object stores a list of nodes and a dictionary of node:childrenList
    for i in range(nodeCount):
        nodes.append(str(i))
        graph.addNode(nodes[i])
    levelCount = int(math.log(nodeCount, 2)) + 1
    extraNodes = nodeCount - 2**(levelCount - 1)

    # attach nodes for all complete levels:
    index = 1
    for level in range(1, levelCount - 1):
        nodes_to_add = 2**level
        parentCount = nodes_to_add // 2
        parents = nodes[index-parentCount : index]
        for parent in parents:
            graph.connect(parent, nodes[index])
            graph.connect(parent, nodes[index + 1])
            index += 2

    # attach nodes for the last, incomplete level
    for node in nodes[index:]:
        parentIndex = index//2
        parent = nodes[index - 1 - parentIndex]
        graph.connect(parent, node)
        index += 1

    return graph

def simpleRecursive(nodeCount):
    nodes = []
    graph = Digraph()
    for i in range(nodeCount):
        nodes.append(str(i))
        graph.addNode(nodes[i])

    def recurBuild (graph, nodes, parentNodes=[]):
        # handle first call
        if parentNodes == []:
            parentNodes = [nodes[0]]
            nodes = nodes[1:]

        # base case - not enough nodes for another complete level of tree
        if len(nodes)//2 < len(parentNodes):
            parentIndex = 0
            while len(nodes) > 1:
                graph.connect(parentNodes[parentIndex], nodes[0])
                graph.connect(parentNodes[parentIndex], nodes[1])
                nodes = nodes[2:]
                parentIndex += 1
            if len(nodes) == 1:
                graph.connect(parentNodes[parentIndex], nodes[0])
            return graph

        # recursive case - enough for another level of tree
        else:
            nextParents = []
            for parent in parentNodes:
                graph.connect(parent, nodes[0])
                graph.connect(parent, nodes[1])
                nextParents.extend(nodes[:2])
                nodes = nodes[2:]
            return recurBuild(graph, nodes, nextParents)

    return recurBuild(graph, nodes)

# TIMETEST - iterative is ~35% faster
# print(timeit.timeit('simpleIterative(1000)', 'from __main__ import simpleIterative', number=1000))
# print(timeit.timeit('simpleRecursive(1000)', 'from __main__ import simpleRecursive', number=1000))
