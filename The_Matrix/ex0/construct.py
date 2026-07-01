
import sys
import os
import site

virtualized = False
if sys.prefix != sys.base_prefix:
    virtualized = True

if not virtualized:
    print("MATRIX STATUS: You’re still plugged in")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected")
    print("WARNING: You’re in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("Then run this program again.")

else:
    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)
    env_name = os.path.basename(sys.prefix)
    print("Virtual Environment:", env_name)
    print("Environment Path:", sys.prefix)
    print("SUCCESS: You’re in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    paths = site.getsitepackages()
    for package in paths:
        if "site-packages" in package:
            print(package)
            break
