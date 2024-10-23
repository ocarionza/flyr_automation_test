import logging

def get_logger():
    """Configura el logger para el proyecto."""
    logger = logging.getLogger("SeleniumProject")
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
