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

    def __init__(self, identifier: str, value: object, adj_vert: dict = None):
        self.id = identifier
        self.value = value
        self.adj_list = {} if adj_vert is None else adj_vert


class GraphException(Exception):
    pass


class DirectedGraph:
    """
    Directed Graph data structure. Can support weighted or unweighted edges.

    :param weighted:        Bool indicating if edges of graph are weighted. Defaults to False.
    """

    def __init__(self, weighted=False):
        self._vertices = {}
        self._size = 0
        self._weighted = weighted

    def add_vertex(self, identifier: str, value: object) -> None:
        """
        Creates a new vertex and adds it to the graph. If a vertex with that identifier already exists in the graph,
        its value is replaced. If replacing an existing vertex value, adjacent vertices will not be changed.

        :param identifier:      String representing the unique identifier of the new vertex.
        :param value:           Value that the new vertex will hold.

        :return:                None.
        """

        # If identifier already exists in graph, replace value.
        if identifier in self._vertices:
            old_vert = self._vertices[identifier]
            self._vertices[identifier] = Vertex(identifier, value, old_vert.adj_list)
            return

        # Otherwise, add new vertex and increment size
        self._vertices[identifier] = Vertex(identifier, value)
        self._size += 1

    def remove_vertex(self, identifier: str) -> None:
        """
        Removes the vertex with the given identifier and any inbound edges.

        :param identifier:      String representing the identifier of the vertex to be removed.

        :return:                None.
        """
        # If vertex does not exist, raise exception
        if identifier not in self._vertices:
            raise GraphException

        # Remove any inbound edges
        for vertex_id in self._vertices:
            vertex = self._vertices[vertex_id]
            if identifier in vertex.adj_list:
                del vertex.adj_list[identifier]

        # Delete the vertex and decrement graph size
        del self._vertices[identifier]
        self._size -= 1

    def add_edge(self, source_id: str, dest_id: str, weight: int = None) -> None:
        """
        Creates a new edge between two vertices in the graph. If graph is weighted, weight must be supplied. If graph
        is not weighted, weight value will be ignored. If either of the vertices do not exist, raises exception. If edge
        already exists, does nothing.

        :param source_id:       String representing the identifier of the vertex where the edge begins.
        :param dest_id:         String representing the identifier of the vertex where the edge ends.
        :param weight:          Integer representing the weight of the edge. Applies to weighted graphs only.

        :return:                None.
        """
        # Raise exception if either vertex is not in the graph
        if source_id not in self._vertices or dest_id not in self._vertices:
            print("ERROR: One of the supplied vertices do not exist in the graph.")
            raise GraphException

        source_vert = self._vertices[source_id]

        # If edge does not already exist
        if dest_id not in source_vert.adj_list:
            # If graph is weighted and no weight was supplied, raise exception
            if self._weighted and not weight:
                print("ERROR: Weight must be provided for an edge in the weighted graph.")
                raise GraphException
            # Otherwise, add edge - ignore weight if graph not weighted
            source_vert.adj_list[dest_id] = weight if self._weighted else None

    def remove_edge(self, source_id: str, dest_id: str) -> None:
        """
        Removes the edge from source to destination vertices. If edge does not exist, raises exception.

        :param source_id:       String representing the identifier of the vertex where the edge begins.
        :param dest_id:         String representing the identifier of the vertex where the edge ends.

        :return:                None.
        """
        # If the edge exists, remove it
        if source_id in self._vertices:
            source_list = self._vertices[source_id].adj_list
            if dest_id in source_list:
                del source_list[dest_id]
                return
        # Otherwise, raise exception
        print("ERROR: Edge does not exist in the graph.")
        raise GraphException

    def edge_exists(self, source_id: str, dest_id: str) -> bool:
        """
        Returns True if the edge exists in the graph, False otherwise.

        :param source_id:       String representing the identifier of the vertex where the edge begins.
        :param dest_id:         String representing the identifier of the vertex where the edge ends.

        :return:                Boolean. True if edge exists, False otherwise.
        """
        # If outbound vert exists, check if inbound vert in adjacency list (y--> True n--> False)
        if source_id in self._vertices:
            source_vert = self._vertices[source_id]
            if dest_id in source_vert.adj_list:
                return True

        return False

    def vertex_exists(self, identifier: str) -> bool:
        """
        Returns True if the vertex exists in the graph, False otherwise.

        :param identifier:      String representing the identifier of the vertex we are checking for.
        :return:                Boolean. True of vertex with given identifier exists, False otherwise.
        """
        if identifier in self._vertices:
            return True

        return False

    def get_adjacent_vertices(self, identifier: str) -> list | None:
        """
        Returns a list of identifiers of the adjacent vertices for the vertex assigned to the given identifier or None
        if no adjacent vertices exist. If the vertex does not exist, raises exception.

        :param identifier:      String representing the identifier of the vertex we are getting adjacent vertices of.

        :return:                List of adjacent vertices, or None if no adjacent vertices.
        """
        if identifier not in self._vertices:
            print("ERROR: Vertex does not exist in graph.")
            raise GraphException

        adj_vertex = self._vertices[identifier].adj_list
        if len(adj_vertex) == 0:
            return

        return [key for key in adj_vertex]


graph = DirectedGraph(weighted=True)
graph.add_vertex("alpha", 5)
graph.add_vertex("beta", 4)
graph.add_edge("alpha", "beta", 10)
print(graph.edge_exists("alpha", "beta"))
print(graph.get_adjacent_vertices("alpha"))
graph.remove_edge("alpha", "beta")
print(graph.get_adjacent_vertices("alpha"))


