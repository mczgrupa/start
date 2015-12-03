
    def setflags(self, flags):
        """
        Set flags on the magic object which determine how magic checking
        behaves; a bitwise OR of the flags described in libmagic(3), but
        without the MAGIC_ prefix.
        Returns -1 on systems that don't support utime(2) or utimes(2)
        when PRESERVE_ATIME is set.
        """
        return _setflags(self._magic_t, flags)

    def load(self, filename=None):
        """
        Must be called to load entries in the colon separated list of database
        files passed as argument or the default database file if no argument
        before any magic queries can be performed.
        Returns 0 on success and -1 on failure.
        """
        return _load(self._magic_t, filename)

    def compile(self, dbs):
        """
        Compile entries in the colon separated list of database files
        passed as argument or the default database file if no argument.
        Returns 0 on success and -1 on failure.
        The compiled files created are named from the basename(1) of each file
        argument with ".mgc" appended to it.
        """
        return _compile(self._magic_t, dbs)

    def check(self, dbs):
        """
        Check the validity of entries in the colon separated list of
        database files passed as argument or the default database file
        if no argument.
        Returns 0 on success and -1 on failure.
        """
        return _check(self._magic_t, dbs)

    def list(self, dbs):
        """
        Check the validity of entries in the colon separated list of
        database files passed as argument or the default database file
        if no argument.