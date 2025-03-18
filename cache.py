import tkinter as tk
import customtkinter
from customtkinter import *
import random

class CacheDataFrame(CTkFrame):
    def __init__(self, master=None, on_submit=None, **kwargs):
        super().__init__(master, **kwargs)
        self.on_submit = on_submit

        # Section for Cache Configuration
        self.label = CTkLabel(master=self, text="Cache Configuration", width=80, height=15, font=("Arial", 15, "bold"))
        self.label.place(relx=0.05, rely=0.02, anchor="nw")

        # Input for Cache Size (2^n Bytes)
        self.label_cache_size = CTkLabel(master=self, text="Cache Size (2^n Bytes)", width=150, height=25)
        self.label_cache_size.place(relx=0.05, rely=0.10, anchor="nw")

        self.entry_cache_size = CTkEntry(master=self, width=100, height=25)
        self.entry_cache_size.place(relx=0.6, rely=0.10, anchor="nw")

        # Input for Block Size in Bytes
        self.label_block_size = CTkLabel(master=self, text="Block Size (Bytes)", width=150, height=25)
        self.label_block_size.place(relx=0.05, rely=0.20, anchor="nw")

        self.entry_block_size = CTkEntry(master=self, width=100, height=25)
        self.entry_block_size.place(relx=0.6, rely=0.20, anchor="nw")

        # Input for RAM Size (2^n Bytes)
        self.label_ram_size = CTkLabel(master=self, text="RAM Size (2^n Bytes)", width=150, height=25)
        self.label_ram_size.place(relx=0.05, rely=0.30, anchor="nw")

        self.entry_ram_size = CTkEntry(master=self, width=100, height=25)
        self.entry_ram_size.place(relx=0.6, rely=0.30, anchor="nw")

        # Input for K-Factor (Associativity)
        self.label_k_factor = CTkLabel(master=self, text="K-Factor (Associativity)", width=180, height=25)
        self.label_k_factor.place(relx=0.05, rely=0.40, anchor="nw")

        self.entry_k_factor = CTkEntry(master=self, width=100, height=25)
        self.entry_k_factor.place(relx=0.6, rely=0.40, anchor="nw")

        # Selection for Eviction Policy
        self.label_eviction_policy = CTkLabel(master=self, text="Eviction Policy", width=150, height=25)
        self.label_eviction_policy.place(relx=0.05, rely=0.50, anchor="nw")

        self.optionmenu_eviction_policy = CTkOptionMenu(master=self, values=["LRU", "FIFO", "Random"])
        self.optionmenu_eviction_policy.place(relx=0.6, rely=0.50, anchor="nw")
        self.optionmenu_eviction_policy.set("LRU")  # Default value

        # Selection for Write Policy
        self.label_write_policy = CTkLabel(master=self, text="Write Policy", width=150, height=25)
        self.label_write_policy.place(relx=0.05, rely=0.60, anchor="nw")

        self.optionmenu_write_policy = CTkOptionMenu(master=self, values=["Write-through", "Write-back"])
        self.optionmenu_write_policy.place(relx=0.6, rely=0.60, anchor="nw")
        self.optionmenu_write_policy.set("Write-through")  # Default value

        # Button to submit configuration
        button = CTkButton(master=self, text="Submit", command=self.submit_data)
        button.place(relx=0.35, rely=0.75, anchor="nw")

    def submit_data(self):
        # Retrieve values from the input fields
        cache_size_power = self.entry_cache_size.get()
        block_size = self.entry_block_size.get()
        ram_size_power = self.entry_ram_size.get()
        k_factor = self.entry_k_factor.get()
        eviction_policy = self.optionmenu_eviction_policy.get()
        write_policy = self.optionmenu_write_policy.get()

        # Call the callback function to update the CacheApp configuration
        if self.on_submit:
            self.on_submit(cache_size_power, block_size, ram_size_power, k_factor, eviction_policy, write_policy)

