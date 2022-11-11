from pathlib import Path

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


def check_graph_for_cycles(data_file) -> tuple[Graph, list]:
    """ Read a graph from file and check it for cycles.
    :return: A pair of graph and a list of vertexes that draw up a cycle
    """
    current_path = []
    visited_vertexes = set()

    def cycle_dfs(g: Graph, vertex) -> bool:
        """ Depth-first search for a cycle in the graph starting from the given vertex
        :param g: a set of key-values pairs like {vertex: list_of_neighbour_vertexes}
        :param vertex: a vertex to start from
        :return: True if any cycle is found else False
        """
        if vertex in visited_vertexes:
            return False

        visited_vertexes.add(vertex)
        current_path.append(vertex)
        for neighbour in g.neighbours(vertex):
            if neighbour in current_path:
                return True
            if cycle_dfs(g, neighbour):
                return True

        current_path.remove(vertex)
        return False

    #
    # Check if the graph has any cycle
    #
    graph = Graph()
    graph.read(file_name=data_file)
    for v in graph:
        if cycle_dfs(graph, v):
            return graph, current_path
    return graph, []


if __name__ == '__main__':

    graph_, cycle = check_graph_for_cycles(data_file=DATA_FILE)
    print(f'{graph_=}')
    if cycle:
        print(f'The Graph has a Cycle: {cycle}')
    else:
        print(f'The Graph has no Cycles')
