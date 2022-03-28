import numpy as np
import matplotlib.pyplot as plt

# samp1 = np.random.standard_normal(30)
# samp2 = np.random.standard_normal(30)

# data = np.vstack((samp1, samp2))
# plt.scatter(data[:, 0], data[:, 1])
# plt.show()


def generate_data() -> np.array:
    """Generate data."""
    mu0 = np.array([0, 0])
    mu1 = np.array([5, 0])
    Sigma0 = np.array([[1, 0], [0, 1]])
    Sigma1 = np.array([[1, 0], [0, 1]])
    points0 = np.random.multivariate_normal(mu0, Sigma0, size=100)
    points1 = np.random.multivariate_normal(mu1, Sigma1, size=100)
    return np.vstack((points0, points1))


def plot_data(data: np.ndarray):
    """Plot data."""
    plt.scatter(data[:, 0], data[:, 1])
    plt.show()


plot_data(generate_data())
