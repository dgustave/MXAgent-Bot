import logging.handlers
import sys,os
import inspect


class Logger:
    """
    Example: logger.info("Add Message here and format is %(asctime)s - %(name)s - %(levelname)s - %(message)s' )
    Logging service default is current "<module name>".
    """

    Logger = None
    def __init__(self, logging_service=os.path.splitext(os.path.basename(__file__))[0], enable_notifications=False):
        # Logger setup
        self.Logger = logging.getLogger(logging_service)
        self.Logger.setLevel(logging.DEBUG)
        self.Logger.propagate = False
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # default is "<module name> as "
        self.modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.logpath = f'{self.modpath}/logs/{logging_service}.log'
        fh = logging.FileHandler(self.logpath)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.Logger.addHandler(fh)
        # logging to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.Logger.addHandler(ch) 
    
    @staticmethod
    def __get_call_info():
        """
        Grabs file path, function name, and line number for logs for better debugging and logging. 
        func - Function Name 
        fn - File Name
        ln - Line Number 
        stack[3][?] - Is used to get the current function logger is being used in. 
        stack[?][1-3] : 
        1 - File Path to script. 
        2 - Function Name.
        3 - Line Number Logger was executed.
        """
        stack = inspect.stack()
        # stack[1] gives previous function ('info' in our case)
        # stack[2] gives before previous function and so on

        fn = str(stack[3][1])
        ln = str(stack[3][2])
        func = str(stack[3][3])
        func_info = f"File Path: {fn} - Function Name: {func} - at line {ln}:"
        return func_info


    def log(self, message, level="info", notification=False):
        message = "{} - {}".format(self.__get_call_info(), message)
        if level == "info":
            self.Logger.info(message)
        elif level == "warning":
            self.Logger.warning(message)
        elif level == "error":
            self.Logger.error(message)
        elif level == "debug":
            self.Logger.debug(message)

        # if notification and self.NotificationHandler.enabled:
        #     self.NotificationHandler.send_notification(str(message))

    def info(self, message, notification=False):
        self.log(message, "info", notification)

    def warning(self, message, notification=False):
        self.log(message, "warning", notification)

    def error(self, message, notification=False):
        self.log(message,  "error", notification)

    def debug(self, message, notification=False):
        self.log(message, "debug", notification)
