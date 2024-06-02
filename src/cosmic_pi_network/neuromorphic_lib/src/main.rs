//! Main Function

use neuromorphic_lib::NeuromorphicLib;

fn main() {
    let mut lib = NeuromorphicLib::new();
    let inputs = vec![1.0, 2.0, 3.0];
    let targets = vec![4.0, 5.0, 6.0];
    lib.train(&inputs, &targets);
    let outputs = lib.run(&inputs);
    println!("Outputs: {:?}", outputs);
}
