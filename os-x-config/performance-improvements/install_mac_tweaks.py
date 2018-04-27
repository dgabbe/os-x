#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import re
import subprocess

# get log file stuff from installer.py

# args: -mode = [b(atch) | i(nteractive)]
# args: -group = various groups
# args: -help

# check for tweaks before importing - use try/catch instead of if/else?
import tweaks

mode = 'batch'
os_version = re.match('[0-9]+\.[0-9]+', platform.mac_ver()[0]).group(0) # major.minor

for t in tweaks.tweaks {
  if (mode == 'batch' && t['group'] != 'sudo' &&
    os_version >= str(t['os_v_min']) &&
    (t['os_v_max'] is None || os_version <= str(t['os_v_max']))):
    try:
      run(t['command'], timeout = 60, check = True)
      # log stuff here
    except CalledProcessError as e:
      print("Command failed:", e, file=sys.stderr)
    except TimeoutExpired as e:
      print("Timeout:", e, file=sys.stderr)
    except OSError as e:
      print("execution flopped:", e, file=sys.stderr)
  else:
    # log skipping message because privs needed or version not supported
}

