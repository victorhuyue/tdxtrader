import logging
import requests

formatter = logging.Formatter('[%(asctime)s]%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def create_logger():

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，并将日志写入文件
    file_handler = logging.FileHandler('my_log_file.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


class WeChatHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log_entry = self.format(record)
        payload = {
            "msgtype": "text",
            "text": {
                "content": log_entry
            }
        }
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send log to WeChat: {e}")

def add_wechat_handler(logger, wechat_webhook_url):

    # 创建企业微信处理器，并将日志发送到企业微信
    wechat_handler = WeChatHandler(wechat_webhook_url)
    wechat_handler.setLevel(logging.INFO)
    wechat_handler.setFormatter(formatter)
    logger.addHandler(wechat_handler)


logger = create_logger()
