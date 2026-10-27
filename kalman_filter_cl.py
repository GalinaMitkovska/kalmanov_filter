import numpy as np


class KalmanFilter:
    def __init__(self, A, H, Q, R, P, x):
        self.A = A
        self.H = H
        self.Q = Q
        self.R = R
        self.P = P
        self.x = x


    def predict(self):
        self.x_pred = self.A @ self.x
        self.P_pred = self.A @ self.P @ self.A.T + self.Q

        return self.x_pred, self.P_pred



    def update(self, z):
        y = z - self.H @ self.x_pred

        S = self.H @ self.P_pred @ self.H.T + self.R

        K = self.P_pred @ self.H.T @ np.linalg.inv(S)

        self.x = self.x_pred + K @ y

        I = np.eye(self.P.shape[0])
        self.P = (I - K @ self.H) @ self.P_pred

        return self.x