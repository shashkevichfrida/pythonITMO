import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
a0, a1, a2, a3 = 0.5, 0.3, -0.2, 0.1
n_obs = 1000

def time_series_generation():
    np.random.seed(42)
    epsilon = np.random.normal(0, 1, n_obs)
    xt = np.zeros(n_obs)

    for t in range(3, n_obs):
        xt[t] = a0 + a1 * xt[t-1] + a2 * xt[t-2] + a3 * xt[t-3] + epsilon[t]
    return xt

def checking_for_stationarity(xt):
    first_half = xt[:n_obs//2]
    second_half = xt[n_obs//2:]

    mean_diff = np.abs(np.mean(first_half) - np.mean(second_half))
    variance_diff = np.abs(np.var(first_half) - np.var(second_half))

    print("Mean Difference:", mean_diff)
    print("Variance Difference:", variance_diff)

def show_time_series(xt):
    plt.plot(xt)
    plt.title("Временной ряд AR(3)")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.show()


xt = time_series_generation()
checking_for_stationarity(xt)
show_time_series(xt)
