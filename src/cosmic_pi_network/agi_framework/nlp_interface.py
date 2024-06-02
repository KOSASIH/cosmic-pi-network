import spacy

class NLPInterface:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_input(self, input_data):
        doc = self.nlp(input_data)
        self.entities = [ent.text for ent in doc.ents]

    def get_entities(self):
        return self.entities

    def __str__(self):
        return f"NLPInterface(entities={self.entities})"

    def __repr__(self):
        return repr(self.entities)
