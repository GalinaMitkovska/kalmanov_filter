import numpy as np

np.random.seed(42)

steps = 10

true_positions = []

position = np.array([0.0, 0.0])
velocity = np.array([1.0, 0.5])

for _ in range(steps):
    position = position + velocity
    true_positions.append(position.copy())

true_positions = np.array(true_positions)

measurements = true_positions + np.random.normal(
    0, 1, size=(steps, 2)
)

print("Истински позиции:")
print(true_positions)

print("Измерени позиции:")
print(measurements)