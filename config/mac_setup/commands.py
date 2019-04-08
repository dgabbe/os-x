import shlex
import subprocess


class cmd:
    """
    Base class definition for all preferences and settings.
    """

    def __init__(self):
        self.method = "command"
        self.description = None

    def __repr__(self):
        return (
            f"{self.method}"  # figure out syntax and add text
            f"{self.__class__.__name__}("
            f"{self.description!r})"
        )

    def set(self, cmd):
        # try
        # logging
        # if command or shell or sudo
        subprocess.run(shlex(cmd))


class defaults_cmd(cmd):
    """For 'defaults' command settings."""

    def __init__(self, domain, domain_key, value_type, value, description):
        """Create a new instance of a defaults preference.
        Must provide a domain, domain key and value.
        """
        super().__init__()
        self.description = description
        self.command = "defaults"
        self.set = "write"
        self.get = "read"
        self.domain = domain
        self.domain_key = domain_key
        self.value_type = value_type
        self.value = value
        try:
            pass
        except IndexError:
            pass

    #            raise ValueError
    #            self.__del__()

    def convert_bool_type(bool_value):
        if bool_value in ("0", "NO", "FALSE"):
            "0"
        elif bool_value in ("1", "TRUE", "YES"):
            "1"
        else:
            pass
            # raise convert_bool_type error

    def validate_value_type(self):
        # from man page
        # value types are: -string, -data, -int[eger], -float, -bool[ean], -date, -array-add, -dict, -dict-add
        if self.value_type in (
            "-string",
            "-data",
            "-int",
            "-integer",
            "-float",
            "-date",
        ):
            pass
            # just store value
        elif self.value_type in ("-bool", "-boolean"):
            pass
            # convert value into 0 or 1
        elif self.value_type in ("-date", "-array-add", "-dict", "-dict-add"):
            pass
            # raise unsupported exception
        else:
            pass
            # raise bad value type error

    #    def __get__(self, instance, owner):(self):

    def get_cmd(self):
        """The actual defaults command string to retrieve"""

        c = self.command + self.get + self.domain_key
        super().os_set_cmd(self, c)

    def set_cmd(self):
        """The actual defaults command string to execute"""

        c = self.command + self.set + self.domain_key + self.preferred_value
        super().os_set_cmd(self, c)


# class shell_cmd(cmd):
#     """For shell commands (sh or bash)"""
#
#     def __init__(self, description, source):
#         """Create a shell command"""
#         super().__init__()
#         self.method = 'shell'
#         self.description = description
#         self.source = source
#         self.command = " ".join(shlex(self.source))
#
#     def os_set_cmd(self):
#         print('Under development: ', self.command)
