import abc
import time
import logging
import traceback
from common import common_utility as commonUtil


class AbstractBatch(object, metaclass=abc.ABCMeta):
    """基底バッチクラス
    各バッチクラスは本クラスを継承して作成する。
    """

    def __init__(self, class_name):
        """初期化処理
        ・ロガー設定
        Arguments:
            class_name {string} -- クラス名文字列
        """
        # logger
        self.class_name = class_name
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)5s : %(name)s - [%(funcName)s]  %(message)s")
        self.LOGGER = logging.getLogger(class_name)

    def pre(self):
        """前処理
        """
        self.LOGGER.info("START：" + self.class_name)
        # 処理時間計測用
        self.start_time = time.time()

    def post(self):
        """後処理
        """
        elapse_time = time.time() - self.start_time
        self.LOGGER.info("elapse time：{:.3f}".format(elapse_time) + "[sec]")
        self.LOGGER.info("END：" + self.class_name)

    def execute(self):
        """
        バッチ処理を実行する。
        バッチ処理中に例外が発生した場合はslackへ通知を行う。
        """
        # 前処理
        self.pre()
        try:
            # 本処理
            self.execute_logic()
        except Exception as e:
            self.LOGGER.exception(e)
            # slack通知
            commonUtil.slack_notice(
                "バッチ実行中に例外発生：{}".format(traceback.format_exc()), ":fearful:")
        finally:
            # 後処理
            self.post()

    @abc.abstractmethod
    def execute_logic(self):
        """バッチメイン処理。実際の処理はサブクラスで実装する。 """
