import numpy as np
from sklearn.tree import DecisionTreeClassifier

class AIAgent:
    def __init__(self):
        pass

    def create_decision_tree(self, X, y):
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X, y)
        return clf

    def make_prediction(self, clf, X):
        return clf.predict(X)

    def evaluate_model(self, clf, X, y):
        accuracy = clf.score(X, y)
        return accuracy

# Example usage
ai_agent = AIAgent()
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 0, 1])
clf = ai_agent.create_decision_tree(X, y)
prediction = ai_agent.make_prediction(clf, X)
print("Prediction:", prediction)
accuracy = ai_agent.evaluate_model(clf, X, y)
print("Accuracy:", accuracy)
