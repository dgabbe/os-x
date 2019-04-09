#! /usr/bin/env python3

#
# Resources:
#   - https://developer.apple.com/documentation/foundation/nsuserdefaults
#   - https://github.com/mathiasbynens/dotfiles/
#   - https://github.com/paulirish/dotfiles
#

from argparse import ArgumentParser
import commands
from csv import DictReader, register_dialect
from os.path import dirname, join
from sys import exit, stderr


def is_admin():
    """Check to see if the user belongs to the 'admin' group.

    :return: boolean
    """
    return os.getlogin() in grp.getgrnam("admin").gr_mem


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
            print("  working: {} | {}".format(row["domain"], row["key"]))
            c = Defaults_Cmd(**row)


if __name__ == "__main__":
    main()
else:
    print("    ** Did not plan on being imported **", file=stderr)
