# visualizations and code for universal approximation in python

# Import additional libraries for better plotting
from matplotlib.ticker import MaxNLocator
import numpy as np
from torch import sigmoid
import matplotlib as plt


# Define a simple function to approximate (sine function)
def target_function(x):
    return np.sin(x)


# Neural network approximation function
def neural_approximation(x, num_neurons):
    np.random.seed(0)  # for reproducibility
    # initialize weights randomly for each neuron
    weights = np.random.randn(num_neurons)
    # initialize biases randomly for each neuron
    biases = np.random.randn(num_neurons)
    # initialize approximation as an array of zeros with the same shape as x
    approx = np.zeros_like(x)

    for i in range(num_neurons):
        approx += weights[i] * sigmoid(x + biases[i])

    return approx / num_neurons


# Generate x values
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y_true = target_function(x_vals)

# Create the plots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 1. Layer-by-Layer Approximation
for neurons in [1, 5, 20]:
    y_approx = neural_approximation(x_vals, neurons)
    axs[0].plot(x_vals, y_approx, label=f"{neurons} Neurons")

axs[0].plot(x_vals, y_true, label="True Function", linestyle="--")
axs[0].set_title("Layer-by-Layer Approximation")
axs[0].legend()
axs[0].grid(True)

# 2. Error Plot
errors = []
neurons_range = list(range(1, 21))
for neurons in neurons_range:
    y_approx = neural_approximation(x_vals, neurons)
    error = np.mean(np.abs(y_true - y_approx))
    errors.append(error)

axs[1].plot(neurons_range, errors, marker="o")
axs[1].set_title("Error vs Number of Neurons")
axs[1].set_xlabel("Number of Neurons")
axs[1].set_ylabel("Mean Absolute Error")
axs[1].xaxis.set_major_locator(MaxNLocator(integer=True))
axs[1].grid(True)

# 3. Multiple Functions
y_exp = np.exp(-0.1 * x_vals)
y_poly = 0.01 * x_vals**2

axs[2].plot(x_vals, neural_approximation(x_vals, 20), label="Approximation")
axs[2].plot(x_vals, y_exp, label="Exp Function", linestyle="--")
axs[2].plot(x_vals, y_poly, label="Poly Function", linestyle="--")
axs[2].set_title("Approximating Different Functions")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
