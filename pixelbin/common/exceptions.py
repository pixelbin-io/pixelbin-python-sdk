"""Python code/pixelbin/common/exceptions.py."""


class PixelbinInvalidCredentialError(Exception):
    """Invalid credential exception."""
    def __init__(self, message="Invalid Credentials"):
        """Initialize function __init__."""
        super(PixelbinInvalidCredentialError, self).__init__(message)


class RequiredParametersError(Exception):
    """Invalid credential exception."""
    def __init__(self, message="Required Parameters not present"):
        """Initialize function __init__."""
        super(RequiredParametersError, self).__init__(message)
        
        
class PixelbinOAuthCodeError(Exception):
    """PB OAuth Exception."""
    def __init__(self, message=""):
        """Initialize function __init__."""
        super(PixelbinOAuthCodeError, self).__init__(message)
