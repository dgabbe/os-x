# python3 -m nuitka --follow-imports --show-progress --python-flag=no_site --remove-output  main.py --standalone

from mac_setup.apply_settings import main, printerr

if __name__ == "__main__":
    main()
else:
    printerr("** Did not plan on being imported **")

