import logging.handlers
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="Logs/Quantuvos.log", format='%(asctime)s - %(message)s', filemode='w')
        rotate_file= logging.handlers.RotatingFileHandler(
            "Logs/Quantuvoslog.log", maxBytes=1824 * 1824 *2, backupCount=3
        )

        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger