import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def add_entity(self, entity):
        self.graph.add_node(entity)

    def add_relation(self, entity1, entity2, relation):
        self.graph.add_edge(entity1, entity2, relation=relation)

    def update(self, new_entities):
        for entity in new_entities:
            self.add_entity(entity)

    def get_entities(self):
        return list(self.graph.nodes)

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return repr(self.graph)
