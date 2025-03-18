import tkinter as tk
from cache import CacheApp
import matplotlib
matplotlib.use("TkAgg")  # Use the TkAgg backend for matplotlib in Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ExtendedCacheApp(CacheApp):
    def __init__(self):
        super().__init__()
        
        # Lists to keep track of time steps (access number) and hit ratios over time
        self.time_steps = []
        self.hit_ratios = []
        self.access_count = 0  # Counts how many accesses have been made

        # Add a button to show hit ratio graph over time
        self.show_graph_button = tk.Button(self, text="Show Graph", command=self.show_graph_window)
        self.show_graph_button.place(relx=0.5, rely=0.95, anchor="center")

    def access_address(self, address, operation="Read", data=None):
        # Use the parent class's method to actually perform the access
        super().access_address(address, operation, data)
        
        # After each access, record the current hit ratio
        self.access_count += 1
        hits = self.hits
        misses = self.misses
        total = hits + misses
        hit_ratio = (hits / total) * 100 if total > 0 else 0

        self.time_steps.append(self.access_count)
        self.hit_ratios.append(hit_ratio)

    def show_graph_window(self):
        # Create a new window to display the graph
        graph_window = tk.Toplevel(self)
        graph_window.title("Hit Ratio Over Time")

        # Create a matplotlib figure
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Plot the hit ratio over time as a line plot
        ax.plot(self.time_steps, self.hit_ratios, marker='o', color='blue')
        ax.set_title("Hit Ratio Over Time")
        ax.set_xlabel("Access Number")
        ax.set_ylabel("Hit Ratio (%)")
        ax.grid(True)

        # Embed the matplotlib figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a close button
        close_button = tk.Button(graph_window, text="Close", command=graph_window.destroy)
        close_button.pack(side=tk.BOTTOM, pady=10)

if __name__ == "__main__":
    app = ExtendedCacheApp()
    app.mainloop()
