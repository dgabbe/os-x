SHELL := /usr/bin/env bash

all:
	@echo "all is $$0"

# Reference:
#   - https://www.gnu.org/software/make/manual/html_node/

# sample rule
foo.o : foo.c defs.h       # module for twiddling the frobs
        cc -c -g foo.c

# sample commands
python3 -m nuitka ... -m mac_setup.apply_settings
 python3 -m nuitka --follow-imports --show-progress --python-flag=no_site --remove-output link-installer.py --standalone

# switches for nuitka3
#     --output-dir=DIRECTORY
# --remove-output
# --show-modules
# --show-progress
# --follow-imports - verify still should use.
#
# --standalone
# --python-flag=no_site
