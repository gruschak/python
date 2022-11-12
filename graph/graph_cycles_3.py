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
        The rest of the lines must each be a pair of vertexes:
        string A B means an arrow from A to B.
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
        """ Return a set of all vertexes of the graph """
        all_vertexes = set()
        for k, v in self.items():
            all_vertexes |= {k} | set(v)
        return all_vertexes

    def find_cycle(self) -> [list]:
        """ Check the graph for cycles.
        :return: A list of vertexes that draw up a cycle
        """
        visited_vertexes = set()
        current_path = []

        def cycle_dfs(vertex) -> bool:
            """ Depth-first search for a cycle in the graph
            starting from the given vertex
            :param vertex: a vertex to start from
            :return: True if any cycle is found else False
            """
            if vertex in visited_vertexes:
                return False

            visited_vertexes.add(vertex)
            current_path.append(vertex)
            for neighbour in self.neighbours(vertex):
                if neighbour in current_path:
                    return True
                if cycle_dfs(neighbour):
                    return True

            current_path.pop()  # we may use also .remove(vertex)
            return False

        # Check if the graph has any cycle
        for v in self:
            if cycle_dfs(v):
                return current_path
        return []


if __name__ == '__main__':

    graph = Graph()
    graph.read(file_name=DATA_FILE)
    cycle = graph.find_cycle()

    print(f'{graph=}')
    if cycle:
        print(f'The Graph has a Cycle: ({" -> ".join(cycle)})')
    else:
        print(f'The Graph has no Cycles')
