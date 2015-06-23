__author__ = 'francis'

class Graph(object):

    def __init__(self, initial_node):

        self.graph_dict = {}

        # add the first node
        self.graph_dict.update({ initial_node: {}})

    def add_node(self, parent, object, **kwargs):
        pass