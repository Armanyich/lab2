import unittest
from datetime import datetime
from model import (
    TemperatureMeasurement, HumidityMeasurement,
    MeasurementModel, MeasurementParser
)


class TestMeasurements(unittest.TestCase):

    def test_parser_valid_temperature(self):
        line = 'Измерение температуры 2023.05.01 "Москва" 22.3'
        m = MeasurementParser.parse(line)
        self.assertIsInstance(m, TemperatureMeasurement)
        self.assertEqual(m.place, "Москва")
        self.assertEqual(m.value, 22.3)

    def test_parser_valid_humidity(self):
        line = 'Измерение влажности 2023.05.01 "СПб" 60%'
        m = MeasurementParser.parse(line)
        self.assertIsInstance(m, HumidityMeasurement)
        self.assertEqual(m.place, "СПб")
        self.assertEqual(m.value, 60)

    def test_parser_invalid_format(self):
        line = 'Неверная строка без даты и значения'
        m = MeasurementParser.parse(line)
        self.assertIsNone(m)

    def test_model_add_and_delete(self):
        model = MeasurementModel()
        m1 = TemperatureMeasurement(datetime(2023, 5, 1).date(), "Москва", "25")
        m2 = HumidityMeasurement(datetime(2023, 5, 2).date(), "Сочи", "55")
        model.add_measurement(m1)
        model.add_measurement(m2)
        self.assertEqual(len(model.measurements), 2)

        model.delete_measurement(0)
        self.assertEqual(len(model.measurements), 1)
        self.assertIsInstance(model.measurements[0], HumidityMeasurement)


if __name__ == "__main__":
    unittest.main()
