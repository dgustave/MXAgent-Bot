import logging.handlers
import sys,os


class Logger:
    """
    Just logs data from service pump currently. 
    Currently logs attempted logins, popup special handling from MXA, and the time it took to finish the job. 
    logger = Logger() 
    Example: logger.info("Add Message here and format is %(asctime)s - %(name)s - %(levelname)s - %(message)s' )
    """

    Logger = None
    def __init__(self, logging_service='datapump', enable_notifications=False):
        # Logger setup
        self.Logger = logging.getLogger(logging_service)
        self.Logger.setLevel(logging.DEBUG)
        self.Logger.propagate = False
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # default is "__name__"
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


    def log(self, message, level="info", notification=False):
        ""
        
        if level == "info":
            self.Logger.info(message)
        elif level == "warning":
            self.Logger.warning(message)
        elif level == "error":
            self.Logger.error(message)
        elif level == "debug":
            self.Logger.debug(message)

        if notification and self.NotificationHandler.enabled:
            self.NotificationHandler.send_notification(str(message))

    def info(self, message, notification=False):
        self.log(message, "info", notification)

    def warning(self, message, notification=False):
        self.log(message, "warning", notification)

    def error(self, message, notification=False):
        self.log(message, "error", notification)

    def debug(self, message, notification=False):
        self.log(message, "debug", notification)
