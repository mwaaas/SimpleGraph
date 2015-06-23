####After searching for a simple graphical data structure in python and didn't find one I decided to implement one


###### Usage
        # implementation of the graph below

                    A
                 /  \   \
               'B'  'C' 'D'
               / \       |
             'E' 'J'    'M'
                       /   \
                      'N'  'O'   
        Its dictinary representation should be :
            {'A':['B', 'C', 'D'], 'B': ['E', 'J'], 'D': ['M'], 'M':['N', 'O']}


#### Code implementation for the graph above
        from graph import Graph, MissingNodeException
        
        graph = Graph('A')
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
