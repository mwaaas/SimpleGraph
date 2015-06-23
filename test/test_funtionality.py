from unittest import TestCase
from graph import Graph, MissingNodeException

class TestGraphFunctionality(TestCase):

    def test_creation_of_graph(self):
        """
        testing that this graph can be created successfully

                   A
                 /  \   \
               'B'  'C' 'D'
               / \       |
             'E' 'J'    'M'
                       /   \
                      'N'  'O'
        Its dictinary representation should be :
            {'A':['B', 'C', 'D'], 'B': ['E', 'J'], 'D': ['M'], 'M':['N', 'O']}
        :return:
        """

        # initialise graph with the root node
        graph = Graph()
        graph.add_node('', 'A')
        graph.add_node('A', 'B')

        # adding node with parent that does not exist in the graph
        self.assertRaises(MissingNodeException, graph.add_node, 'c', 'b')

        # continue adding children for A
        graph.add_node('A', 'C')
        graph.add_node('A', 'D')

        # add children node for B
        graph.add_node('B', 'E')
        graph.add_node('B', 'J')

        # add child node for D
        graph.add_node('D', 'M')

        # add children node for M
        graph.add_node('M', 'N')
        graph.add_node('M', 'O')

        self.assertEqual(graph.to_dict(),
                         {'A': ['B', 'C', 'D'], 'B': ['E', 'J'], 'D': ['M'], 'M': ['N', 'O']})

        # test graph can be created with initial node
        graph2 = Graph('A')
        graph2.add_node('A', 'B')
        graph2.add_node('A', 'C')

        self.assertEqual(graph2.to_dict(), {'A': ['B', 'C']})

        # test adding node whose parent does not exist
        graph2.add_node('D', 'A')