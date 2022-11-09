# Coded By: Tom Sumner
# Date: 09-11-2022
# Github: Tom-Sumner / https://github.com/Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.

"""\
Simplified logging module for easy use and setup.\n
Logging Types:\n
1. Error
2. Success
3. Warning
4. Info
5. Debug\n
EG:
```
from simplelogging import Logger
logger = Logger(print=True)
logger.info("This is information!")
```
"""

from datetime import date, datetime

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")[:-3]

class Logger:
    """
    Structure variables are: '__date__', '__level__', '__msg__'
    print: True / False: Whether or not to print logs to terminal.
    """
    def __init__(self, filename:str=None, structure:str=None, print:bool=False) -> None:
        default_structure = "__date__ : __level__ : __msg__"
        self.filename = filename
        self.structure = structure if structure else default_structure
        self.print = print
    
    def __formatMsg(self, msg:str, level:str) -> str:
        """Formats the structure to a writeable message

        Args:
            msg (str): Message passed
            level (str): Level passed

        Returns:
            str: String to be printed or logged
        """
        structure = self.structure
        msg1 = structure.replace("__date__", now)
        msg2 = msg1.replace("__level__", level)
        msg3 = msg2.replace("__msg__", msg)
        return msg3
        
    def __toTerminal(self, msg:str):
        """Uses print() to print the message

        Args:
            msg (str): The message to be printed
        """
        print(msg)
    
    def __toFile(self, msg:str):
        """Writes the message to log file

        Args:
            msg (str): The message to write to log file
        """
        with open(self.filename, "a+") as log:
            log.write(f"{msg}\n")
    
    def __process(self, msg:str, lvl):
        msg = self.__formatMsg(msg, lvl)
        if self.print:
            self.__toTerminal(msg)
        self.__toFile(msg)

    def success(self, msg:str):
        """Success log method

        Args:
            msg (str): Message to be passed
        """
        self.__process(msg, "SUCESS")
    
    def warning(self, msg:str):
        """Warning log method

        Args:
            msg (str): Message to be passed
        """
        self.__process(msg, "WARNING")
    
    def debug(self, msg:str):
        """Debug log method

        Args:
            msg (str): Message to be passed
        """
        self.__process(msg, "DEBUG")
    
    def info(self, msg:str):
        """Info log method

        Args:
            msg (str): Message to be passed
        """
        self.__process(msg, "INFO")
    
    def error(self, msg:str):
        """Error log method

        Args:
            msg (str): Message to be passed
        """
        self.__process(msg, "ERROR")