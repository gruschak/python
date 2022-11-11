from enum import Enum
from pathlib import Path
from typing import Any

DATA_FILE = Path.home() / 'projects/python/graph/graph_data.txt'


class Graph(dict):
    """ """
    def __init__(self):
        super().__init__()

    def neighbours(self, vertex) -> list:
        """ """
        return self.get(vertex) or []

    def read(self, file_name):
        """ Read a graph from the text file.
        A data in the first line must be
        a number of graph edges to read.
        The rest lines must have pairs of vertexes like
        A B - that means an arrow from A to B.
        """
        with open(file_name) as f:
            total_edges = int(f.readline())
            for _ in range(total_edges):
                a, b = f.readline().strip().split()
                if self.get(a):
                    self[a].append(b)
                else:
                    self[a] = [b]

    def vertexes(self) -> set:
        """ Return all vertexes of the graph """
        all_vertexes = set()
        for k, v in self.items():
            all_vertexes |= {k} | set(v)
        return all_vertexes


class StateColor(Enum):
    WHITE = 'Not visited yet'
    GRAY = 'Currently in process'
    BLACK = 'Finished (visited Ok)'


def check_graph_for_cycles(data_file) -> tuple[Graph, bool]:
    """ """
    color: dict[Any, StateColor] = {}

    def paint_all_vertexes(g: Graph, colour: StateColor):
        """ """
        for vertex in g.vertexes():
            color[vertex] = colour

    def cycle_dfs(g: Graph, initial_vertex=None) -> bool:
        """ Depth-first search for a cycle in the graph starting from the given vertex
        :param g: a set of key-values pairs like {vertex: list_of_neighbour_vertexes}
        :param initial_vertex: a vertex to start from
        :return: True if any cycle is found else False
        """
        color[initial_vertex] = StateColor.GRAY

        for neighbour in (g.vertexes() if initial_vertex is None else g.neighbours(initial_vertex)):

            if color[neighbour] is StateColor.GRAY:
                return True
            if (color[neighbour] is StateColor.WHITE) and cycle_dfs(g, neighbour):
                return True

        color[initial_vertex] = StateColor.BLACK
        return False

    #
    # Check if the graph has any cycle
    #
    graph = Graph()
    graph.read(file_name=data_file)
    paint_all_vertexes(graph, StateColor.WHITE)
    return graph, cycle_dfs(graph)


if __name__ == '__main__':

    graph_, has_cycle = check_graph_for_cycles(data_file=DATA_FILE)
    print(f'{graph_=}')
    if has_cycle:
        print("The Graph has a Cycle")
    else:
        print("The Graph has no Cycles")
