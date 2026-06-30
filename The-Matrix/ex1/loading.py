from importlib import import_module, util
import sys


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def instructions(missing: list[str]) -> None:
    print()
    print("Missing dependencies:", ", ".join(missing))
    print()
    print("To install the missing dependencies, run:")
    print("python -m pip install -r requirements.txt")
    print()
    print("Or with Poetry:")
    print("poetry install")


def get_version(package: str) -> str:
    module = import_module(package)
    return getattr(module, "__version__", "unknown")


def check_dependencies() -> bool:
    missing: list[str] = []

    print("Checking dependencies:")

    for package, message in DEPENDENCIES.items():
        if util.find_spec(package) is None:
            print(f"[MISSING] {package}")
            missing.append(package)
        else:
            version = get_version(package)
            print(f"[OK] {package} ({version}) - {message}")

    if missing:
        instructions(missing)
        return False

    return True


def check_hourly(data: object) -> bool:
    nums = [
        "time",
        "temperature_2m",
        "wind_speed_10m",
        "relative_humidity_2m",
    ]

    if "hourly" not in data:
        return False

    hourly = data["hourly"]

    for item in nums:
        if item not in hourly:
            return False

    lengths = [len(hourly[item]) for item in nums]
    return all(length == lengths[0] for length in lengths)


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print()

    if not check_dependencies():
        sys.exit(1)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=32.5556&longitude=35.85&"
        "hourly=temperature_2m,wind_speed_10m,relative_humidity_2m&"
        "timezone=auto&forecast_days=3"
    )

    print()
    print("Fetching weather data from Open-Meteo...")

    try:
        req = requests.get(url, timeout=10)
        req.raise_for_status()
        data = req.json()
    except requests.RequestException as error:
        print(f"Error: Could not fetch weather data: {error}")
        sys.exit(1)
    except ValueError:
        print("Error: API response is not valid JSON")
        sys.exit(1)

    if not check_hourly(data):
        print("Error: Missing hourly data")
        sys.exit(1)

    hourly = pd.DataFrame(data["hourly"])
    hourly["time"] = pd.to_datetime(hourly["time"])

    print("Weather data received successfully.")
    print(f"Processing {len(hourly)} data points...")

    temperature = np.array(hourly["temperature_2m"], dtype=float)
    wind = np.array(hourly["wind_speed_10m"], dtype=float)
    humidity = np.array(hourly["relative_humidity_2m"], dtype=float)

    min_tmp = np.min(temperature)
    avg_tmp = np.mean(temperature)
    max_tmp = np.max(temperature)

    avg_wind = np.mean(wind)
    avg_humidity = np.mean(humidity)

    print()
    print(f"Average temperature: {avg_tmp:.2f} C")
    print(f"Minimum temperature: {min_tmp:.2f} C")
    print(f"Maximum temperature: {max_tmp:.2f} C")
    print(f"Average wind speed: {avg_wind:.2f} km/h")
    print(f"Average humidity: {avg_humidity:.2f}%")

    chart_data = hourly.head(24).copy()
    day_label = chart_data["time"].dt.strftime("%Y-%m-%d").iloc[0]
    time_labels = chart_data["time"].dt.strftime("%H:%M")

    print()
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, chart_data["temperature_2m"])
    plt.title(f"Irbid Hourly Temperature Forecast ({day_label})")
    plt.xlabel("Time")
    plt.ylabel("Temperature (C)")
    plt.xticks(time_labels[::2], rotation=45)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
