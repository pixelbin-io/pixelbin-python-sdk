class PixelbinInvalidCredentialError(Exception):
    """Invalid credential exception."""
    def __init__(self, message="Invalid Credentials"):
        """Initialize function __init__."""
        super(PixelbinInvalidCredentialError, self).__init__(message)        

class PixelbinServerResponseError(Exception):
    """Pixelbin Server Response Exception."""
    def __init__(self, message=""):
        """Initialize function __init__."""
        super(PixelbinServerResponseError, self).__init__(message)


class PixelbinInvalidUrlError(Exception):
    """Pixelbin Invalid Url Exception."""
    def __init__(self, message=""):
        """Initialize function __init__."""
        super(PixelbinInvalidUrlError, self).__init__(message)


class PixelbinIllegalArgumentError(Exception):
    """Pixelbin Illegal Argument Exception."""
    def __init__(self, message=""):
        """Initialize function __init__."""
        super(PixelbinIllegalArgumentError, self).__init__(message)