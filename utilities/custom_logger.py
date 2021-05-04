import logging

class logGen:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename="F:\\selenium_hybrid_framework\\Logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S:%p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

#logger is not creating
