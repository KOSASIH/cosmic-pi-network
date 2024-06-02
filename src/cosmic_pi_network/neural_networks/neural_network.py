import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

class NeuralNetwork:
    def __init__(self):
        pass

    def create_model(self, input_shape, num_classes):
        inputs = Input(shape=input_shape)
        x = Conv2D(32, (3, 3), activation='relu')(inputs)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(64, (3, 3), activation='relu')(x)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(128, (3, 3), activation='relu')(x)
        x = MaxPooling2D((2, 2))(x)
        x = Flatten()(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.2)(x)
        outputs = Dense(num_classes, activation='softmax')(x)
        model = Model(inputs=inputs, outputs=outputs)
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
neural_network = NeuralNetwork()
model = neural_network.create_model((28, 28, 1), 10)
neural_network.train_model(model, X_train, y_train)
loss, accuracy = neural_network.evaluate_model(model, X_test, y_test)
print("Loss:", loss, "Accuracy:", accuracy)
neural_network.save_model(model, "model.h5")
loaded_model = neural_network.load_model("model.h5")
