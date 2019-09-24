#! /usr/bin/env bash

# think about moving to bin for global access
pipreqs --print . --ignore _untracked,app,macos_settings.dist,nuitka,bin
