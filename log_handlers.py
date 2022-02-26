import logging

def get_logger(log_path="/tmp/logger.log"):
    """Sets the logger to log info in terminal and file `log_path`.
    In general, it is useful to have a logger so that every output to the terminal is saved
    in a permanent file. Here we save it to `tmp/<log_file_path>.log`.
    Example:
    ```
    logging.info("Starting training...")'%Y-%m-%d:%H:%M:%S'
    ```
    Args:
        log_path: (string) where to log
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    log_format = '%(asctime)s %(levelname)-4s [%(filename)s-%(funcName)s():%(lineno)d] :: %(message)s'
    date_format = '%Y-%m-%d:%H:%M:%S'
    if not logger.handlers:
        # Logging to a file
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(logging.Formatter(log_format,datefmt=date_format))
        logger.addHandler(file_handler)

        # Logging to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(log_format,datefmt=date_format))
        logger.addHandler(stream_handler)

    return logger
