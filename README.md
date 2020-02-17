# Python バッチファイル用テンプレートプロジェクト

私がPythonでバッチを書くときに使うためのプロジェクトテンプレート。

## 概説

[基底バッチクラス](./base/abstractbatch.py)で`ロガー設定`、`バッチ共通前後処理`、`例外処理`を実装するため実際のバッチ処理を行う個々のサブクラスではそれらを実装する必要がなくなります。

`バッチ共通前後処理`はデフォルトで以下の処理を実装しています。

- バッチ実行開始・終了ログ出力
- バッチ処理時間計測

`例外処理`ではデフォルトで以下の処理を実装しています。

- 例外ログ出力
- slack通知

なおサブクラスのバッチ処理内で独自に例外を処理することももちろん可能です。キャッチした例外を再スローしないかぎり基底クラスの例外処理は実行されません。

## 前提

このプロジェクトではパッケージ管理にpipenvを使用しています。

- [pipenv](https://github.com/pypa/pipenv)

※ただしpipenvは必須ではなく、標準のpipでも特に問題はありません。その場合は以下のパッケージをpipでインストールします。

- requests
- python-dotenv

## セットアップ & 実行

**.env ファイル作成**

```
SLACK_WEBHOOK=<your slack webhook url>
```

```Bash
# install package from pipfile.lock
pipenv sync --dev

# activate
pipenv shell

# execute batch
python sample_batch.py
```

## 👀 Author

👤 **K**

- Twitter: [@k_urtica](https://twitter.com/k_urtica)
- Github: [@k-urtica](https://github.com/k-urtica)
