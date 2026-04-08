def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("hi")
    elif operation_number == 1:
        8 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "42" + 42


def test_error_types() -> None:
    for i in range(4):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as v:
            print(f"Caught ValueError: {v}")
        except ZeroDivisionError as z:
            print(f"Caught ZeroDivisionError: {z}")
        except (FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")

    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