class CacheView(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label_cache = CTkLabel(master=self, text="Cache Content", width=80, height=15, font=("Arial", 15))
        self.label_cache.place(relx=0.1, rely=0.05, anchor="n")

        self.field_cache = CTkTextbox(master=self, width=600, height=300)
        self.field_cache.place(relx=0.1, rely=0.15, anchor="nw")
        self.field_cache.configure(state="disabled")

    def update_cache_content(self, cache_content):
        self.field_cache.configure(state="normal")
        self.field_cache.delete("1.0", "end")
        for idx, set_content in enumerate(cache_content):
            self.field_cache.insert("end", f"Set {idx}:\n")
            for line_content in set_content:
                self.field_cache.insert("end", f"  {line_content}\n")
            self.field_cache.insert("end", "\n")
        self.field_cache.configure(state="disabled")

class RamMemory(CTkFrame):
    def __init__(self, master=None, ram_size=256, **kwargs):
        super().__init__(master, **kwargs)
        self.ram_size = ram_size
        self.memory = [random.randint(0, 1000) for _ in range(ram_size)]  # Random numbers in base 10

        self.label_ram = CTkLabel(master=self, text="RAM Content", width=80, height=15, font=("Arial", 15))
        self.label_ram.place(relx=0.1, rely=0.05, anchor="n")

        self.field_ram = CTkTextbox(master=self, width=600, height=150)
        self.field_ram.place(relx=0.1, rely=0.15, anchor="nw")
        self.field_ram.configure(state="disabled")
        self.update_ram_content()

    def update_ram_content(self):
        self.field_ram.configure(state="normal")
        self.field_ram.delete("1.0", "end")
        for idx, data in enumerate(self.memory):
            self.field_ram.insert("end", f"Address {hex(idx)}: {data}\n")  # Addresses in hexadecimal
        self.field_ram.configure(state="disabled")

    def get_data(self, address):
        if 0 <= address < len(self.memory):
            return self.memory[address]
        else:
            return None

    def set_data(self, address, value):
        if 0 <= address < len(self.memory):
            self.memory[address] = value
            self.update_ram_content()

class CacheStats(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.stats_label = CTkLabel(master=self, text="Cache Stats", font=("Arial", 15, "bold"))
        self.stats_label.place(relx=0.5, rely=0.1, anchor="c")

        self.hit_label = CTkLabel(master=self, text="Hits: 0", font=("Arial", 15))
        self.hit_label.place(relx=0.05, rely=0.3, anchor="nw")

        self.miss_label = CTkLabel(master=self, text="Misses: 0", font=("Arial", 15))
        self.miss_label.place(relx=0.05, rely=0.5, anchor="nw")

        self.ratio_label = CTkLabel(master=self, text="Hit Ratio: 0%", font=("Arial", 15))
        self.ratio_label.place(relx=0.05, rely=0.7, anchor="nw")

    def update_stats(self, hits, misses):
        self.hit_label.configure(text=f"Hits: {hits}")
        self.miss_label.configure(text=f"Misses: {misses}")
        total = hits + misses
        ratio = (hits / total) * 100 if total > 0 else 0
        self.ratio_label.configure(text=f"Hit Ratio: {ratio:.2f}%")

class Console(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.field_console = tk.Text(self, wrap="word", width=80, height=10, font=("Arial", 15),
                                     bg="black", fg="white", insertbackground="white")
        self.field_console.place(relx=0.485, rely=0.5, anchor="c", width=1100, height=342)

        self.scrollbar = tk.Scrollbar(self, command=self.field_console.yview)
        self.scrollbar.place(relx=0.98, rely=0.5, anchor="c", height=342)

        self.field_console.config(yscrollcommand=self.scrollbar.set)

        self.field_console.insert("1.0", "Here is the console")
        self.field_console.configure(state="disabled")

    def update_console(self, message):
        self.field_console.configure(state="normal")
        self.field_console.insert("end", f"\n{message}")
        self.field_console.configure(state="disabled")
        self.field_console.see("end")

class DataInput(CTkFrame):
    def __init__(self, master=None, console=None, cache_app=None, **kwargs):
        super().__init__(master, **kwargs)
        self.console = console
        self.cache_app = cache_app

        self.label_data = CTkLabel(master=self, text="Address Input (Hexadecimal)", font=("Arial", 15, "bold"))
        self.label_data.place(relx=0.5, rely=0.05, anchor="c")

        self.entry_data = CTkEntry(master=self, width=100, height=25)
        self.entry_data.place(relx=0.5, rely=0.15, anchor="c")

        # Selection for Read or Write Operation
        self.label_operation = CTkLabel(master=self, text="Operation", font=("Arial", 15))
        self.label_operation.place(relx=0.5, rely=0.30, anchor="c")

        self.optionmenu_operation = CTkOptionMenu(master=self, values=["Read", "Write"], command=self.operation_changed)
        self.optionmenu_operation.place(relx=0.5, rely=0.40, anchor="c")
        self.optionmenu_operation.set("Read")  # Default is Read

        # Entry for Data (only visible when Write is selected)
        self.label_data_value = CTkLabel(master=self, text="Data to Write (Decimal)", font=("Arial", 15))
        self.entry_data_value = CTkEntry(master=self, width=100, height=25)

        # Button to submit data
        self.button_submit = CTkButton(master=self, text="Submit", command=self.submit_data)
        self.button_submit.place(relx=0.5, rely=0.85, anchor="c")

    def operation_changed(self, value):
        if value == "Write":
            self.label_data_value.place(relx=0.5, rely=0.55, anchor="c")
            self.entry_data_value.place(relx=0.5, rely=0.65, anchor="c")
        else:
            self.label_data_value.place_forget()
            self.entry_data_value.place_forget()

    def submit_data(self):
        entered_address = self.entry_data.get()
        operation = self.optionmenu_operation.get()
        data_value = self.entry_data_value.get() if operation == "Write" else None

        try:
            # Convert hexadecimal input to integer
            address = int(entered_address, 16)
            if operation == "Write":
                # Validate data_value
                data = int(data_value)
                if data < 0 or data > 255:
                    self.console.update_console("Error: Data to write must be between 0 and 255.")
                    return
            else:
                data = None

            self.cache_app.access_address(address, operation, data)
        except ValueError:
            self.console.update_console("Invalid address or data entered. Please enter valid values.")

class CacheApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")  # Set window size
        self.title("Cache Memory Simulator")  # Set window title

        # Initialize cache and RAM
        self.cache = []
        self.cache_size = 0
        self.num_cache_lines = 0
        self.block_size = 0
        self.ram_size = 256  # Default RAM size
        self.k_factor = 1  # Default associativity (Direct Mapping)
        self.num_sets = 0

        self.hits = 0
        self.misses = 0
        self.access_counter = 0  # Counter for LRU and FIFO policies

        # Left side frames
        self.cache_frame_height = 300
        self.cache_stats_height = 200
        self.data_input_height = 300

        self.cache_frame = CacheDataFrame(master=self, width=350, height=self.cache_frame_height, on_submit=self.update_cache_config)
        self.cache_frame.place(relx=0.01, rely=0.0, anchor="nw")

        self.cache_stats = CacheStats(master=self, width=350, height=self.cache_stats_height)
        self.cache_stats.place(relx=0.01, rely=self.cache_frame_height / 800, anchor="nw")

        self.console = Console(master=self, width=750, height=250)
        self.console.place(relx=0.98, rely=(350 + 200) / 800, anchor="ne")

        self.data_input = DataInput(master=self, width=350, height=self.data_input_height, console=self.console, cache_app=self)
        self.data_input.place(relx=0.01, rely=(self.cache_frame_height + self.cache_stats_height) / 800, anchor="nw")

        # Right side frames
        self.cache_view = CacheView(master=self, width=750, height=350)
        self.cache_view.place(relx=0.98, rely=0.0, anchor="ne")

        self.ram_frame = RamMemory(master=self, width=750, height=200, ram_size=self.ram_size)
        self.ram_frame.place(relx=0.98, rely=350 / 800, anchor="ne")

    def update_cache_config(self, cache_size_power, block_size, ram_size_power, k_factor, eviction_policy, write_policy):
        # ERROR HANDLING: Validate inputs
        error_message = ""
        try:
            cache_size_power = int(cache_size_power)
            block_size = int(block_size)
            ram_size_power = int(ram_size_power)
            k_factor = int(k_factor)
        except ValueError:
            error_message += "All input values must be integers.\n"

        if not error_message:
            if cache_size_power < 0:
                error_message += "Cache size power must be non-negative.\n"
            if ram_size_power < 0:
                error_message += "RAM size power must be non-negative.\n"
            if block_size <= 0:
                error_message += "Block size must be positive.\n"
            if k_factor <= 0:
                error_message += "K-factor must be positive.\n"

        if error_message:
            self.console.update_console("Configuration Error:\n" + error_message)
            return

        # Compute sizes
        self.cache_size = 2 ** cache_size_power
        self.block_size = block_size
        self.ram_size = 2 ** ram_size_power
        self.k_factor = k_factor
        self.eviction_policy = eviction_policy
        self.write_policy = write_policy

        # ERROR HANDLING: Check relationships
        if self.block_size > self.cache_size:
            self.console.update_console("Configuration Error:\nBlock size cannot be larger than cache size.")
            return

        if self.cache_size % self.block_size != 0:
            self.console.update_console("Configuration Error:\nCache size must be divisible by block size.")
            return

        self.num_cache_lines = self.cache_size // self.block_size

        if self.num_cache_lines == 0:
            self.console.update_console("Configuration Error:\nNo cache lines available. Check cache and block size.")
            return

        if self.num_cache_lines % self.k_factor != 0:
            self.console.update_console("Configuration Error:\nNumber of cache lines must be divisible by K-factor.")
            return

        self.num_sets = self.num_cache_lines // self.k_factor
        if self.num_sets == 0:
            self.console.update_console("Configuration Error:\nK-factor is too large, resulting in zero sets.")
            return

        if self.ram_size == 0:
            self.console.update_console("Configuration Error:\nRAM size cannot be zero.")
            return

        # If all checks pass, proceed
        self.cache = [[{'valid': 0, 'tag': None, 'data': None, 'dirty': False, 'inserted_at': None, 'last_used': None} 
                        for _ in range(self.k_factor)] for _ in range(self.num_sets)]

        # Re-initialize RAM with the new size
        self.ram_frame.ram_size = self.ram_size
        self.ram_frame.memory = [random.randint(0, 256) for _ in range(self.ram_size)]  # Random data
        self.ram_frame.update_ram_content()

        # Reset hits and misses
        self.hits = 0
        self.misses = 0
        self.access_counter = 0  # Reset access counter

        # Update cache view
        cache_content_display = []
        for idx in range(self.num_sets):
            lines = []
            for line_idx in range(self.k_factor):
                line = self.cache[idx][line_idx]
                if line['valid'] == 0:
                    lines.append(f"Line {line_idx}: Valid:0, Empty")
                else:
                    lines.append(f"Line {line_idx}: Valid:1, Tag:{line['tag']}, Data:{line['data']}, Dirty:{line['dirty']}")
            cache_content_display.append(lines)
        self.cache_view.update_cache_content(cache_content_display)

        # Update cache stats
        self.cache_stats.update_stats(self.hits, self.misses)

        # Update console
        message = f"Cache configurations updated:\nCache Size: {self.cache_size} Bytes\nNumber of Cache Lines: {self.num_cache_lines}\n"
        message += f"Block Size: {self.block_size} Bytes\nRAM Size: {self.ram_size} Bytes\nK-Factor (Associativity): {self.k_factor}\n"
        message += f"Number of Sets: {self.num_sets}\n"
        message += f"Eviction Policy: {self.eviction_policy}\n"
        message += f"Write Policy: {self.write_policy}\n"
        self.console.update_console(message)

    def access_address(self, address, operation="Read", data=None):
        self.access_counter += 1  # Increment the access counter

        message = f"{operation} operation at address: {hex(address)}\n"  # Address in hexadecimal

        if address < 0 or address >= self.ram_size:
            message += f"Address {hex(address)} is out of bounds.\n"
            self.console.update_console(message)
            return

        block_address = address // self.block_size
        set_index = block_address % self.num_sets
        tag = block_address // self.num_sets

        cache_set = self.cache[set_index]

        # Search for tag in the set
        cache_line = None
        line_index = None
        for i, line in enumerate(cache_set):
            if line['valid'] == 1 and line['tag'] == tag:
                cache_line = line
                line_index = i
                break

        if cache_line is not None:
            # Cache Hit
            self.hits += 1
            cache_line['last_used'] = self.access_counter  # Update last used
            if operation == "Read":
                data_value = cache_line['data'][address % self.block_size]
                message += f"Cache Hit in set {set_index}. Data: {data_value}\n"
            elif operation == "Write":
                data_value = data  # Data to write
                cache_line['data'][address % self.block_size] = data_value
                message += f"Cache Hit in set {set_index}. Wrote data: {data_value}\n"
                if self.write_policy == "Write-through":
                    # Write to RAM immediately
                    self.ram_frame.set_data(address, data_value)
                    message += f"Write-through policy: Data written to RAM at address {hex(address)}\n"
                elif self.write_policy == "Write-back":
                    # Mark the line as dirty
                    cache_line['dirty'] = True
                    message += f"Write-back policy: Data marked as dirty in cache\n"
        else:
            # Cache Miss
            self.misses += 1
            # Find an invalid line first
            invalid_line_index = None
            for i, line in enumerate(cache_set):
                if line['valid'] == 0:
                    invalid_line_index = i
                    break

            if invalid_line_index is not None:
                # Use the invalid line
                evict_line = cache_set[invalid_line_index]
                message += f"Cache Miss. Using an invalid line in set {set_index}.\n"
            else:
                # Evict a line according to the eviction policy
                if self.eviction_policy == "LRU":
                    # Evict the valid line with the smallest 'last_used' value
                    evict_line = min((l for l in cache_set if l['valid'] == 1), key=lambda x: x['last_used'])
                elif self.eviction_policy == "FIFO":
                    # Evict the valid line with the smallest 'inserted_at' value
                    evict_line = min((l for l in cache_set if l['valid'] == 1), key=lambda x: x['inserted_at'])
                elif self.eviction_policy == "Random":
                    evict_line = random.choice([l for l in cache_set if l['valid'] == 1])

                evict_line_index = cache_set.index(evict_line)
                # If the evicted line is dirty and write-back policy, write it back to RAM
                if self.write_policy == "Write-back" and evict_line.get('dirty', False):
                    block_start_address = (evict_line['tag'] * self.num_sets + set_index) * self.block_size
                    for i, val in enumerate(evict_line['data']):
                        self.ram_frame.set_data(block_start_address + i, val)
                    message += f"Evicted dirty cache line with tag {evict_line['tag']}. Written back to RAM.\n"
                else:
                    message += f"Evicted cache line with tag {evict_line['tag']} from set {set_index}.\n"

                # This line will be reused
                evict_line_index = cache_set.index(evict_line)
                evict_line = cache_set[evict_line_index]

            # Load the block into the chosen line
            block_start_address = block_address * self.block_size
            block_end_address = min(block_start_address + self.block_size, self.ram_size)
            block_data = [self.ram_frame.get_data(addr) for addr in range(block_start_address, block_end_address)]

            evict_line['valid'] = 1
            evict_line['tag'] = tag
            evict_line['data'] = block_data
            evict_line['inserted_at'] = self.access_counter
            evict_line['last_used'] = self.access_counter
            evict_line['dirty'] = False

            if operation == "Read":
                data_value = evict_line['data'][address % self.block_size]
                message += f"Loaded block into cache. Data at address {hex(address)}: {data_value}\n"
            elif operation == "Write":
                data_value = data  # Data to write
                evict_line['data'][address % self.block_size] = data_value
                if self.write_policy == "Write-through":
                    self.ram_frame.set_data(address, data_value)
                    message += f"Write-through policy: Data written to RAM at address {hex(address)}\n"
                elif self.write_policy == "Write-back":
                    evict_line['dirty'] = True
                    message += f"Write-back policy: Data marked as dirty in cache\n"

        # Update cache stats
        self.cache_stats.update_stats(self.hits, self.misses)

        # Update cache view
        cache_content_display = []
        for idx, cache_set in enumerate(self.cache):
            set_lines = []
            for line_idx, line in enumerate(cache_set):
                if line['valid'] == 0:
                    line_content = f"Line {line_idx}: Valid:0, Empty"
                else:
                    line_content = (f"Line {line_idx}: Valid:1, Tag:{line['tag']}, "
                                    f"Data:{line['data']}, Inserted:{line['inserted_at']}, "
                                    f"LastUsed:{line['last_used']}, Dirty:{line['dirty']}")
                set_lines.append(line_content)
            cache_content_display.append(set_lines)
        self.cache_view.update_cache_content(cache_content_display)

        self.console.update_console(message)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("Dark")  # Set dark mode
    customtkinter.set_default_color_theme("blue")  # Set default blue theme
    
    app = CacheApp()
    app.mainloop()
