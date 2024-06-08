# Directed Graph Data Structure
# Jacob Mosiman
# Personal Project June 2024

class Vertex:
    """
    Object representing a vertex in a graph.

    :param identifier:      Unique identifier for the vertex. Used to store in Graph vertices dictionary.
    :param value:           Value that the vertex will hold.
    :param adj_vert:        List containing identifiers of adjacent vertices. Default to None / empty list.
    """

    def __init__(self, identifier: str, value: object, adj_vert: list = None):
        self.id = identifier
        self.value = value
        self.adj_list = [] if adj_vert is None else adj_vert


class DirectedGraph:
    """
    Directed Graph data structure. Can support weighted or unweighted edges.

    :param weighted:        Bool indicating if edges of graph are weighted. Defaults to False.
    """

    def __init__(self, weighted=False):
        self._vertices = {}
        self._size = 0
        self._weighted = weighted

    def add_vertex(self, identifier: str, value: object):
        """
        Creates a new vertex and adds it to the graph. If a vertex with that identifier already exists in the graph,
        its value is replaced. If replacing an existing vertex value, adjacent vertices will not be changed.

        :param identifier:      String representing the unique identifier of the new vertex.
        :param value:           Value that the new vertex will hold.
        """

        # If identifier already exists in graph, replace value.
        if identifier in self._vertices:
            old_vert = self._vertices[identifier]
            self._vertices[identifier] = Vertex(identifier, value, old_vert.adj_list)
            return

        # Otherwise, add new vertex and increment size
        self._vertices[identifier] = Vertex(identifier, value)
        self._size += 1

