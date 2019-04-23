import shlex
from functools import partial
from subprocess import run


class Cmd:
    """
    Base class definition for all preferences and settings.
    """

    def __init__(self):
        self._description = None
        self._command = None
        self._set = None
        self._get = None

    # def __repr__(self):
    #     return (
    #         f"{self.method}"  # figure out syntax and add text
    #         f"{self.__class__.__name__}("
    #         f"{self._description!r})"
    #     )

    def build_set_cmd(self):
        raise NotImplementedError(
            "  Oops: method build_set_cmd needs to be implemented"
        )

    def build_get_cmd(self):
        raise NotImplementedError(
            "  Oops: method build_get_cmd needs to be implemented"
        )

    # Need better name since an OS call is made for get as well as set_value
    # change_value, execute_change, ...
    def execute_cmd(self, cmd):
        print("  ** ToDo: implement execute_cmd()! **")
        # if !not dry_run
        #   subprocess.run(shlex(cmd))
        #   call logger
        # else
        #   print nice message to stdout


class Defaults_Cmd(Cmd):
    """For 'defaults' command settings."""

    _timeout = 30  # seconds
    run_subprocess = partial(run, capture_output=True, check=True)

    def __init__(self, domain, key, value_type, value, description):
        """Create a new instance of a defaults preference.
        Must provide a domain, domain key and value.
        """
        super().__init__()
        self._description = description
        self._command = "defaults"
        self._set = "write"
        self._get = "read"
        self._domain = domain
        self._key = key
        self.set_value(value_type, value)

    # def __repr__(self):
    #     raise NotImplementedError("__repr__ is not implemented yet")

    def __str__(self):
        return f"{self._command} {self._get} {self._domain} {self._key}"

    def __eq__(self, other):
        raise NotImplementedError("__eq__ is not implemented yet")
        pass

    def normalize_bool_value(self, bool_value):
        if bool_value.upper() in ("0", "NO", "FALSE"):
            return "0"
        elif bool_value.upper() in ("1", "TRUE", "YES"):
            return "1"
        else:
            raise ValueError("{} is an invalid -boolean value".format(bool_value))

    def set_value(self, value_type, value):
        # defaults man page lists types as:
        #   -string, -data, -int[eger], -float, -bool[ean], -date, -array-add, -dict, -dict-add
        # Normalize boolean values to "0" or "1" to match values returned by 'defaults read'.
        if value_type in ("-string", "-data", "-date"):
            self._value_type = value_type
            self._value = value
        elif value_type in ("-int", "-integer"):
            self._value_type = "-int"
            self._value = value
        elif value_type == "-float":
            self._value_type = value_type
            self._value = value
            if self._value[0] == ".":
                # Add leading 0 before decimal point if missing
                self._value = "0" + self._value
        elif value_type in ("-bool", "-boolean"):
            self._value_type = "-bool"
            self._value = self.normalize_bool_value(value)
        elif value_type in ("-date", "-array-add", "-dict", "-dict-add"):
            raise NotImplementedError(
                "{} type processing is not implemented".format(value_type)
            )
        else:
            raise TypeError("{} is not a valid type".format(value_type))

    def build_get_cmd(self):
        """The actual defaults command string to execute"""

        return [self._command, self._get, self._domain, self._key]

    def build_set_cmd(self):
        """The actual defaults command string to execute"""
        return [
            self._command,
            self._set,
            self._domain,
            self._key,
            self._value_type,
            self._value,
        ]

    def get(self):
        """Caller catches exception."""
        # add shlex ??
        sp = Defaults_Cmd.run_subprocess(self.build_get_cmd())
        sp.check_returncode()
        value = sp.stdout.decode("utf-8").rstrip("\n")
        if self._value_type == "-bool":
            value = self.normalize_bool_value(value)
        elif self._value_type == "-float":
            value = value[0 : len(self._value)]
        # print(" " * 6, "Value is: {}".format(value))
        return value

    def set(self, quiet=False, dry_run=False):
        current_value = self.get()
        if current_value != self._value:
            if not dry_run:
                sp = Defaults_Cmd.run_subprocess(self.build_set_cmd())
                sp.check_returncode()
            if not quiet:
                print(
                    " " * 6,
                    "{} | {}: New value: {} Old value: {}".format(
                        self._domain, self._key, self._value, current_value
                    ),
                )
            elif dry_run:
                print(
                    " " * 4,
                    "{} | {} would be changed from to {} from {}".format(
                        self._domain, self._key, self._value, current_value
                    ),
                )
            # Add logging

    def describe(self):
        print(self._domain, self._key, self._value_type, self._value)
        print(" " * 4, self._description)
        print()


# for sudo, beware the exception trace.
# See https://alexwlchan.net/2018/05/beware-logged-errors/
# try:
#     subprocess.check_call(sensitive_command)
# except subprocess.CalledProcessError:
#     raise RuntimeError("The sensitive command failed!") from None
