import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class ModelUtils:
    def __init__(self):
        pass

    def create_model(self, input_shape, num_classes):
        model = Sequential()
        model.add(Dense(64, activation='relu', input_shape=input_shape))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, model, X_train, y_train, epochs=10):
        model.fit(X_train, y_train, epochs=epochs, batch_size=32, verbose=1)

    def evaluate_model(self, model, X_test, y_test):
        loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
        return loss, accuracy

    def save_model(self, model, file_path):
        model.save(file_path)

    def load_model(self, file_path):
        return tf.keras.models.load_model(file_path)

# Example usage
model_utils = ModelUtils()
model = model_utils.create_model((10,), 2)
model_utils.train_model(model, X_train, y_train)
loss, accuracy = model_utils.evaluate_model(model, X_test, y_test)
print("Loss:", loss, "Accuracy:", accuracy)
model_utils.save_model(model, "model.h5")
loaded_model = model_utils.load_model("model.h5")
