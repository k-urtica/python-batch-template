"""
処理概要
サンプルバッチクラス
"""

from base.abstractbatch import AbstractBatch
import sys
import time


class SampleBatch(AbstractBatch):

    def __init__(self):
        super().__init__(self.__class__.__name__)

    def execute_logic(self):
        """
        サンプルバッチメイン処理
        """
        # 実際のバッチ処理を実装します
        # プライベートメソッド呼び出し
        self.__sample_method()
        # loggerは基底クラスでセットアップ済み
        self.LOGGER.info("サンプルバッチメイン処理")

    def __sample_method(self):
        """
        プライベートメソッド
        """
        time.sleep(1)


if __name__ == "__main__":
    sample_batch = SampleBatch()
    # 実行時は基底クラスのexecuteメソッドをコールします
    sys.exit(sample_batch.execute())
