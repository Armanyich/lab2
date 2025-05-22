from datetime import datetime
import re
from tkinter import messagebox
from log_utils import logger


class InvalidMeasurementError(Exception):
    """Исключение для некорректных строк измерений."""
    pass


class Measurement:
    def __init__(self, date, place, value):
        self.date = date
        self.place = place
        self.value = value

    def to_list(self):
        return [self.date.strftime("%Y.%m.%d"), self.place, str(self.value)]


class TemperatureMeasurement(Measurement):
    def __init__(self, date, place, value):
        super().__init__(date, place, float(value))


class HumidityMeasurement(Measurement):
    def __init__(self, date, place, value):
        super().__init__(date, place, int(value))


class MeasurementParser:
    @staticmethod
    def parse(line):
        try:
            if "температуры" in line.lower():
                measurement_type = "Температура"
            elif "влажности" in line.lower():
                measurement_type = "Влажность"
            else:
                raise InvalidMeasurementError(f"Неизвестный тип измерения: {line.strip()}")

            date_match = re.search(r'\d{4}\.\d{2}\.\d{2}', line)
            if not date_match:
                raise InvalidMeasurementError(f"Дата не найдена в строке: {line.strip()}")

            line_parts = line[date_match.start():].strip().split()
            if len(line_parts) < 3:
                raise InvalidMeasurementError(f"Недостаточно данных: {line.strip()}")

            date = datetime.strptime(line_parts[0], "%Y.%m.%d").date()
            place = line_parts[1].strip('"')
            value = line_parts[2].replace('%', '') if '%' in line_parts[2] else line_parts[2]

            if measurement_type == "Температура":
                return TemperatureMeasurement(date, place, value)
            else:
                return HumidityMeasurement(date, place, value)

        except (ValueError, InvalidMeasurementError) as e:
            logger.error(f"Ошибка обработки строки: {line.strip()} — {e}")
            return None


class MeasurementStorage:
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
