import unittest

from directed_graph import DirectedGraph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_edge("Ivo", "Hrisi")
        self.graph.add_edge("Pesho", "Ivo")
        self.graph.add_edge("Pesho", 'a')
        self.graph.add_edge("Niki", "Georgi")

    def test_addEdge(self):
        self.assertIn(("Niki", "Georgi"), self.graph.edges)
        self.assertIn("Niki", self.graph.nodes)
        self.assertIn("Georgi", self.graph.nodes)

    def test_get_neighbours(self):
        self.assertIn("a", self.graph.get_neighbors_for("Pesho"))
        self.assertIn("Ivo", self.graph.get_neighbors_for("Pesho"))
        self.assertIn("Hrisi", self.graph.get_neighbors_for('Ivo'))

    def test_path_between(self):
        self.assertTrue(self.graph.path_between("Ivo", "Hrisi"))
        self.assertFalse(self.graph.path_between("Hrisi", "Ivo"))
        self.assertTrue(self.graph.path_between("Niki", "Georgi"))
        self.assertTrue(self.graph.path_between("Pesho", "Hrisi"))

    @unittest.skip("Just testing print")
    def test_print(self):
        print(self.graph)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
