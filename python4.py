none_magic = Magic(_open(MAGIC_NONE))
none_magic.load()


def _create_filemagic(mime_detected, type_detected):
    mime_type, mime_encoding = mime_detected.split('; ')

    return FileMagic(name=type_detected, mime_type=mime_type,
                     encoding=mime_encoding.replace('charset=', ''))


def detect_from_filename(filename):
    '''Detect mime type, encoding and file type from a filename
    Returns a `FileMagic` namedtuple.
    '''

    return _create_filemagic(mime_magic.file(filename),
                             none_magic.file(filename))


def detect_from_fobj(fobj):
    '''Detect mime type, encoding and file type from file-like object
    Returns a `FileMagic` namedtuple.
    '''

    file_descriptor = fobj.fileno()
    return _create_filemagic(mime_magic.descriptor(file_descriptor),
                             none_magic.descriptor(file_descriptor))


def detect_from_content(byte_content):
    '''Detect mime type, encoding and file type from bytes
    Returns a `FileMagic` namedtuple.
    '''

    return _create_filemagic(mime_magic.buffer(byte_content),
                             none_magic.buffer(byte_content))