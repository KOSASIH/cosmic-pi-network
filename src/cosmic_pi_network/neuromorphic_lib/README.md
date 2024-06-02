# Neuromorphic Library
================. 
================. 
=====================
# Rust Convolutional Neural Network from Scratch

This repository contains a Rust implementation of a Convolutional Neural Network (CNN) built from scratch. This repository provides code for training on the MNIST dataset, and the 50States10K dataset.

All machine learning code is written from scratch, however the `ndarray` crate is used for matrix operations. When tuned correctly, the network should reach 90+% accuracy within one minute on the MNIST dataset.

## Overview

The repository implements the following features:

- Convolutional, max pooling, and fully connected layers
- ReLU and Softmax activation functions
- Cross-entropy loss function
- SGD, Momentum, RMSProp, and Adam optimizers
- Dropout
- He initialization

## Installation

To use this CNN implementation, you must have Rust and Cargo installed on your machine. After installing Rust and Cargo, you can clone this repository to your local machine and build the project with the following command:

```
1. $ cargo build --release
```


## Usage

To run the demo of the CNN, place the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) in a folder named `data`, and use the following command:

```
1. $ cargo run --release
```


This command will run a demo of the CNN and train it on the MNIST dataset.

## Further Reading

For more information about this project, read [my blog post on CNNs](https://charliegoldstraw.com/articles/cnn/).

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the `LICENSE` file for details.

# rust-neural-net

A simple Neural Network implementation in Rust, made to learn the basics of machine learning from scratch.

Learning resources:

- [Quick intro] by ujjwalkarn (concepts)
- Mind: [How to build a Neural Network] by Steven Miller (Javascript)
- [Artificial Neural Networks Series] by Rubik's Code (C#)
- Neural Networks Demystified by the [Welch Labs] Youtube channel ([supporting Github] in iPython/Jupyter)

[Quick intro]: https://ujjwalkarn.me/2016/08/09/quick-intro-neural-networks/
[How to build a Neural Network]: https://stevenmiller888.github.io/mind-how-to-build-a-neural-network/
[Artificial Neural Networks Series]: https://rubikscode.net/2018/02/19/artificial-neural-networks-series/
[Welch Labs]: https://www.youtube.com/watch?v=bxe2T-V8XRs&list=PLiaHhY2iBX9hdHaRr6b7XevZtgZRa1PoU
[supporting Github]: https://github.com/stephencwelch/Neural-Networks-Demystified
Sign up
Sign in
Sign up
Sign in
Member-only story
Ashish Sharda
Follow
--
Share
Welcome back to our series on building a neural network in Rust! In Part 1, we discussed the basics of neural networks and set up our Rust environment. Now, it’s time to dive deeper and build the foundational components of our neural network: neurons, layers, and activation functions. By the end of this part, you’ll have a solid understanding of these components and how they interact to form a neural network.
--
--
Help
Status
About
Careers
Press
Blog
Privacy
Terms
Text to speech
Teams

=====================
