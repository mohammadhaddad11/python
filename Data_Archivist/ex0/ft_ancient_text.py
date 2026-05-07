import sys


def ft_ancient_text() -> None:
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print(f"=== Cyber Archives Recovery ===\nAccessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1], "r")
        print(f"---\n{f.read()}\n---")
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    ft_ancient_text()
