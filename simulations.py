
import numpy as np

np.random.seed(42)

steps = 100

true_positions = []

position = np.array([0.0, 0.0])
velocity = np.array([1.0, 0.5])

# Стандартно отклонение на случайното ускорение
acceleration_std = 0.15

# Стандартно отклонение на шума в измерванията
measurement_std = 1.0

for _ in range(steps):
    # Случайно ускорение по X и Y
    acceleration = np.random.normal(
        0, acceleration_std, size=2
    )

    # Обновяване на позицията и скоростта
    position = position + velocity + 0.5 * acceleration
    velocity = velocity + acceleration

    true_positions.append(position.copy())

true_positions = np.array(true_positions)

# Измервания с допълнителен шум
measurements = true_positions + np.random.normal(
    0, measurement_std, size=(steps, 2)
)

print("Истински позиции:")
print(true_positions)

print("Измерени позиции:")
print(measurements)
