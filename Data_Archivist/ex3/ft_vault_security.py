
def secure_archive(file, action="r", content="") -> tuple[bool, str]:
    try:
        with open(file, action) as f:
            if (action == "w"):
                f.write(content)
                return (True, "Content successfully written to file")
            else:
                return (True, f.read())
    except FileNotFoundError as e:
        return (False, str(e))
    except PermissionError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("why.txt"))

    print("Using ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    bol, cont = secure_archive("m.txt", "r")
    print("Using ’secure_archive’ to write previous content to a new file:")
    if bol:
        print(secure_archive("new.txt", "w", cont))
    else:
        print(False, cont)
