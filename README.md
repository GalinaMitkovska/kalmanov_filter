# 2D Kalman Filter in Python

## Description

This project implements a two-dimensional Kalman Filter using Python and NumPy.

It simulates the movement of an object in two dimensions, including random acceleration. Noisy GPS-like measurements are generated to simulate sensor inaccuracies. The Kalman Filter predicts the object's state and corrects its estimate using the measurements.

The project compares the true positions, noisy measurements, and estimated positions to evaluate the performance of the filter.

## Features

- Simulates object movement in two dimensions over 100 steps.
- Includes random acceleration to vary the object's velocity.
- Generates noisy position measurements using a normal distribution.
- Predicts the object's position and velocity.
- Corrects predictions using noisy measurements.
- Calculates prediction errors and errors after correction.
- Calculates average errors and success rates using a specified error tolerance.
- Visualizes the true, measured, and estimated trajectories in a graph.

## Technologies

- Python
- NumPy
- Matplotlib
- uv for dependency and project environment management

## Project Structure

- `main.py` — runs the Kalman Filter, calculates errors and success rates, and displays the trajectory graph.
- `kalman_filter_cl.py` — contains the Kalman Filter class and its prediction and update methods.
- `simulations.py` — simulates object movement with random acceleration and generates noisy measurements.
- `pyproject.toml` — contains project configuration and dependencies.
- `uv.lock` — records the resolved dependency versions.
- `.python-version` — specifies the Python version for the project.

## How It Works

The Kalman Filter follows two main steps:

1. **Prediction:** Estimates the next state of the object using the motion model.
2. **Update:** Uses the new measurement to correct the predicted state.

The state contains four values:

- `x` — horizontal position.
- `y` — vertical position.
- `vx` — horizontal velocity.
- `vy` — vertical velocity.

The filter uses the following matrices:

- `A` — state transition matrix.
- `H` — measurement matrix.
- `Q` — process noise covariance matrix.
- `R` — measurement noise covariance matrix.
- `P` — estimation error covariance matrix.
- `K` — Kalman gain, which determines how strongly the prediction is corrected using the measurement.

The simulation generates true positions and noisy measurements. The filter estimates the object's state at each step. The estimated positions are then compared with the true positions.

## How to Run

Make sure Python and `uv` are installed.

Open a terminal in the project directory and run:

```bash
uv sync
```

This installs the project dependencies from the project configuration and lock file.

Then run the program:

```bash
uv run python main.py
```

The program prints the simulation results, calculates the errors and success rates, and displays a graph comparing the true, measured, and estimated trajectories.

## Evaluation

The program calculates:

- Average prediction error.
- Average error after Kalman Filter correction.
- Number and percentage of predictions within the chosen error tolerance.
- Number and percentage of corrected estimates within the chosen error tolerance.

The error tolerance is set to `1.0` position unit. A prediction or estimate is considered successful when its distance from the true position is less than or equal to this value.

The results depend on the simulation parameters, initial state, and measurement noise.

## Learning Objectives

This project demonstrates the practical use of NumPy arrays and matrix operations, object-oriented programming, simulation of noisy measurements, Kalman Filter prediction and correction, visualization with Matplotlib, and