"""
Docstring for lab 7 ex 1
"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    graphs = []
    with open(file_name) as file:
        for line in file:
            line = line.strip().split(",")
            lineage = []
            for variab in line:
                lineage.append(int(variab))
            graphs.append(lineage)
    return graphs


def to_edge_dict(edge_list):
    r"""
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]]) #doctest: +ELLIPSIS
    {1: [2, 5]...
    """
    edge_dict = {}
    for graph in edge_list:
        for edge in range(len(graph)):
            if (edge_dict.get(graph[edge])) is None:
                edge_dict[graph[edge]] = [graph[1 - edge]]
            else:
                edge_dict.get(graph[edge]).append(graph[1 - edge])
    return edge_dict
print(to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]]))

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    try:
        if edge[1] in graph[edge[0]]:
            return True
        else:
            return False
    except KeyError:
        return False


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    try:
        first = graph[edge[0]]
        first.append(edge[1])
    except KeyError:
        graph[edge[0]] = [edge[1]]
    try:
        second = graph[edge[1]]
        second.append(edge[0])
    except KeyError:
        graph[edge[1]] = [edge[0]]
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    try:
        graph[edge[0]].remove(edge[1])
    except (ValueError, KeyError):
        pass
    try:
        graph[edge[1]].remove(edge[0])
    except (ValueError, KeyError):
        pass
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node in (elem for elem in graph):
        pass
    else:
        graph[node] = []

    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    for variable in [x for x in graph]:
        try:
            del graph[node]
        except (ValueError, KeyError):
            pass
        try:
            graph[variable].remove(node)
        except (ValueError, KeyError):
            pass
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    graphs = []
    for element in [x for x in graph]:
        for doubleelement in graph[element]:
            if doubleelement < element:
                pass
            else:
                graphs.append((element, doubleelement))
    with open("File.dot", "w") as file:
        file.write("graph {\n")
        for graphic in graphs:
            file.write(str(graphic[0]) + " -- " + str(graphic[1]) + ";\n")
        file.write("}")
