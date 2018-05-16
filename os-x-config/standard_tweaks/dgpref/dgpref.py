class dgpref:
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
        #subprocess.run(shlex(cmd))
        print('dgpref.set_pref executed')
