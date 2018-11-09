#define Python user-defined exceptions

class CLI_Audio_Exception(Exception):
    """Base class for user-defined exceptions"""
    pass

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    """Exception for when a .wav file is not found"""
    pass

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    """Exception for when the screen does not fit the application window"""
    pass


