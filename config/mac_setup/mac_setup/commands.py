import shlex
import subprocess


class Cmd:
    """
    Base class definition for all preferences and settings.
    """

    def __init__(self):
        self.description = None
        self.command = None
        self.set = None
        self.get = None

    def __repr__(self):
        return (
            f"{self.method}"  # figure out syntax and add text
            f"{self.__class__.__name__}("
            f"{self.description!r})"
        )

    def set_cmd(self):
        raise NotImplementedError("  Oops: method set_cmd needs to be implemented")

    def get_cmd(self):
        raise NotImplementedError("  Oops: method get_cmd needs to be implemented")

    # Need better name since an OS call is made for get as well as set
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
        self.description = description
        self.command = "defaults"
        self.set = "write"
        self.get = "read"
        self.domain = domain
        self.key = key
        self.validate_value(value_type, value)

    def __repr__(self):
        raise NotImplementedError("__repr__ is not implemented yet")

    def __str__(self):
        raise NotImplementedError("__str__ is not implemented yet")

    def __eq__(self, other):
        raise NotImplementedError("__eq__ is not implemented yet")
        pass

    def normalize_bool_value(self, bool_value):
        if bool_value.upper() in ("0", "NO", "FALSE"):
            "0"
        elif bool_value.upper() in ("1", "TRUE", "YES"):
            "1"
        else:
            raise ValueError("{} is an invalid -boolean value".format(bool_value))

    def validate_value(self, value_type, value):
        # defaults man page lists types as:
        #   -string, -data, -int[eger], -float, -bool[ean], -date, -array-add, -dict, -dict-add
        # Normalize boolean values to "0" or "1" to match values returned by 'defaults read'.
        if value_type in ("-string", "-data", "-float", "-date"):
            self.value_type = value_type
        elif value_type in ("-int", "-integer"):
            self.value_type = "-int"
        elif value_type in ("-bool", "-boolean"):
            self.value_type = "-bool"
            self.value = self.normalize_bool_value(value)
        elif value_type in ("-date", "-array-add", "-dict", "-dict-add"):
            raise NotImplementedError(
                "{} type processing is not implemented".format(value_type)
            )
        else:
            raise TypeError("{} is not a valid type".format(value_type))

    def get_cmd(self):
        """The actual defaults command string to execute"""

        c = f"{self.command} {self.get} {self.domain} {self.key}"
        print(c)

    def set_cmd(self):
        """The actual defaults command string to execute"""

        c = f"{self.command} {self.get} {self.domain} {self.key} {self.value_type} {self.value}"
        print(c)

    def get(self):
        # do I get the value back?
        subprocess.run(shlex(cmd))

    def set(self):
        current_value = self.get()
        if current_value != self.value:
            subprocess.run(shlex(self.set_cmd))
            # try
            # logging
            # if command or shell or sudo
