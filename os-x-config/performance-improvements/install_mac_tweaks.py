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

parser = argparse.ArgumentParser(
    description="install_mac_tweaks changes user and global settings to improve performance, security, and convenience. Results logged to a file."
    )
group = parser.add_mutually_exclusive_group()
group.add_argument("--mode", choices=['b', 'batch', 'i', 'interactive'],
                   action = 'store', default = 'batch',
                    help='Run interactively to confirm each change.')
group.add_argument('--list', action="store_true",
                    help='Print lists of the groups and set commands')
parser.add_argument('--groups', type = str, nargs='+',
                    help='Select a subset of tweaks to execute')
args = parser.parse_args()

mode = args.mode
#
# Process args
#
# if (args.mode is None):
#     mode = 'batch'
# else:
#     mode = 'interactive'  # for now - need to match against a regex

# if (args.groups is not None):
print("groups: " + str(args.groups))

print("list: ", + args.list)

print("mode:  " + mode)

# https://apple.stackexchange.com/questions/179527/check-if-an-os-x-user-is-an-administrator?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# 'id -Gn uid' to check for privs, wonder if there is something in platform module

# check for tweaks before importing - use try/catch instead of if/else?
import tweaks

os_version = re.match('[0-9]+\.[0-9]+', platform.mac_ver()[0]).group(0)  # major.minor

for t in tweaks.tweaks:
    if (os_version < str(t['os_v_min']) or
            (t['os_v_max'] is not None and os_version > str(t['os_v_max']))):
        print("...OS version not supported")  # log os version not supported
    elif (mode == 'batch' and t['group'] != 'sudo' and t['group'] != 'test'):
        try:
            subprocess.run(t['set'], shell=True, timeout=60, check=True)
            print('...' + str(t['set']))  # place holder for logging call
        except subprocess.CalledProcessError as e:
            print("Command failed:", e, file=sys.stderr)
        except subprocess.TimeoutExpired as e:
            print("Timeout:", e, file=sys.stderr)
        except OSError as e:
            print("execution flopped:", e, file=sys.stderr)
        except KeyError as e:
            print("bad dictionary value:", e, file=sys.stderr)
    else:
        pass  # log skipping message because privs needed

# How to check for admin or privs on os-x
# regex to replace i and b for mode - code or argsparse fiddling
# fix entries w/2 set commands
# pswd = getpass.getpass()
# getpass.getuser() for user name - check this code, installer.py & dot-profile, rprofile.site, home-profile
# Sorting dictionaries: https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values/20948781?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# Sorting dictionaries: https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
# Asking for a password: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password
# Add shlex parsing for safe passing of parameters
