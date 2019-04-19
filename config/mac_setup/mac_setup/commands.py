import shlex
import subprocess


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
        return f"{self.command} {self._get} {self._domain} {self._key}"

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
        if value_type in ("-string", "-data", "-float", "-date"):
            self._value_type = value_type
            self._value = value
        elif value_type in ("-int", "-integer"):
            self._value_type = "-int"
            self._value = value
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
        # return list instead for subprocess.run?
        return f"{self._command} {self._get} {self._domain} {self._key} {self._value_type} {self._value}"

    def get(self):
        # add shlex ??
        # try:
        sp = subprocess.run(self.build_get_cmd(), capture_output=True, check=True)
        sp.check_returncode()
        value = sp.stdout.decode("utf-8").rstrip("\n")
        if self._value_type == "-bool":
            value = self.normalize_bool_value(value)
        print(" " * 6, "Value is: {}".format(value))
        return value

    def set(self):
        current_value = self.get()
        # need to fix floating point comparison.  May be trim get() string or convert to floating point...
        if current_value != self._value:
            # subprocess.run(shlex(self.build_set_cmd))
            print("would change to {}".format(self._value))
            # try
            # logging
            # if command or shell or sudo
