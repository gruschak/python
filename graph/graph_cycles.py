from enum import Enum
from pathlib import Path
from typing import Any

DATA_FILE = Path.home() / 'tmp/input.txt'


class Graph(dict):
    """ """
    def __init__(self):
        super().__init__()

    def neighbours(self, vertex) -> list:
        return self.get(vertex) or []

    def read(self, file_name):
        with open(file_name) as f:
            total_edges = int(f.readline())
            for _ in range(total_edges):
                a, b = f.readline().strip().split()
                if self.get(a):
                    self[a].append(b)
                else:
                    self[a] = [b]

    def vertexes(self) -> set:
        all_vertexes = set()
        for k, v in self.items():
            all_vertexes |= {k} | set(v)
        return all_vertexes


class StateColour(Enum):
    WHITE = 'Not visited yet'
    GRAY = 'Currently in process'
    BLACK = 'Finished (visited Ok)'


def check_graph_for_cycles(data_file) -> tuple[Graph, bool]:

    color: dict[Any, StateColour] = {}

    def paint_all_vertexes(g: Graph):
        """ """
        for vertex in g.vertexes():
            color[vertex] = StateColour.WHITE

    def cycle_dfs(g: Graph, initial_vertex: int = None) -> bool:
        """ Depth-first search for a cycle in the graph starting from the given vertex
        :param g: a set of key-values pairs like {vertex: list_of_neighbour_vertexes}
        :param initial_vertex: a vertex to start from
        :return: True if any cycle is found else False
        """
        color[initial_vertex] = StateColour.GRAY

        for neighbour in (g.vertexes() if initial_vertex is None else g.neighbours(initial_vertex)):
            if color[neighbour] is StateColour.GRAY:
                return True
            if (color[neighbour] is StateColour.WHITE) and cycle_dfs(g, neighbour):
                return True

        color[initial_vertex] = StateColour.BLACK
        return False

    #
    # Check if the graph has any cycle
    #
    graph = Graph()
    graph.read(file_name=data_file)
    paint_all_vertexes(graph)
    return graph, cycle_dfs(graph)


if __name__ == '__main__':

    graph_, has_cycle = check_graph_for_cycles(data_file=DATA_FILE)
    print(f'{graph_=}')
    if has_cycle:
        print("The Graph has a Cycle")
    else:
        print("The Graph has no Cycles")
