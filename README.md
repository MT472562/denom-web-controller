# Denon AVR-Series　WEB　Control App

このアプリケーションは、Denon AVR-X1600H AVレシーバーをWebブラウザから簡単に操作できるようにするFlaskベースのWebアプリです。

本来PC上のWEBUIからでは変更できない音量の操作をできるようにすることが目的です

## 特徴

* 電源のON/OFF操作
* ミュート/ミュート解除
* 音量スライダーによるコントロール
* 本体設定画面へのリンク

## 前提条件

* Python 3.x
* Flask
* Denon AVRシリーズ（同一ネットワーク上にあること）

## インストールと実行

```bash
# 必要なパッケージをインストール
pip install Flask

# アプリケーションの起動
python main.py
```

## ファイル構成

```
project/
├── main.py            # Flaskアプリケーション本体
└── templates/
    └── index.html    # コントロール画面
```

## Webページ構成

* 電源コントロール（PWON / PWSTANDBY）
* ミュートコントロール（MUON / MUOFF）
* 音量コントロールスライダー（MVxx）
* 本体設定（https://{AMP_IP}:10443/）へのボタンリンク)

## 注意事項

* 音量値は0〜60の範囲で調整できます。
* コマンド送信にはDenon AVR-シリーズのAPI（ポート8080）を使用しています。
* 実際のIPアドレスはmain.pyにある設定部分を変更してください

## ライセンス

MIT License

## 作者

*　まぎらわしぃ
