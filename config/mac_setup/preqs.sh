#! /usr/bin/env bash

# think about moving to bin for global access
pipreqs --print . --ignore _untracked,apply_settings.dist,macos_settings.app,macos_settings.dist,nuitka
