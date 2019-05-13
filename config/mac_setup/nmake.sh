#!/usr/bin/env bash

file="mac_setup/apply_settings.py"

python3 -m nuitka --follow-imports --show-progress --python-flag=no_site --remove-output ${file} --standalone

# Nuitka won't move settings into .dist folder

cp -pvR ./mac_setup/settings apply_settings.dist/
