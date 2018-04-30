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

indent = '    '

def print_list_arg(indent = indent):
    print("--list: " + str(args.list))

    if args.list == 'a' or args.list == 'all' or args.list == 'g' or args.list == 'groups':
        grp = set()
        for s in tweaks.tweaks:
            grp.add(s['group'])

        print('The groups are:')
        for t in sorted(grp):
            print(indent + t)

    if args.list == 'a' or args.list == 'all' or args.list == 'd' or args.list == 'descriptions':
        descriptions = set()
        for d in tweaks.tweaks:
            descriptions.add(d['group'] + ' | ' + d['description'])

        print('group | description:')
        for t in sorted(descriptions):
            print(indent + t)


# get log file stuff from installer.py

parser = argparse.ArgumentParser(
    description="install_mac_tweaks changes user and global settings to improve performance, security, and convenience. Results logged to a file."
    )
group = parser.add_mutually_exclusive_group()
group.add_argument("--mode", choices=['b', 'batch', 'i', 'interactive'],
                   action = 'store', default = 'batch',
                    help='Run interactively to confirm each change.')
group.add_argument('--list', choices = ['all', 'a', 'groups', 'g', 'desciptions', 'd'],
                   action = 'store',
                    help='Print lists of the groups and set commands. Silently ignores --groups.')
parser.add_argument('--groups', type = str, nargs='+',
                    help='Select a subset of tweaks to execute')
args = parser.parse_args()

mode = args.mode

# if (args.groups is not None):

# https://apple.stackexchange.com/questions/179527/check-if-an-os-x-user-is-an-administrator?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# 'id -Gn uid' to check for privs, wonder if there is something in platform module

try:
    import tweaks
except ImportError as e:
    print("...ImportError:", e, file=sys.stderr)
    # end log
    sys.exit(1)

os_version = re.match('[0-9]+\.[0-9]+', platform.mac_ver()[0]).group(0)  # major.minor

if (args.list is not None):
    print_list_arg()
    sys.exit(0)

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
# regex to replace i and b for mode - code or argsparse fiddling - probably can do in argparse
# pswd = getpass.getpass()
# getpass.getuser() for user name - check this code, installer.py & dot-profile, rpr-3-sort-a-diofile.site, home-profile
# # Sorting dictionaries: https://stackoverflow.com/questions/20944483/pythonct-by-its-values/20948781?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# Sorting dictionaries: https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
# Asking for a password: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password
# Add shlex parsing for safe passing of parameters
# --list output to less or more for pagination
