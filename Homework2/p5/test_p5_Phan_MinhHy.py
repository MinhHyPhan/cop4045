"""Unit tests for the weather observation program."""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from p5_Phan_MinhHy import (
    read_observations,
    station_outliers,
    station_statistics,
    write_statistics,
)


class WeatherObservationTests(unittest.TestCase):
    """Test weather observation parsing and analysis."""

    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary_directory.name)

    def tearDown(self):
        self.temporary_directory.cleanup()

    def write_input(self, contents):
        """Create an input file and return its path."""
        input_path = self.directory / "observations.csv"
        input_path.write_text(contents, encoding="utf-8")
        return input_path

    def test_reads_several_stations_and_sorts_observations(self):
        input_path = self.write_input(
            "Boston,09:00:00 AM 04/21/2026,60.0\n"
            "Albany,08:00:00 AM 04/20/2026,45.0\n"
            "Boston,09:00:00 AM 04/20/2026,55.0\n"
        )

        observations, errors = read_observations(input_path)

        self.assertEqual(errors, [])
        self.assertEqual(set(observations), {"Albany", "Boston"})
        self.assertEqual(
            observations["Boston"],
            [
                (datetime(2026, 4, 20, 9), 55.0),
                (datetime(2026, 4, 21, 9), 60.0),
            ],
        )

    def test_accepts_negative_temperatures(self):
        input_path = self.write_input(
            "North Pole,12:00:00 AM 01/01/2026,-42.5\n"
        )

        observations, errors = read_observations(input_path)

        self.assertEqual(errors, [])
        self.assertEqual(observations["North Pole"][0][1], -42.5)

    def test_rejects_duplicate_station_and_date(self):
        input_path = self.write_input(
            "Boston,09:00:00 AM 04/20/2026,55.0\n"
            "Boston,09:00:00 AM 04/20/2026,70.0\n"
        )

        observations, errors = read_observations(input_path)

        self.assertEqual(observations["Boston"], [(datetime(2026, 4, 20, 9), 55.0)])
        self.assertEqual(errors, [(2, "duplicate station/date")])

    def test_rejects_temperatures_outside_valid_range(self):
        input_path = self.write_input(
            "Low,01:00:00 AM 01/01/2026,-100.1\n"
            "Minimum,01:00:00 AM 01/01/2026,-100.0\n"
            "Maximum,01:00:00 AM 01/01/2026,150.0\n"
            "High,01:00:00 AM 01/01/2026,150.1\n"
        )

        observations, errors = read_observations(input_path)

        self.assertEqual(set(observations), {"Minimum", "Maximum"})
        self.assertEqual(
            errors,
            [(1, "invalid temperature"), (4, "invalid temperature")],
        )

    def test_calculates_station_statistics(self):
        observations = {
            "Boston": [
                (datetime(2026, 4, 20), -5.0),
                (datetime(2026, 4, 21), 10.0),
                (datetime(2026, 4, 22), 25.0),
            ]
        }

        statistics = station_statistics(observations)

        self.assertEqual(statistics["Boston"], (-5.0, 25.0, 10.0))

    def test_finds_station_outliers(self):
        observations = {
            "Rising": [
                (datetime(2026, 4, 20), 10.0),
                (datetime(2026, 4, 21), 20.0),
            ],
            "Falling": [
                (datetime(2026, 4, 20), 20.0),
                (datetime(2026, 4, 21), 10.0),
            ],
        }

        outliers = station_outliers(observations)

        self.assertEqual(
            outliers,
            {"Rising": (datetime(2026, 4, 21), 20.0, 15.0)},
        )

    def test_writes_sorted_output_with_one_decimal_place(self):
        output_path = self.directory / "statistics.csv"
        statistics = {
            "Zulu": (-2.0, 12.25, 5.125),
            "Alpha": (1.0, 3.0, 2.0),
        }

        write_statistics(output_path, statistics)

        self.assertEqual(
            output_path.read_text(encoding="utf-8").splitlines(),
            ["Alpha,1.0,3.0,2.0", "Zulu,-2.0,12.2,5.1"],
        )

    def test_missing_input_file_raises_file_not_found_error(self):
        missing_path = self.directory / "missing.csv"

        with self.assertRaises(FileNotFoundError):
            read_observations(missing_path)


if __name__ == "__main__":
    unittest.main()
