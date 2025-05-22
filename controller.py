from datetime import datetime
from model import MeasurementModel, TemperatureMeasurement, HumidityMeasurement
from tkinter import filedialog
from view import MeasurementView


class MeasurementController:
    def __init__(self, root):
        self.model = MeasurementModel()
        self.view = MeasurementView(root)
        self._bind_commands()

    def _bind_commands(self):
        self.view.add_button.config(command=self.add_measurement)
        self.view.delete_button.config(command=self.delete_selected)
        self.view.load_button.config(command=self.load_measurements)

    def add_measurement(self):
        data = self.view.get_input_data()
        try:
            date = datetime.strptime(data["date"], "%Y.%m.%d").date()
            if data["type"] == "Температура":
                measurement = TemperatureMeasurement(date, data["place"], data["value"])
            else:
                measurement = HumidityMeasurement(date, data["place"], data["value"])
            self.model.add_measurement(measurement)
            self.view.update_tree(self.model.measurements)
        except ValueError as e:
            self.view.show_error(f"Неверный формат ввода:\n{e}")

    def delete_selected(self):
        selected_items = self.view.tree.selection()
        for item in selected_items:
            index = self.view.tree.index(item)
            self.model.delete_measurement(index)
        self.view.update_tree(self.model.measurements)

    def load_measurements(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.model.load_from_file(filename)
            self.view.update_tree(self.model.measurements)
