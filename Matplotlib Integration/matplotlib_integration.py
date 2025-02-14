# matplotlib_integration.py
from matplotlib_plot import create_line_plot
import numpy as np

def generate_and_save_plot(data, plot_type, filename="generated_plot.png"):
    """Generates and saves a plot based on the given data and plot type.

    Args:
        data (list): The data to plot.
        plot_type (str): The type of plot to generate (e.g., "line").
        filename (str): The filename to save the plot to.
    """
    if plot_type == "line":
        x = np.arange(len(data))
        create_line_plot(x, data, "Data Plot", "Index", "Value", filename)
    else:
        print("Unsupported plot type.")

if __name__ == '__main__':
    # Example usage:
    data = [1, 3, 2, 4, 5, 3, 2, 1]
    generate_and_save_plot(data, "line", "data_plot.png")
    print("Plot generated and saved to data_plot.png")
