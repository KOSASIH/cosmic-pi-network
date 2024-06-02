//! Spike-Timing-Dependent Plasticity (STDP) Module

use neural_network::NeuralNetwork;
use rand::Rng;

/// STDP
pub struct STDP {
    learning_rate: f64,
    time_constant: f64,
}

impl STDP {
    /// Create a new instance of STDP
    pub fn new() -> Self {
        STDP {
            learning_rate: 0.01,
            time_constant: 20.0,
        }
    }

    /// Train the neural network using STDP
    pub fn train(&self, neural_network: &mut NeuralNetwork, inputs: &Vec<f64>, targets: &Vec<f64>) {
        let mut rng = rand::thread_rng();
        for (input, target) in inputs.iter().zip(targets.iter()) {
            let pre_synaptic_spike = rng.gen::<f64>();
            let post_synaptic_spike = rng.gen::<f64>();
            let weight_change = self.learning_rate * (post_synaptic_spike - pre_synaptic_spike).exp() / self.time_constant;
            neural_network.weights += weight_change * input * target;
        }
    }
}
