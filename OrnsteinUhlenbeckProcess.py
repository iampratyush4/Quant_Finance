import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

def generate_process(dt=0.1, theta=1.2, mu=0.9, sigma=0.9, n=10000):
    # x(t=0)=0 and initialize x(t) with zeros
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = x[t-1] + theta*(mu-x[t-1])*dt + sigma * normal(0, np.sqrt(dt))
    return x

def plot_process(x):
    plt.plot(x)
    plt.xlabel('t')
    plt.ylabel('x(t)')

    
    plt.title('Ornstein-Uhlenbeck Process')
    plt.show()


if __name__ == '__main__':
    data = generate_process()
    plot_process(data)
