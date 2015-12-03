# coding: utf-8

'''
Python bindings for libmagic
'''

import ctypes

from collections import namedtuple

from ctypes import *
from ctypes.util import find_library


def _init():
    """
    Loads the shared library through ctypes and returns a library
    L{ctypes.CDLL} instance
    """
    return ctypes.cdll.LoadLibrary(find_library('magic'))

_libraries = {}
_libraries['magic'] = _init()

# Flag constants for open and setflags
MAGIC_NONE = NONE = 0
MAGIC_DEBUG = DEBUG = 1
MAGIC_SYMLINK = SYMLINK = 2
MAGIC_COMPRESS = COMPRESS = 4
MAGIC_DEVICES = DEVICES = 8
MAGIC_MIME_TYPE = MIME_TYPE = 16
MAGIC_CONTINUE = CONTINUE = 32
MAGIC_CHECK = CHECK = 64
MAGIC_PRESERVE_ATIME = PRESERVE_ATIME = 128
MAGIC_RAW = RAW = 256
MAGIC_ERROR = ERROR = 512
MAGIC_MIME_ENCODING = MIME_ENCODING = 1024
MAGIC_MIME = MIME = 1040  # MIME_TYPE + MIME_ENCODING
MAGIC_APPLE = APPLE = 2048

MAGIC_NO_CHECK_COMPRESS = NO_CHECK_COMPRESS = 4096
MAGIC_NO_CHECK_TAR = NO_CHECK_TAR = 8192
MAGIC_NO_CHECK_SOFT = NO_CHECK_SOFT = 16384
MAGIC_NO_CHECK_APPTYPE = NO_CHECK_APPTYPE = 32768
MAGIC_NO_CHECK_ELF = NO_CHECK_ELF = 65536
MAGIC_NO_CHECK_TEXT = NO_CHECK_TEXT = 131072
MAGIC_NO_CHECK_CDF = NO_CHECK_CDF = 262144
MAGIC_NO_CHECK_TOKENS = NO_CHECK_TOKENS = 1048576
MAGIC_NO_CHECK_ENCODING = NO_CHECK_ENCODING = 2097152

MAGIC_NO_CHECK_BUILTIN = NO_CHECK_BUILTIN = 4173824

FileMagic = namedtuple('FileMagic', ('mime_type', 'encoding', 'name'))


class magic_set(Structure):
    pass
magic_set._fields_ = []
magic_t = POINTER(magic_set)

_open = _libraries['magic'].magic_open
_open.restype = magic_t
_open.argtypes = [c_int]

_close = _libraries['magic'].magic_close
_close.restype = None
_close.argtypes = [magic_t]

_file = _libraries['magic'].magic_file
_file.restype = c_char_p
_file.argtypes = [magic_t, c_char_p]

_descriptor = _libraries['magic'].magic_descriptor
_descriptor.restype = c_char_p
_descriptor.argtypes = [magic_t, c_int]

_buffer = _libraries['magic'].magic_buffer
_buffer.restype = c_char_p
_buffer.argtypes = [magic_t, c_void_p, c_size_t]

_error = _libraries['magic'].magic_error
_error.restype = c_char_p
_error.argtypes = [magic_t]

_setflags = _libraries['magic'].magic_setflags
_setflags.restype = c_int
_setflags.argtypes = [magic_t, c_int]

_load = _libraries['magic'].magic_load
_load.restype = c_int
_load.argtypes = [magic_t, c_char_p]

_compile = _libraries['magic'].magic_compile
_compile.restype = c_int
_compile.argtypes = [magic_t, c_char_p]

_check = _libraries['magic'].magic_check
_check.restype = c_int
_check.argtypes = [magic_t, c_char_p]

_list = _libraries['magic'].magic_list
_list.restype = c_int
_list.argtypes = [magic_t, c_char_p]

_errno = _libraries['magic'].magic_errno
_errno.restype = c_int
_errno.argtypes = [magic_t]


class Magic(object):
    def __init__(self, ms):
        self._magic_t = ms

    def close(self):
        """
        Closes the magic database and deallocates any resources used.