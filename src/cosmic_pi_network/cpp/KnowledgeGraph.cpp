#include "KnowledgeGraph.h"
#include <networkx/networkx.h>

KnowledgeGraph::KnowledgeGraph() {
    this->graph = new nx::MultiDiGraph();
}

void KnowledgeGraph::add_entity(const char* entity) {
    graph->add_node(entity);
}

void KnowledgeGraph::add_relation(const char* entity1, const char* entity2, const char* relation) {
    graph->add_edge(entity1, entity2, relation);
}

void KnowledgeGraph::update(const char** new_entities) {
    for (int i = 0; new_entities[i]!= nullptr; i++) {
        add_entity(new_entities[i]);
    }
}

const char** KnowledgeGraph::get_entities() {
    int num_entities = graph->number_of_nodes();
    char** entities = new char*[num_entities];
    int i = 0;
    for (auto node : graph->nodes()) {
        entities[i++] = node.first.c_str();
    }
    return entities;
}

KnowledgeGraph::~KnowledgeGraph() {
    delete graph;
}
