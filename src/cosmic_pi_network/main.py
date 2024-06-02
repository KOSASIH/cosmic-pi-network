from cosmic_pi_network.cosmic_network import CosmicPiNetwork
from cosmic_pi_network.data_processing import clean_data, preprocess_data
from cosmic_pi_network.data_analysis import analyze_data
from cosmic_pi_network.models import train_model, evaluate_model
from cosmic_pi_network.visualization import plot_results
from cosmic_pi_network.config import COSMIC_PI_IP, COSMIC_PI_PORT

# Initialize the network object
network = CosmicPiNetwork(ip=COSMIC_PI_IP, port=COSMIC_PI_PORT)

# Connect to the network
network.connect()

# Receive raw data from the network
raw_data = network.receive_data()

# Clean and preprocess the data
cleaned_data = clean_data(raw_data)
preprocessed_data = preprocess_data(cleaned_data)

# Analyze the data
analysis_results = analyze_data(preprocessed_data)

# Train and evaluate the model
model = train_model(analysis_results)
model_accuracy = evaluate_model(model, analysis_results)

# Visualize the results
plot_results(analysis_results)

# Disconnect from the network
network.disconnect()
