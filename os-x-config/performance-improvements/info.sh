#! /usr/bin/env bash

echo 'MacOS:' `sw_vers -productVersion`
echo 'Python:' `python -V`
echo 'which python:' `which python`
echo 'whereis python:' `whereis python`
echo 'which python3:' `which python3`
echo 'privs:' `id -Gn`
