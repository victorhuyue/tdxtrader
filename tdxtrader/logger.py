import logging
def create_logger():

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，并将日志写入文件
    file_handler = logging.FileHandler('my_log_file.log')
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s]%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = create_logger()
