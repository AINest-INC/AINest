# matplotlib_plot.py
import matplotlib.pyplot as plt
import numpy as np

def create_line_plot(x_data, y_data, title, x_label, y_label, filename="line_plot.png"):
    """Creates a line plot using Matplotlib.

    Args:
        x_data (list): The x-axis data.
        y_data (list): The y-axis data.
        title (str): The title of the plot.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        filename (str): The filename to save the plot to.
    """
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(filename)
    plt.close()  # Close the plot to free memory

if __name__ == '__main__':
    # Example usage:
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    create_line_plot(x, y, "Sine Wave", "X", "Y", "sine_wave.png")
    print("Line plot created and saved to sine_wave.png")
