use ndarray::prelude::*;
use rand::distributions::Uniform;
use rand::prelude::*;

pub struct DeepNeuralNetwork {
    pub layers: Vec<usize>,
    pub learning_rate: f32,
}

impl DeepNeuralNetwork {
    pub fn new(layers: Vec<usize>, learning_rate: f32) -> Self {
        Self { layers, learning_rate }
    }

    pub fn initialize_weights(&self) -> Vec<Array2<f32>> {
        let mut weights = Vec::new();
        for i in 0..self.layers.len() - 1 {
            let weight = Array2::random((self.layers[i], self.layers[i + 1]), Uniform::new(-1.0, 1.0));
            weights.push(weight);
        }
        weights
    }
}
