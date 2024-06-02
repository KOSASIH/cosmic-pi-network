#include "AGIAgent.h"
#include "KnowledgeGraph.h"
#include "Reasoner.h"
#include "NLPInterface.h"

AGIAgent::AGIAgent(KnowledgeGraph* knowledge_graph, Reasoner* reasoner, NLPInterface* nlp_interface) {
    this->knowledge_graph = knowledge_graph;
    this->reasoner = reasoner;
    this->nlp_interface = nlp_interface;
    this->state = new double[100];  // Initialize agent state
    for (int i = 0; i < 100; i++) {
        this->state[i] = rand() / (double) RAND_MAX;
    }
}

void AGIAgent::perceive(const char* input_data) {
    nlp_interface->process_input(input_data);
    knowledge_graph->update(nlp_interface->get_entities());
    reasoner->reason(knowledge_graph);
}

const char* AGIAgent::act() {
    return reasoner->get_action();
}

void AGIAgent::learn(const char* feedback) {
    reasoner->learn(feedback);
    knowledge_graph->update(reasoner->get_new_knowledge());
}

AGIAgent::~AGIAgent() {
    delete[] state;
}
