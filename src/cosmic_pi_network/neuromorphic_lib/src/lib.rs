//! Neuromorphic Library

pub mod neural_network;
pub mod stdp;

use neural_network::NeuralNetwork;
use stdp::STDP;

/// Neuromorphic Library
pub struct NeuromorphicLib {
    neural_network: NeuralNetwork,
    stdp: STDP,
}

impl NeuromorphicLib {
    /// Create a new instance of the neuromorphic library
    pub fn new() -> Self {
        NeuromorphicLib {
            neural_network: NeuralNetwork::new(),
            stdp: STDP::new(),
        }
    }

    /// Train the neural network using STDP
    pub fn train(&mut self, inputs: &Vec<f64>, targets: &Vec<f64>) {
        self.stdp.train(&mut self.neural_network, inputs, targets);
    }

    /// Run the neural network
    pub fn run(&self, inputs: &Vec<f64>) -> Vec<f64> {
        self.neural_network.run(inputs)
    }
}
