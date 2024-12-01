import time
from tdxtrader.file import clear_file_content
from tdxtrader.trader import create_trader
from tdxtrader.order import create_order, cancel_order

def start(account_id, mini_qmt_path, file_path, buy_sign, sell_sign, buy_event, sell_event, interval=1, cancel_after=None):

    xt_trader, account = create_trader(account_id, mini_qmt_path)

    previous_df = None

    # 启动前清空文件内容
    clear_file_content(file_path)

    while True:
        try:
            previous_df = create_order(xt_trader, account, file_path, previous_df, buy_sign, sell_sign, buy_event, sell_event)
            # 撤单
            cancel_order(xt_trader, account, cancel_after)

        except Exception as e:
            print(f"【发生错误】{e}")
        
        time.sleep(interval)
