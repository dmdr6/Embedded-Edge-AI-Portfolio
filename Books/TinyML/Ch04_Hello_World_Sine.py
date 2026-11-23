"""
TinyML Chapter 4: "Hello World" Sine Wave Model Pipeline
Trains, evaluates, quantizes, and exports a sine-wave neural network to a C byte array.
"""

# 1. Imports
import math
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras import layers

try:
    from ai_edge_litert.interpreter import Interpreter as LiteInterpreter
except ImportError:
    LiteInterpreter = tf.lite.Interpreter

# 2. Generate Data (Sine Wave)

# Number of sample datapoints to generate
SAMPLES = 100

# Fixed seed so random numbers are reproducible across runs
SEED = 1337
np.random.seed(SEED)
tf.random.set_seed(SEED)
keras.utils.set_random_seed(SEED)

# Generate uniformly distributed x values over one full sine wave [0, 2*pi]
x_values = np.random.uniform(low=0.0, high=2 * math.pi, size=SAMPLES).astype(np.float32)

# Shuffle x values so samples are not ordered sequentially
np.random.shuffle(x_values)

# Compute the true sine values and add small Gaussian noise
y_values = np.sin(x_values).astype(np.float32)
y_values += (0.1 * np.random.randn(*y_values.shape)).astype(np.float32)

# Plot the noisy sine wave dataset
plt.figure("Section2 : Noisy Sine Data")
plt.plot(x_values, y_values, "b.", label="Noisy sine")
plt.title("Generated Sine Data with Noise")
plt.xlabel("x (radians)")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show(block=False)
plt.pause(0.5)

# 3. Splitting Data (60% train, 20% validation, 20% test)

# Compute split indices for 60% train, 20% validation, and 20% test
train_split = int(0.6 * SAMPLES)
test_split = int(0.2 * SAMPLES + train_split)

# Split inputs and targets into three disjoint subsets
x_train, x_validate, x_test = np.split(x_values, [train_split, test_split])
y_train, y_validate, y_test = np.split(y_values, [train_split, test_split])

# Verify no samples were lost or duplicated during splitting
assert (x_train.size + x_validate.size + x_test.size) == SAMPLES

# Plot each subset in a different color to inspect coverage
plt.figure("Train / Val / Test Split")
plt.plot(x_train, y_train, "b.", label="Train (60%)")
plt.plot(x_validate, y_validate, "y.", label="Validate (20%)")
plt.plot(x_test, y_test, "r.", label="Test (20%)")
plt.title("Dataset Partitioning")
plt.xlabel("x (radians)")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show(block=False)
plt.pause(0.5)

# 4. Defining & Training Model 1

# Build a sequential stack: 1D input -> 16 ReLU neurons -> 1 linear output
model_1 = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),    # Linear output for regression
])

# Configure optimizer, MSE loss function, and MAE evaluation metric
model_1.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])

# Print layer shapes and parameter counts (49 total parameters)
model_1.summary()

# Train Model 1 on the training set while tracking validation metrics
history_1 = model_1.fit(
    x_train,
    y_train,
    epochs=1000,
    batch_size=16,
    validation_data=(x_validate, y_validate),
    verbose=0
)

# Print final training and validation metrics after all epochs
print(
    f"Model 1 final -> loss: {history_1.history['loss'][-1]:.4f}, "
    f"mae: {history_1.history['mae'][-1]:.4f}, "
    f"val_loss: {history_1.history['val_loss'][-1]:.4f}, "
    f"val_mae: {history_1.history['val_mae'][-1]:.4f}"
)
