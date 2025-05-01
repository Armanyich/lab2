import tkinter as tk
from tkinter import ttk, messagebox
from model import TemperatureMeasurement, HumidityMeasurement

class MeasurementView:
    """Графический интерфейс для отображения измерений."""

    def __init__(self, root):
        self.root = root
        self.root.title("Измерения")
        self._create_widgets()

    def _create_widgets(self):
        self.date_entry = tk.Entry(self.root)
        self.place_entry = tk.Entry(self.root)
        self.value_entry = tk.Entry(self.root)

        self.type_var = tk.StringVar(value="Температура")
        self.type_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.type_var,
            values=["Температура", "Влажность"],
            state="readonly",
            width=15
        )

        tk.Label(self.root, text="Дата (ГГГГ.ММ.ДД):").grid(row=0, column=0)
        tk.Label(self.root, text="Место:").grid(row=0, column=2)
        tk.Label(self.root, text="Значение:").grid(row=0, column=4)
        tk.Label(self.root, text="Тип:").grid(row=0, column=6)

        self.date_entry.grid(row=0, column=1)
        self.place_entry.grid(row=0, column=3)
        self.value_entry.grid(row=0, column=5)
        self.type_dropdown.grid(row=0, column=7)

        self.add_button = tk.Button(self.root, text="Добавить")
        self.delete_button = tk.Button(self.root, text="Удалить")
        self.load_button = tk.Button(self.root, text="Загрузить")

        self.add_button.grid(row=1, column=0)
        self.delete_button.grid(row=1, column=1)
        self.load_button.grid(row=1, column=2)

        self.tree = ttk.Treeview(
            self.root, columns=("date", "place", "value", "type"), show="headings"
        )
        self.tree.heading("date", text="Дата")
        self.tree.heading("place", text="Место")
        self.tree.heading("value", text="Значение")
        self.tree.heading("type", text="Тип")
        self.tree.grid(row=2, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=8, sticky="ns")

    def get_input_data(self):
        return {
            "date": self.date_entry.get(),
            "place": self.place_entry.get(),
            "value": self.value_entry.get(),
            "type": self.type_var.get()
        }

    def show_error(self, message):
        messagebox.showerror("Ошибка", message)

    def update_tree(self, measurements):
        self.tree.delete(*self.tree.get_children())
        for m in measurements:
            self.tree.insert("", "end", values=m.to_list() + [self._get_measurement_type(m)])

    def _get_measurement_type(self, measurement):
        return "Температура" if isinstance(m, TemperatureMeasurement) else "Влажность"