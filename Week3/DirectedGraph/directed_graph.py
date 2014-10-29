class DirectedGraph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes:
            self.nodes.append(node_a)
        if node_b not in self.nodes:
            self.nodes.append(node_b)

        if (node_a, node_b) not in self.edges:
            self.edges.append((node_a, node_b))

    def get_neighbors_for(self, node):
        return [neighbour[1] for neighbour
                in self.edges if node == neighbour[0]]

    def path_between(self, node_a, node_b):
        flag = True
        looked_at = []
        connected_to_a = self.get_neighbors_for(node_a)
        while flag:
            flag = False
            for a in connected_to_a:
                if a not in looked_at:
                    connected_to_a += self.get_neighbors_for(a)
                    looked_at.append(a)
                    flag = True
        return node_b in connected_to_a

    def __str__(self):
        people = "People = {"
        for person in self.nodes:
            people += "{}, ".format(person)
        people = people[:-2]
        people += "}\n"

        edgess = "Edges = {"
        for edge in self.edges:
            edgess += "{}, ".format(edge)
        edgess = edgess[:-2]
        edgess += "}\n"

        return people + edgess
