import tkinter as tk
from tkinter import filedialog, ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class DataVisualizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Visualization App")

        # Create Matplotlib Figure and Axes
        self.fig, self.ax = Figure(figsize=(5, 4), dpi=100), None

        # Create Tkinter Canvas to embed Matplotlib Figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create Buttons
        self.load_data_button = tk.Button(master=self.master, text="Load Data", command=self.load_data)
        self.load_data_button.pack(side=tk.BOTTOM)

        self.plot_data_button = tk.Button(master=self.master, text="Plot Data", command=self.plot_data)
        self.plot_data_button.pack(side=tk.BOTTOM)

        # Dropdowns for column selection
        self.x_column_label = tk.Label(master=self.master, text="Select X Column:")
        self.x_column_label.pack(side=tk.LEFT)
        self.x_column_var = tk.StringVar()
        self.x_column_dropdown = ttk.Combobox(master=self.master, textvariable=self.x_column_var, state="disabled")
        self.x_column_dropdown.pack(side=tk.LEFT)

        self.y_column_label = tk.Label(master=self.master, text="Select Y Column:")
        self.y_column_label.pack(side=tk.LEFT)
        self.y_column_var = tk.StringVar()
        self.y_column_dropdown = ttk.Combobox(master=self.master, textvariable=self.y_column_var, state="disabled")
        self.y_column_dropdown.pack(side=tk.LEFT)

        # Dropdown for graph type selection
        self.graph_type_label = tk.Label(master=self.master, text="Select Graph Type:")
        self.graph_type_label.pack(side=tk.LEFT)
        self.graph_type_var = tk.StringVar()
        self.graph_type_var.set("Line Plot")  # Default graph type
        self.graph_type_dropdown = ttk.Combobox(master=self.master, textvariable=self.graph_type_var,
                                                values=["Line Plot", "Scatter Plot"], state="readonly")
        self.graph_type_dropdown.pack(side=tk.LEFT)

        # Instance variable to store loaded data
        self.data = None

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select Data File", filetypes=[("CSV files", "*.csv")])

        try:
            # Assuming you have a CSV file
            self.data = pd.read_csv(file_path)
            
            # Enable column selection dropdowns
            columns = self.data.columns.tolist()
            self.x_column_dropdown['values'] = columns
            self.x_column_dropdown['state'] = 'readonly'

            self.y_column_dropdown['values'] = columns
            self.y_column_dropdown['state'] = 'readonly'
            
            print("Data Loaded Successfully!")

        except Exception as e:
            print(f"Error loading data: {e}")

    def plot_data(self):
        if self.ax is None:
            self.ax = self.fig.add_subplot(111)

        try:
            # Get selected columns and graph type
            selected_x_column = self.x_column_var.get()
            selected_y_column = self.y_column_var.get()
            graph_type = self.graph_type_var.get()

            # Plot the data based on the selected graph type
            if graph_type == "Line Plot":
                self.ax.plot(self.data[selected_x_column], self.data[selected_y_column], label=f"{selected_x_column} vs {selected_y_column}")
            elif graph_type == "Scatter Plot":
                self.ax.scatter(self.data[selected_x_column], self.data[selected_y_column], label=f"{selected_x_column} vs {selected_y_column}")

            self.ax.set_title(f"{graph_type} - {selected_x_column} vs {selected_y_column}")
            self.ax.set_xlabel(selected_x_column)
            self.ax.set_ylabel(selected_y_column)
            self.ax.legend()

            self.canvas.draw()

            print("Data Plotted Successfully!")

        except Exception as e:
            print(f"Error plotting data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizerApp(root)
    root.mainloop()
