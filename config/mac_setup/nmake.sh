#!/usr/bin/env bash

#
# To make a Mac app: https://mathiasbynens.be/notes/shell-script-mac-apps
#

#
# Hints for making a MacOS app bundle
# - https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html#//apple_ref/doc/uid/10000123i-CH101-SW19
# - https://stackoverflow.com/questions/1596945/building-osx-app-bundle
# - https://medium.com/@mattholt/packaging-a-go-application-for-macos-f7084b00f6b5
#

file="mac_setup/apply_settings.py"

app_args="--standalone"
compile_args="--remove-output"
debug_args=""
imports_args="--follow-imports"
show_progress_args="--show-progress"

python3 -m nuitka ${imports_args} ${show_progress_args} --python-flag=no_site ${debug_args} ${compile_args}  \
${app_args} ${file}

# Nuitka won't move settings into .dist folder

cp -pvR ./mac_setup/settings apply_settings.dist/

unset file
