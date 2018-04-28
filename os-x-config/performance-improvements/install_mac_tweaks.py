#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Notes:
#   * Didn't bother to check to see if running on a Mac.
#

import argparse
import os
import platform
import re
import shlex
import subprocess
import sys

# get log file stuff from installer.py

# args: -mode = [b(atch) | i(nteractive)]
# args: -group = various groups
# args: -help

parser = argparse.ArgumentParser(description = 'add description here')
parser.add_argument("--mode", choices=['b', 'batch', 'i', 'interactive'],
                    help = 'Run interactively to confirm each change.')
parser.add_argument('--group', dest = 'groups', help = 'Select a subset of tweaks to execute')
args = parser.parse_args()

#
# Process args
#
if (args.mode is None):
  mode = 'batch'
else:
  mode = 'interactive' # for now - need to match against a regex

if (args.groups is not None):
  print("groups: " + args.groups)

print("mode:  " + mode)

# 'id -Gn uid' to check for privs, wonder if there is something in platform module

# check for tweaks before importing - use try/catch instead of if/else?
import tweaks

os_version = re.match('[0-9]+\.[0-9]+', platform.mac_ver()[0]).group(0) # major.minor

for t in tweaks.tweaks:
  if (os_version < str(t['os_v_min']) or
    (t['os_v_max'] is not None and os_version > str(t['os_v_max']))):
    print("...OS version not supported") # log os version not supported
  elif (mode == 'batch' and t['group'] != 'sudo' and t['group'] != 'test'):
    try:
      subprocess.run(t['set'], shell = True, timeout = 60, check = True)
      print('...' + str(t['set'])) # place holder for logging call
    except subprocess.CalledProcessError as e:
      print("Command failed:", e, file=sys.stderr)
    except subprocess.TimeoutExpired as e:
      print("Timeout:", e, file=sys.stderr)
    except OSError as e:
      print("execution flopped:", e, file=sys.stderr)
    except KeyError as e:
      print("bad dictionary value:", e, file=sys.stderr)
  else:
    pass # log skipping message because privs needed



# How to check for admin or privs on os-x
