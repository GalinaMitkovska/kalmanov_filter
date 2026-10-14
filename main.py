import numpy as np
from kalman_filter_cl import KalmanFilter
from simulations import true_positions, measurements
import matplotlib.pyplot as plt


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

Q = np.eye(4) * 0.1
R = np.eye(2) * 0.5
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

    predicted_state, _ = kalman.predict()
    predicted_position = predicted_state[:2].flatten()
    prediction_error = np.linalg.norm(
        true_positions[i] - predicted_position
    )
    prediction_errors.append(prediction_error)

    print("Грешка на предвиждането:", round(prediction_error, 3))

    z = measurements[i].reshape(2, 1)

    corrected_state = kalman.update(z)

    estimated_position = corrected_state[:2].flatten()
    error = np.linalg.norm(true_positions[i] - estimated_position)
    errors.append(error)

    kalman_positions.append(estimated_position)

    print("Грешка:", round(error, 3))

    print("Стъпка:", i + 1)
    print("Истинска позиция:", true_positions[i])
    print("Измерена позиция:", z.flatten())
    print("Позиция на Калман:", corrected_state[:2].flatten())
    print()

average_error = np.mean(errors)
print("Средна грешка:", round(average_error, 3))

tolerance = 1.0

successful_predictions = sum(
    error <= tolerance for error in prediction_errors
)

success_rate = (
    successful_predictions / len(prediction_errors)
) * 100

print("Успешни предвиждания:", successful_predictions)
print("Общ брой предвиждания:", len(prediction_errors))
print("Успеваемост:", round(success_rate, 1), "%")


# Преобразуване на данните за графиката
true_pos_np = np.array(true_positions)
measured_pos_np = np.array(measurements)
kalman_pos_np = np.array(kalman_positions)

# Генериране на визуализацията
plt.figure(figsize=(10, 8))
plt.plot(true_pos_np[:, 0], true_pos_np[:, 1], label="Истинска позиция", color="black", linestyle="--", linewidth=2)
plt.scatter(measured_pos_np[:, 0], measured_pos_np[:, 1], label="Измерена позиция (с шум)", color="red", marker="x", s=30, alpha=0.6)
plt.plot(kalman_pos_np[:, 0], kalman_pos_np[:, 1], label="Позиция на Калман", color="blue", linewidth=1.5)

plt.xlabel("X позиция")
plt.ylabel("Y позиция")
plt.title("Сравнение на траекториите (Калибриране с Калманов филтър)")
plt.legend()
plt.grid(True)
plt.show()

