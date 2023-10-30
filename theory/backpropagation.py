# implementation of the backpropagation algorithm from scratch

import random


# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + (1.0**-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Initialize parameters
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.1
epochs = 10000

# Initialize weights and biases with small random values
weights_input_hidden = [
    [random.uniform(0, 0.5) for _ in range(hidden_size)] for _ in range(input_size)
]
weights_hidden_output = [random.uniform(0, 0.5) for _ in range(hidden_size)]
bias_hidden = [0.1] * hidden_size
bias_output = 0.1

# Training data and labels
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

# Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = [
        [
            sum(a * b for a, b in zip(X_row, w_col))
            for w_col in zip(*weights_input_hidden)
        ]
        for X_row in X
    ]
    hidden_layer_output = [[sigmoid(x) for x in row] for row in hidden_layer_input]
    output_layer_input = [
        sum(a * b for a, b in zip(hidden_row, weights_hidden_output)) + bias_output
        for hidden_row in hidden_layer_output
    ]
    output_layer_output = [sigmoid(x) for x in output_layer_input]

    # Compute loss (Mean Squared Error)
    loss = sum((a - b) ** 2 for a, b in zip(y, output_layer_output)) / len(y)

    # Backward pass
    # Calculate the gradients
    d_loss_d_output = [(2 * (a - b)) for a, b in zip(output_layer_output, y)]
    d_output_d_input = [sigmoid_derivative(x) for x in output_layer_output]

    # Gradients for weights_hidden_output
    gradients_hidden_output = [
        d_loss * d_output for d_loss, d_output in zip(d_loss_d_output, d_output_d_input)
    ]

    # Update weights_hidden_output and bias_output
    for i in range(len(weights_hidden_output)):
        for j in range(len(hidden_layer_output)):
            weights_hidden_output[i] -= (
                learning_rate * gradients_hidden_output[j] * hidden_layer_output[j][i]
            )
    bias_output -= (
        learning_rate * sum(gradients_hidden_output) / len(gradients_hidden_output)
    )

print("Final weights and biases:", weights_hidden_output, bias_output)
