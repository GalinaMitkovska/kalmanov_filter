
import numpy as np
import matplotlib.pyplot as plt

from kalman_filter_cl import KalmanFilter
from simulations import true_positions, measurements


A = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])


H = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])


acceleration_variance = 0.15 ** 2

Q = acceleration_variance * np.array([
    [0.25, 0,    0.5, 0],
    [0,    0.25, 0,   0.5],
    [0.5,  0,    1.0, 0],
    [0,    0.5,  0,   1.0]
])

R = np.eye(2) * 1.0

P = np.eye(4) * 1.0

x = np.array([
    [0.0],
    [0.0],
    [1.0],
    [0.5]
])

kalman = KalmanFilter(A, H, Q, R, P, x)

errors = []
prediction_errors = []
kalman_positions = []

for i in range(len(measurements)):

    # 1. Предсказване
    predicted_state, _ = kalman.predict()
    predicted_position = predicted_state[:2].flatten()

    prediction_error = np.linalg.norm(
        true_positions[i] - predicted_position
    )
    prediction_errors.append(prediction_error)

    z = measurements[i].reshape(2, 1)

    corrected_state = kalman.update(z)
    estimated_position = corrected_state[:2].flatten()


    error = np.linalg.norm(
        true_positions[i] - estimated_position
    )
    errors.append(error)
    kalman_positions.append(estimated_position)

    print(f"Стъпка: {i + 1}")
    print("Истинска позиция:", true_positions[i])
    print("Измерена позиция:", z.flatten())
    print("Предсказана позиция:", predicted_position)
    print("Позиция на Калман:", estimated_position)
    print("Грешка на предсказването:", round(prediction_error, 3))
    print("Грешка след корекцията:", round(error, 3))
    print()


average_prediction_error = np.mean(prediction_errors)
average_error = np.mean(errors)

print("Средна грешка на предсказването:",
      round(average_prediction_error, 3))
print("Средна грешка след корекцията:",
      round(average_error, 3))


tolerance = 1.0

successful_predictions = sum(
    error <= tolerance for error in prediction_errors
)
successful_estimates = sum(
    error <= tolerance for error in errors
)

prediction_success_rate = (
    successful_predictions / len(prediction_errors)
) * 100

estimate_success_rate = (
    successful_estimates / len(errors)
) * 100

print("\nПраг за успех:", tolerance)
print("Успешни предсказвания:", successful_predictions)
print("Общ брой предсказвания:", len(prediction_errors))
print("Успеваемост на предсказванията:",
      round(prediction_success_rate, 1), "%")

print("\nУспешни оценки след корекция:", successful_estimates)
print("Общ брой оценки:", len(errors))
print("Успеваемост след корекция:",
      round(estimate_success_rate, 1), "%")


true_pos_np = np.array(true_positions)
measured_pos_np = np.array(measurements)
kalman_pos_np = np.array(kalman_positions)


plt.figure(figsize=(10, 8))

plt.plot(
    true_pos_np[:, 0],
    true_pos_np[:, 1],
    label="Истинска позиция",
    color="black",
    linestyle="--",
    linewidth=2
)

plt.scatter(
    measured_pos_np[:, 0],
    measured_pos_np[:, 1],
    label="Измерена позиция (с шум)",
    color="red",
    marker="x",
    s=30,
    alpha=0.6
)

plt.plot(
    kalman_pos_np[:, 0],
    kalman_pos_np[:, 1],
    label="Оценена позиция с Калман",
    color="blue",
    linewidth=1.5
)

plt.xlabel("X позиция")
plt.ylabel("Y позиция")
plt.title("Сравнение на истинската, измерената и оценената траектория")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


