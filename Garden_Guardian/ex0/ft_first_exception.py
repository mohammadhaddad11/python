def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return (int(temp_str))


def test_temperature() -> None:
    try:
        print(f"Temperature is now {input_temperature("25")}°C")
        print(f"Temperature is now {input_temperature("abc")}°C")

    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
