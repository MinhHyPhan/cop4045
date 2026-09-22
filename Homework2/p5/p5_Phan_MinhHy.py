"""Read and validate daily weather-station observations."""

import csv
import math
import sys
from datetime import datetime
from pathlib import Path


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"
MIN_TEMPERATURE = -100.0
MAX_TEMPERATURE = 150.0


def read_observations(filename):
    """Read weather observations from *filename*.

    Valid input rows have the form ``station,date,temperature``.  The returned
    observations dictionary maps each station name to a chronologically sorted
    list of ``(datetime, float)`` tuples.  Invalid rows are omitted and reported
    as ``(line_number, error_message)`` tuples.

    File access errors are intentionally allowed to propagate so a caller can
    decide how they should be handled.
    """
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8", newline="") as input_file:
        for line_number, row in enumerate(csv.reader(input_file), start=1):
            if len(row) != 3:
                errors.append((line_number, "malformed line"))
                continue

            station, date_text, temperature_text = (
                field.strip() for field in row
            )

            if not station or not date_text or not temperature_text:
                errors.append((line_number, "malformed line"))
                continue

            try:
                date = datetime.strptime(date_text, DATE_FORMAT)
            except ValueError:
                errors.append((line_number, "invalid date"))
                continue

            try:
                temperature = float(temperature_text)
            except ValueError:
                errors.append((line_number, "invalid temperature"))
                continue

            if not math.isfinite(temperature) or not (
                MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE
            ):
                errors.append((line_number, "invalid temperature"))
                continue

            station_date = (station, date)
            if station_date in seen:
                errors.append((line_number, "duplicate station/date"))
                continue

            seen.add(station_date)
            observations.setdefault(station, []).append((date, temperature))

    for station_observations in observations.values():
        station_observations.sort(key=lambda observation: observation[0])

    return observations, errors


def station_statistics(observations):
    """Return the minimum, maximum, and mean temperature per station.

    Each value in the returned dictionary is a
    ``(minimum, maximum, mean)`` tuple.
    """
    statistics = {}

    for station, station_observations in observations.items():
        temperatures = [temperature for _, temperature in station_observations]
        if temperatures:
            statistics[station] = (
                min(temperatures),
                max(temperatures),
                sum(temperatures) / len(temperatures),
            )

    return statistics


def station_outliers(observations):
    """Return stations whose latest temperature is above their mean."""
    statistics = station_statistics(observations)

    return {
        station: (
            station_observations[-1][0],
            station_observations[-1][1],
            statistics[station][2],
        )
        for station, station_observations in observations.items()
        if station_observations
        and station_observations[-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    """Write station statistics to *filename* in lexicographic order.

    Each output row contains the station name followed by its minimum,
    maximum, and mean temperature. Numeric values use one decimal place.
    """
    with open(filename, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            writer.writerow(
                (station, f"{minimum:.1f}", f"{maximum:.1f}", f"{mean:.1f}")
            )


def main():
    """Read observations, display results, and write station statistics."""
    if len(sys.argv) != 3:
        program_name = Path(sys.argv[0]).name if sys.argv else "weather.py"
        print(
            f"Usage: {program_name} INPUT_FILE OUTPUT_FILE",
            file=sys.stderr,
        )
        return 1

    input_filename, output_filename = sys.argv[1:]

    try:
        observations, errors = read_observations(input_filename)
        statistics = station_statistics(observations)
        outliers = station_outliers(observations)

        print("Statistics:", statistics)
        print("Outliers:", outliers)

        for line_number, message in errors:
            print(f"Line {line_number}: {message}", file=sys.stderr)

        write_statistics(output_filename, statistics)
    except OSError as error:
        print(f"File error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
