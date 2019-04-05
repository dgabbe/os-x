from csv import DictReader, register_dialect
from os.path import dirname, join

register_dialect("comma-space", delimiter=",", skipinitialspace=True)
with open(join(dirname(__file__), "settings/defaults.csv"), newline="") as csvfile:
    reader = DictReader(csvfile, dialect="comma-space")
    for row in reader:
        print(row)
