# test = {'group': 'general',
#         'type': 'user', # [user | system]
#         'method': 'command', # [command | shell]
#         'description': 'The keyboard react faster to keystrokes (not equally useful for everyone)',
#         'command': 'defaults',
#         'domain_key': 'NSGlobalDomain KeyRepeat',
#         'preferred_value': '-int 0',
#         'set': 'write',
#         'get': 'read',
#         'os_v_min': None, 'os_v_max': None
#         }
#import dglogger
import shlex
import subprocess

class cmd:
    """
    Base class definition for all preferences and settings.
    """

    def __init__(self):
        self.group = 'general'
        self.type = 'user'
        self.method = 'command'
        self.description = None
        self.source = None
        self.os_min = None
        self.os_max = None

    def __repr__(self):
        return (f'{self.type}, {self.group}, {self.method}' # figure out syntax and add text 
                f'{self.__class__.__name__}('
                f'{self.group!r}, {self.description!r})')

    def os_set_cmd(self, cmd):
        # try
        # logging
        # if command or shell or sudo
        subprocess.run(shlex(cmd))


class defaults_cmd(cmd):
    """For preferences set with 'defaults' command"""

    def __init__(self, description, source):
        """Create a new instance of a defaults preference.
        Must provide a domain key and value.
        """
        super().__init__()
        self.description = description
        self.source = source
        self.command = 'defaults'
        self.set = 'write'
        self.get = 'read'
        try:
            ss = source.split()
            self.domain_key = ss[2] + " " + ss[3]
            self.preferred_value = ss[4] + " " + ss[5]
        except IndexError:
            dglogger.log_warning("Expecting domain key and value for: " + self.source)
#            raise ValueError
#            self.__del__()


    def os_set_cmd(self):
        """The actual defaults command string to execute"""

        c = self.command + self.set + self.domain_key + self.preferred_value
        super().os_set_cmd(self, c)


class shell_cmd(cmd):
    """For shell commands (sh or bash)"""

    def __init__(self, description, source):
        """Create a shell command"""
        super().__init__()
        self.method = 'shell'
        self.description = description
        self.source = source
        self.command = " ".join(shlex(self.source))

    def os_set_cmd(self):
        print('Under development: ', self.command)