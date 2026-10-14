# 2D Kalman Filter in Python

## Description

This project implements a two-dimensional Kalman Filter using Python and NumPy. It simulates the movement of an object, generates noisy GPS measurements, and estimates the object's position using the Kalman Filter algorithm.

The goal is to demonstrate how a Kalman Filter combines a motion model with noisy measurements to improve position estimation.

## Features

- Simulates object movement in two dimensions.
- Generates noisy GPS measurements using a normal distribution.
- Predicts the object's next state.
- Corrects the prediction using GPS measurements.
- Calculates prediction errors and average estimation error.
- Evaluates prediction success based on a specified error tolerance.

## Technologies

- Python
- NumPy

## Project Structure

- `main.py` — runs the Kalman Filter and evaluates the results.
- `kalman_filter_cl.py` — contains the Kalman Filter implementation.
- `simulation.py` — simulates object movement and generates noisy measurements.

## How It Works

The Kalman Filter follows two main steps:

1. **Prediction:** Estimates the next state of the object using the motion model.
2. **Update:** Corrects the predicted state using the GPS measurement.

The filter uses the following matrices:

- `A` — state transition matrix.
- `H` — measurement matrix.
- `Q` — process noise covariance matrix.
- `R` — measurement noise covariance matrix.
- `P` — estimation error covariance matrix.

The estimated positions are compared with the true positions to evaluate the filter's performance.

## How to Run

1. Install Python 3.12 or a compatible Python version.
2. Install NumPy:

   ```bash
   pip install numpy
   ```

3. Run the main program:

   ```bash
   python main.py
   ```

## Evaluation

The program calculates the average position estimation error and the percentage of predictions within a specified error tolerance.

The results depend on the simulation parameters, initial state, and measurement noise.

## Learning Objectives

This project demonstrates practical use of NumPy arrays and matrix operations, object-oriented programming, simulation, and basic error analysis.
