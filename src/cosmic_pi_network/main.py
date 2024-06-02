from cosmic_pi_network.api import API
from cosmic_pi_network.computer_vision import ComputerVision
from cosmic_pi_network.data_preprocessing import DataPreprocessing
from cosmic_pi_network.neural_network import NeuralNetwork
from cosmic_pi_network.nlp import NLP

def main():
    api = API()
    weather_data = api.get_weather("New York")
    print("Weather data:", weather_data)

    nlp = NLP()
    text = "This is a sample text."
    tokens = nlp.tokenize_text(text)
    filtered_tokens = nlp.remove_stopwords(tokens)
    lemmatized_tokens = nlp.lemmatize_tokens(filtered_tokens)
    sentiment = nlp.sentiment_analysis(text)
    print("Sentiment:", sentiment)

    computer_vision = ComputerVision()
    image = computer_vision.load_image("image.jpg")
    grayscale_image = computer_vision.convert_to_grayscale(image)
    thresh_image = computer_vision.apply_threshold(grayscale_image)
    edges_image = computer_vision.detect_edges(grayscale_image)
    faces = computer_vision.detect_faces(grayscale_image)
    print("Number offaces detected:", len(faces))

    data_preprocessing = DataPreprocessing()
    data = data_preprocessing.load_data("data.csv")
    X_train, X_test, y_train, y_test = data_preprocessing.split_data(data)
    X_train_scaled, X_test_scaled = data_preprocessing.scale_data(X_train, X_test)

    neural_network = NeuralNetwork()
    model = neural_network.create_model((28, 28, 1), 10)
    neural_network.train_model(model, X_train_scaled, y_train)
    loss, accuracy = neural_network.evaluate_model(model, X_test_scaled, y_test)
    print("Loss:", loss, "Accuracy:", accuracy)

if __name__ == "__main__":
    main()
