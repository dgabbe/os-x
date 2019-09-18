#! /usr/bin/env python3

# $ python3 -m mac_setup.apply_settings (from parent directory of this file)

# Build as an exe:
#   cd ~/_git/_os-x/config/mac_setup
#   python3 -m nuitka --follow-imports --show-progress --python-flag=no_site --remove-output mac_setup/apply_settings.py --standalone
# Also see nmake.sh in repo.

#
# To run from the terminal:
#   $ open -a /Applications/Utilities/Terminal.app/Contents/MacOS/Terminal apply_settings --args -h
#
# Resources:
#   - https://developer.apple.com/documentation/foundation/nsuserdefaults
#   - Patrick Wardell's tool https://objective-see.com/products/lockdown.html
#
#   - http://www.defaults-write.com/10-terminal-commands-to-speed-up-your-mac-in-os-x-el-capitan/
#   - https://github.com/kevinSuttle/macOS-Defaults/blob/master/.macos
#   - https://gist.github.com/benfrain/7434600
#   - https://gist.github.com/mbinna/2357277
#   - https://github.com/drduh/
#   - https://github.com/mathiasbynens/dotfiles/
#   - https://github.com/mathiasbynens/dotfiles/blob/master/.macos
#   - https://github.com/paulirish/dotfiles
#   - https://github.com/pawelgrzybek/dotfiles/blob/master/setup-macos.sh
#   - https://pawelgrzybek.com/change-macos-user-preferences-via-command-line/
#   - https://zerotoroot.me/hardening-macos-part-1/
#

from argparse import ArgumentParser
from csv import DictReader, register_dialect
from functools import partial
from grp import getgrnam
from os import getlogin
from os.path import abspath, dirname, join
from subprocess import CalledProcessError, TimeoutExpired
from sys import exit, stderr, path

from mac_setup.commands import Defaults_Cmd

path.extend(["/Users/dgabbe/_git/_python/dglogger"])
import dglogger


def epilogue(describe, dry_run):
    """Complete setup by restarting specific services to pickup changes."""
    if not describe or not dry_run:
        # killall SystemUIServer
        pass


def is_admin():
    """Check to see if the user belongs to the 'admin' group.

    :return: boolean
    """
    return getlogin() in getgrnam("admin").gr_mem


def printq(quiet_arg, *args, **kwargs):
    if not quiet_arg:
        print(*args, **kwargs)


def prologue(describe: object, dry_run: object) -> object:
    if not describe or not dry_run:
        # AppleScript to close System Preferences
        pass


def main():
    printerr(
        "DEBUG: {} parent of settings/".format(dirname(__file__))
    )  # should really be a dglogger call!
    parser = ArgumentParser(
        prog="Apply MacOS Settings",
        description="""Tailor MacOS settings for better performance and default behavior""",
        epilog="""Only settings that need changing need are executed. Changes are logged to <<fill in>>.
        The format for the csv file is <<fill in later>>""",
    )
    parser.add_argument(
        "-settings",
        choices=["defaults", "shell", "sudo", "all"],
        default="defaults",
        help="Which group of settings to apply.",
    )

    verbose_or_silent = parser.add_mutually_exclusive_group()
    verbose_or_silent.add_argument(
        "-dryrun",
        action="store_true",
        default=False,
        help="Report the changes, but do not make them.",
    )
    verbose_or_silent.add_argument(
        "-quiet", action="store_true", default=False, help="""Operate in quiet mode."""
    )

    describe_or_interactive = parser.add_mutually_exclusive_group()
    describe_or_interactive.add_argument(
        "-describe",
        action="store_true",
        default=False,
        help="Display short description for each settings.",
    )
    describe_or_interactive.add_argument(
        "-interactive",
        action="store_true",
        default=False,
        help="Ask user whether to accept each change for each setting.",
    )

    args = parser.parse_args()

    print("    About to optimize some settings for your account.")
    print("    Any changes are displayed on screen and written to a log file. ")
    print("    Use the Console utility to view the log file.")
    # answer = input("Proceed [y|n]? ")
    # if answer == "n": # weak test - replsys.path.extend(['/Users/dgabbe/_git/_python/dglogger'])ace w/better way
    #     exit("... No Change; no problem.")

    prologue(args.describe, args.dryrun)

    if args.dryrun:
        print("Performing a dry run - no changes will be made.")
    csv = "defaults.csv"
    register_dialect("comma-space", delimiter=",", skipinitialspace=True)
    with open(join(abspath(dirname(__file__)), "settings", csv), newline="") as csvfile:
        reader = DictReader(csvfile, dialect="comma-space")
        row_count = sum(1 for row in csvfile)
        print(" " * 2, "{}: Reviewing {} settings...".format(csv, row_count - 1))
        csvfile.seek(0)
        line = 1  # account for header
        for row in reader:
            line += 1
            cursor = row["domain"] + " | " + row["key"]
            try:
                c = Defaults_Cmd(**row)
                if args.describe:
                    c.describe(line_number=line)
                elif args.interactive:
                    raise NotImplementedError
                else:
                    printq(args.quiet, " " * 4, "working: {}".format(cursor))
                    c.set(quiet=args.quiet, dry_run=args.dryrun)
            except (TypeError, ValueError):
                printerr(
                    "Line {}: Domain/key: {}: Check for missing ',' delimiter".format(
                        line, cursor
                    ),
                    sep="",
                )
            except CalledProcessError:
                # figure out what to report
                printerr("Line {}: Called Process Error ...".format(line))
            except TimeoutExpired:
                # figure out what to report
                printerr("Line {}: Timeout Expired...".format(line))
            except NotImplementedError:
                printerr("Standby while more code is written...")

    epilogue(args.describe, args.dryrun)


if __name__ == "__main__":
    main()
else:
    printerr("** Did not plan on being imported **")
