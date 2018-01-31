'''
Contains function dynamicDFS, a dynamically programmed function to find all
possible paths through a digraph from one specified node to another.  The
motivation here was mostly to see how it could be done, but it could be useful
in any scenario where recursion is undesirable.
'''

import string

class SmartPos:
    def __init__(self, start):
        self.path = [start]
        self.memory = {start}

    def moveTo(self, dest):
        self.path.append(dest)
        self.memory.add(dest)

    def moveBack(self):
        self.path = self.path[:-1]

    def getPath(self):
        return self.path

    def getCurrentNode(self):
        try:
            return self.path[-1]
        except IndexError:
            # if all paths have been tested, the final moveBack will make path = []
            return None

    def beenThere(self, node):
        return node in self.memory


def dynamicDFS(graph, start, end):
    '''
    Args:
        graph: a digraph with function getChildrenOf(node), returning a set of nodes.
            Nodes can be any object type but must be separate objects.
        start: origin node object
        end: desination node object
    Returns:
            List of all valid paths (lists) in graph from origin to destination
    '''
    validPaths = []
    position = SmartPos(start)
    nodesToCheck = graph.getChildrenOf(start)

    while nodesToCheck != []:
        position.moveTo(nodesToCheck[-1])
        if position.getCurrentNode() == end:
            validPaths.append(position.getPath())
            nodesToCheck = nodesToCheck[:-1]
            position.moveBack()
        else:
            uncheckedChildren = []
            for childNode in graph.getChildrenOf(position.getCurrentNode()):
                # if child node is the end, just add the path if we don't already
                # have it recorded in validPaths
                if childNode == end:
                    path = position.getPath() + [end]
                    if path not in validPaths:
                        validPaths.append(path)
                # if we haven't checked the child node before, add it to uncheckedChildren
                elif not position.beenThere(childNode):
                    uncheckedChildren.append(childNode)
                # if we have checked the node before, test to see whether it's part
                # of a recorded valid path or not (if not, it's a dead end)
                else:
                    for knownPath in validPaths:
                        # if the child node leads to the end, add this path to validPaths
                        if childNode in knownPath:
                            nodeToEnd = knownPath[knownPath.index(childNode):]
                            newPath = position.getPath() + nodeToEnd
                            # but only if it's not a repeat
                            if newPath not in validPaths:
                                validPaths.append(newPath)
                        # if it doesn't lead to the end, it's a dead end and we
                        # can safely ignore it - no action needed

            if uncheckedChildren == []:
                position.moveBack()
                nodesToCheck = nodesToCheck[:-1]
            else:
                nodesToCheck.extend(uncheckedChildren)
    return validPaths
