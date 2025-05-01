from datetime import datetime
import re
from tkinter import messagebox, filedialog


class Measurement:
    """Базовый класс измерения."""

    def __init__(self, date, place, value):
        self.date = date
        self.place = place
        self.value = value

    def to_list(self):
        return [self.date.strftime("%Y.%m.%d"), self.place, str(self.value)]


class TemperatureMeasurement(Measurement):
    """Температурное измерение."""

    def __init__(self, date, place, value):
        super().__init__(date, place, float(value))


class HumidityMeasurement(Measurement):
    """Измерение влажности."""

    def __init__(self, date, place, value):
        super().__init__(date, place, int(value))


class MeasurementParser:
    """Парсинг строки в измерение."""

    @staticmethod
    def parse(line):
        if "температуры" in line.lower():
            measurement_type = "Температура"
        elif "влажности" in line.lower():
            measurement_type = "Влажность"
        else:
            print(f"Неизвестный тип измерения в строке: {line.strip()}")
            return None

        date_match = re.search(r'\d{4}\.\d{2}\.\d{2}', line)
        if not date_match:
            print(f"Не найдена дата в строке: {line.strip()}")
            return None

        line_parts = line[date_match.start():].strip().split()
        if len(line_parts) < 3:
            print(f"Недостаточно данных в строке: {line.strip()}")
            return None

        try:
            date = datetime.strptime(line_parts[0], "%Y.%m.%d").date()
            place = line_parts[1].strip('"')
            value = line_parts[2]
            
            if measurement_type == "Влажность" and '%' in value:
                value = value.replace('%', '')

            if measurement_type == "Температура":
                return TemperatureMeasurement(date, place, value)
            elif measurement_type == "Влажность":
                return HumidityMeasurement(date, place, value)
        except ValueError as e:
            print(f"Ошибка обработки строки '{line.strip()}': {e}")
            return None


class MeasurementStorage:
    """Работа с файлом измерений."""

    @staticmethod
    def load_from_file(filename):
        measurements = []
        try:
            with open(filename, encoding="utf-8") as file:
                for line in file:
                    if not line.strip():
                        continue
                    measurement = MeasurementParser.parse(line)
                    if measurement:
                        measurements.append(measurement)
        except FileNotFoundError:
            messagebox.showwarning("Внимание", f"Файл '{filename}' не найден")
        return measurements


class MeasurementModel:
    """Модель данных измерений."""

    def __init__(self):
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)

    def delete_measurement(self, index):
        if 0 <= index < len(self.measurements):
            del self.measurements[index]

    def load_from_file(self, filename):
        self.measurements = MeasurementStorage.load_from_file(filename)
        return self.measurements