#! /usr/bin/env python3

# $ python3 -m mac_setup.apply_settings

#
# Resources:
#   - https://developer.apple.com/documentation/foundation/nsuserdefaults
#
#   - http://www.defaults-write.com/10-terminal-commands-to-speed-up-your-mac-in-os-x-el-capitan/
#   - https://gist.github.com/benfrain/7434600
#   - https://gist.github.com/mbinna/2357277
#   - https://github.com/drduh/
#   - https://github.com/mathiasbynens/dotfiles/
#   - https://github.com/mathiasbynens/dotfiles/blob/master/.macos
#   - https://github.com/paulirish/dotfiles
#   - https://github.com/pawelgrzybek/dotfiles/blob/master/setup-macos.sh
#   - https://pawelgrzybek.com/change-macos-user-preferences-via-command-line/
#

from argparse import ArgumentParser
from csv import DictReader, register_dialect
from grp import getgrnam
from os import getlogin
from os.path import dirname, join
from sys import stderr

from mac_setup.commands import Defaults_Cmd


def is_admin():
    """Check to see if the user belongs to the 'admin' group.

    :return: boolean
    """
    return getlogin() in getgrnam("admin").gr_mem


def main():
    parser = ArgumentParser(
        prog="Apply MacOS Settings",
        description="""Tailor MacOS settings for better performance and better default behavior""",
        epilog="""Only settings that need changing need are executed. Changes are logged to <<fill in>>. 
        The format for the csv file is <<fill in later>>""",
    )
    parser.add_argument(
        "-settings",
        choices=["defaults", "shell", "sudo", "all"],
        default="defaults",
        help="Which group of settings to apply.",
    )

    # Change -dryrun & -quiet to be mutually exclusive
    parser.add_argument(
        "-dryrun",
        action="store_true",
        default=False,
        help="Simulate and report the changes, but do not make them.",
    )
    parser.add_argument(
        "-quiet", action="store_true", default=False, help="""Operate in quiet mode."""
    )
    args = parser.parse_args()

    register_dialect("comma-space", delimiter=",", skipinitialspace=True)
    with open(join(dirname(__file__), "settings/defaults.csv"), newline="") as csvfile:
        reader = DictReader(csvfile, dialect="comma-space")
        row_count = sum(1 for row in csvfile)
        print("    Reviewing {} settings...".format(row_count - 1))
        csvfile.seek(0)
        for row in reader:
            # add -quiet support here
            print("  working: {} | {}".format(row["domain"], row["key"]))
            try:
                c = Defaults_Cmd(**row)
            except:
                pass
                # handle TypeError & ValueError


if __name__ == "__main__":
    main()
else:
    print("    ** Did not plan on being imported **", file=stderr)
