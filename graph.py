class LocalGraph:
    def __init__(self):
        # _graph представляет собой запись вершин и смежные между ними соединения.
        # Пример: {'A': ('B', 'C'), 'B': ('A'), 'C': ('A')}
        #   -> _graph.keys() это все вершины у данного графа.
        #   -> _graph['A'] смежные с вершиной 'A' другие вершины.
        self.__graph = {}

    @staticmethod
    def from_list_edges_and_nodes(nodes_list: list, edges_list: list):
        # Пример ввода:
        # nodes_list = ['A', 'B', 'C']
        # edges_list = [('A', 'B'), ('B', 'C')]
        gr = LocalGraph()
        for node in nodes_list:
            gr.add_node(node)
        for edge in edges_list:
            gr.add_edge(*edge)
        return gr

    @staticmethod
    def from_adjacency_matrix(nodes_list: list, adjacency_matrix: list):
        # Пример ввода:
        # nodes_list = ['A', 'B', 'C']
        # adjacency_matrix = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]
        assert len(nodes_list) != len(adjacency_matrix), "The number of nodes and the matrix do not match in size"
        gr = LocalGraph()
        for row_index in range(len(nodes_list)):
            node1 = nodes_list[row_index]
            gr.add_node(node1)
            row = adjacency_matrix[row_index]
            for index in range(len(row)):
                node2 = nodes_list[index]
                if row[index] and not gr.is_edge_exists(node1, node2):
                    gr.add_edge(node1, node2)

    @staticmethod
    def from_adjacency_map(adjacency_map: dict):
        # Пример ввода:
        # adjacency_map = {'A': ('B', 'C'), 'B': ('A', 'C'), 'C': ('A', 'B')}
        gr = LocalGraph()
        gr.__graph = adjacency_map
        return gr

    def add_node(self, node: str):
        assert node not in self.__graph.keys(), f'{node} дублируется в списке вершин'
        self.__graph[node] = ()

    def add_edge(self, node1: str, node2: str):
        assert node1 in self.__graph.keys(), f'{node1} не в списке вершин'
        assert node2 in self.__graph.keys(), f'{node2} не в списке вершин'
        self.__graph[node1] = (*self.__graph[node1], node2)
        self.__graph[node2] = (*self.__graph[node2], node1)

    def is_edge_exists(self, node1: str, node2: str) -> bool:
        assert node1 in self.__graph.keys(), f'{node1} не в списке вершин'
        assert node2 in self.__graph.keys(), f'{node2} не в списке вершин'
        return node2 in self.__graph[node1] and node1 in self.__graph[node2]

    def to_adjacency_map(self):
        # Пример вывода
        # {'A': ('B', 'C'), 'B': ('A', 'C'), 'C': ('A', 'B')}
        return self.__graph

    def to_adjacency_matrix(self):
        # Пример вывода
        # (['A', 'B', 'C'], [[0, 1, 1], [1, 0, 1], [1, 1, 0]])
        arr = []
        for node1 in self.__graph.keys():
            row = []
            for node2 in self.__graph.keys():
                row.append(1 if node1 in self.__graph[node2] else 0)
            arr.append(row)
        return list(self.__graph.keys()), arr

    def to_list_edges_and_nodes(self):
        # Пример вывода
        # (['A', 'B', 'C'], [('A', 'B'), ('A', 'C'), ('B', 'C')])
        list_edges = list(self.__graph.keys())
        list_nodes = []
        for node1 in self.__graph.keys():
            raw_node = self.__graph[node1]
            for node2 in raw_node:
                if not ((node1, node2,) in list_nodes or (node2, node1,) in list_nodes):
                    list_nodes.append((node1, node2,))
        return list_edges, list_nodes
