#!/usr/bin/env bash

#
# To make a Mac app: https://mathiasbynens.be/notes/shell-script-mac-apps
#

file="mac_setup/apply_settings.py"

show_progress_args="--show-progress"
imports_args="--follow-imports"
app_args="--standalone"
debug_args=""
compile_args="--remove-output"


python3 -m nuitka ${imports_args} ${show_progress_args} --python-flag=no_site ${debug_args} ${compile_args}  \
${app_args} ${file}

# Nuitka won't move settings into .dist folder

cp -pvR ./mac_setup/settings apply_settings.dist/

unset file
