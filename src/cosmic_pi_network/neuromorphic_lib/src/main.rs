use neuromorphic_lib::neural_network::DeepNeuralNetwork;
use neuromorphic_lib::stdp::STDP;

fn main() {
    let neural_network = DeepNeuralNetwork::new(vec![784, 256, 10], 0.01);
    let stdp = STDP::new(0.01, 20.0);

    let mut weights = neural_network.initialize_weights();

    // Train the network
    // ...
}
