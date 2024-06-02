#include "NLPInterface.h"
#include <spacy/spacy.h>

NLPInterface::NLPInterface() {
    this->nlp = new spacy::Language("en_core_web_sm");
}

void NLPInterface::process_input(const char* input_data) {
    spacy::Doc doc = nlp->process(input_data);
    int num_entities = doc.ents.size();
    this->entities = new char*[num_entities];
    for (int i = 0; i < num_entities; i++) {
        entities[i] = doc.ents[i].text.c_str();
    }
}

const char** NLPInterface::get_entities() {
    return entities;
}

NLPInterface::~NLPInterface() {
    delete nlp;
    delete[] entities;
}
