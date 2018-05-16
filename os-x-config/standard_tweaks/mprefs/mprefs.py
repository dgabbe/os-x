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
import shlex
import subprocess

class pref:
    """
    Base class definition for all preferences and tweaks.
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
        return (f'{self.__class__.__name__}('
                f'{self.group!r}, {self.description!r})')

    def set_pref(self, cmd):
        # try
        # logging
        # if command or shell or sudo
        subprocess.run(shlex(cmd))


class defaults_pref(pref):
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
        # parse source for domain key & value!!
        self.domain_key = None
        self.preferred_value = None

    def set_pref(self):
        """fill in later"""

        c = self.command + self.set + self.domain_key + self.preferred_value
        pref.set_pref(self, c)


class shell_pref(pref):
    """For shell commands (sh or bash)"""

    def __init__(self, description, source):
        """Create a shell command"""
        super().__init__()
        self.method = 'shell'
        self.description = description
        self.source = source
        self.command = " ".join(shlex(self.source))

    def set_pref(self, cmd):
        pass  # for now - figure out
