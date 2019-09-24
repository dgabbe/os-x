# python3 -m nuitka --follow-imports --show-progress --python-flag=no_site --remove-output  main.py --standalone

from mac_setup.macos_settings import main
from sys import stderr

if __name__ == "__main__":
    main()
else:
    print("** Did not plan on being imported **", file = stderr)
