# we can implement a graph with a dictionary 
# the keys stand for nodes

testGraph = {'0': ['3', '5', '9'],
             '1': ['6', '7', '4'],
             '2': ['10', '5'],
             '3': ['0'],
             '4': ['1', '5', '8'],
             '5': ['2', '0', '4'],
             '6': ['1'],
             '7': ['1'],
             '8': ['4'],
             '9': ['0'],
             '10': ['2']
             }

# function for implementing Breath First Search
def bfs(graph, startNode):
    visitedNodes = []
    # I implement my queue with list but there are better ways
    queue = [startNode]


    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)


    return visitedNodes

# implement shortest path algorithm for Breadth First Search
def bfsShortestPath(graph, startNode, endNode):
    visitedNodes = []
    queue = [startNode]
    parentNodes = {}

    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)
                parentNodes[neighbor] = currentNode

    print(bfsShortestPath(parentNodes, startNode, endNode))



def shortestPath(parentNode, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = parentNode[currentNode]
        path.append(currentNode)
    path.reverse()
    return path


result = bfsShortestPath(testGraph, '0', '1')

print(result)