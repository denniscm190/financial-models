import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def histogram(data, bins, color, ylabel, xlabel, title, grid):
    plt.hist(data, bins, facecolor=color)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.grid(grid)
    plt.show()


def plot(data, ylabel, xlabel, title, grid):
    fig = plt.figure()
    plt.plot(data)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.grid(grid)
    plt.show()


def historical_plot(data, ylabel, title, grid):
    fig, ax = plt.subplots()
    ax.plot(data)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(grid)
    plt.xticks(rotation=65)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(len(data) * 0.1))  # Tick Spacing
    plt.tight_layout()
    plt.show()
