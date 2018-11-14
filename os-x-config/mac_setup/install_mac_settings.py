#! /usr/bin/env python3
"""
Set user settings to optimize performance, Finder and windowing features, and automate standard preference
settings.

While this is an Apple specific script, it doesn't check to see if it's executing on a Mac.
"""

import argparse
import commands
import getpass
import grp
import os
#import pexpect
import platform
import re
import shlex
import subprocess
import sys
# Also read https://airbrake.io/blog/python-exception-handling/importerror-and-modulenotfounderror
sys.path.insert(0, '/Users/dgabbe/_git/_python/dglogger')

def is_admin():
    """Check to see if the user belongs to the 'admin' group.

    :return: boolean
    """
    return os.getlogin() in grp.getgrnam('admin').gr_mem


def is_executable(tweak_group, groups, is_admin = is_admin()):
    """Determines if the tweak should be executed.

    :param tweak_group: tweak's group key value.
    :param groups: groups specified on the command line.
    :param is_admin: True if user belongs to 'admn' group.
    :return boolean
    """
    # return True # for testing
    if groups is None and tweak_group != 'sudo':
        return True
    if groups is None and tweak_group == 'sudo' and is_admin:
        return True
    if groups is not None and tweak_group in groups and tweak_group != 'sudo':
        return True
    if groups is not None and tweak_group in groups and tweak_group == 'sudo' and is_admin:
        return True
    return False


def os_supported(min_v, max_v):
    """Checks to see if the preference is supported on your version of the Mac OS.
    NB: 10.9 is represented in the tweaks.py file as 10.09.

    :param min_v:
    :param max_v:
    :return: boolean
    """
    os_version = re.match('[0-9]+\.[0-9]+', platform.mac_ver()[0]).group(0)  # major.minor
    return not (os_version < str(min_v) or (max_v is not None and os_version > str(max_v)))


def run_batch_mode(settings, args):
    for s in settings:
        run_command(s.os_set_cmd())


def run_command(cmd):
    try:
        subprocess.run(shlex.split(cmd), shell=False, timeout=60, check=True)
        dglogger.log_info(str(cmd))
    except subprocess.CalledProcessError as e:
        dglogger.log_error(str(e))
    except subprocess.TimeoutExpired as e:
        dglogger.log_error(e)
    except OSError as e:
        dglogger.log_error(e)
    except KeyError as e:
        dglogger.log_error(e)
    except TypeError as e:
        dglogger.log_error(e)


def run_interactive_mode():
    print("Interactive not implemented")


def run_list_mode(indent = '    '):
    """helper function to print summary info from the tweaks list.

    :global arg.list: replies on global results from parser.
    :param indent: number of spaces to indent. Defaults to 4.
    :return:
    """
    print("--list: " + str(args.list))

    if args.list == 'a' or args.list == 'all' or args.list == 'g' or args.list == 'groups':
        grp = set()
        for s in settings.settings:
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


def main():
    try:
        import dglogger
    except ModuleNotFoundError as e:
        print('...Logging unavailable. Continuing.')

    try:
        log_file = dglogger.log_config()
        dglogger.log_start()
    except Exception:
        None

    parser = argparse.ArgumentParser(
        description="""install_mac_settings changes user and global settings to improve performance, security,
    and convenience. Results logged to a file."""
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--mode", choices=['b', 'batch', 'i', 'interactive'],
                   action = 'store', default = 'batch',
                   help='Run interactively to confirm each change.')
    group.add_argument('--list', choices = ['all', 'a', 'groups', 'g', 'descriptions', 'd'],
                   action = 'store',
                   help='Print lists of the groups and set commands. Silently ignores --groups.')
    parser.add_argument('--groups', type = str, nargs='+',
                    help='Select a subset of settings to execute')
    args = parser.parse_args()

    try:
        import settings
        if (len(settings) ==0): raise ValueError('settings has no commands to process.')
    except ImportError as e:
        try:
            dglogger.log_error(e)
            dglogger.log_end(log_file)
        except Exception:
            None
        sys.exit(1)

    # Build data structure to process
    settings = []
    for s in settings.settings:
        try:
            settings.append(new_command) # blah blash
        except Exception as e:
            print(e)

    if args.list is not None:
        run_list_mode()
        sys.exit(0)
    elif args.mode == 'batch' or args.mode == 'b':
        run_batch_mode(settings.settings, args)
    elif args.mode == 'interactive' or args.mode == 'i':
        run_interactive_mode()

    dglogger.log_end(log_file)


if __name__ == '__main__':
    main()
else:
    print("WARNING: Was not expecting to be imported. Exiting.")

# regex to replace i and b for mode - code or argsparse fiddling - probably can do in argparse
# pswd = getpass.getpass()
# getpass.getuser() for user name - check this code, installer.py & dot-profile, rpr-3-sort-a-diofile.site, home-profile
# # Sorting dictionaries: https://stackoverflow.com/questions/20944483/pythonct-by-its-values/20948781?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# Sorting dictionaries: https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
# Asking for a password: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password
# --list output to less or more for pagination
