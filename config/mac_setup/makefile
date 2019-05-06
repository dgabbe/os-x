SHELL := /usr/bin/env bash

all:
	@echo "all is $$0"

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
