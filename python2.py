rrno.argtypes = [magic_t]


class Magic(object):
    def __init__(self, ms):
        self._magic_t = ms

    def close(self):
        """
        Closes the magic database and deallocates any resources used.
        """
        _close(self._magic_t)

    def file(self, filename):
        """
        Returns a textual description of the contents of the argument passed
        as a filename or None if an error occurred and the MAGIC_ERROR flag
        is set.  A call to errno() will return the numeric error code.
        """
        if isinstance(filename, bytes):
            bi = filename
        else:
            bi = bytes(filename, 'utf-8')
        r = _file(self._magic_t, bi)
        if isinstance(r, str):
            return r
        else:
            return str(r, 'utf-8')

    def descriptor(self, fd):
        """
        Like the file method, but the argument is a file descriptor.
        """
        return _descriptor(self._magic_t, fd)

    def buffer(self, buf):
        """
        Returns a textual description of the contents of the argument passed
        as a buffer or None if an error occurred and the MAGIC_ERROR flag
        is set. A call to errno() will return the numeric error code.
        """