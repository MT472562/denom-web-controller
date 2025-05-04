# Denon AVR-Series WEBコントロールアプリ

このアプリケーションは、Denon AVR-Series AVレシーバーをWebブラウザから簡単に操作できるようにするFlaskベースのWebアプリです。本来PC上のWEBUIからでは変更できない音量の操作をできるようにすることが目的です。

## 特徴
* 電源のON/OFF操作
* ミュート/ミュート解除
* 音量スライダーによるコントロール
* 本体設定画面へのリンク

## 前提条件
* Python 3.x
* Flask
* Denon AVRシリーズ（同一ネットワーク上にあること）（IPアドレスを固定することを推奨します）
  [DHCPを無効にする方法](https://support-jp.denon.com/app/answers/detail/a_id/19342/related/1)

## インストールと実行
```bash
# 必要なパッケージをインストール
pip install Flask
# アプリケーションの起動
python main.py
```

## 設定について
実際のIPアドレスはmain.pyにある設定部分を変更してください。
[AVRが接続されているネットワークのSSIDとIPアドレスを見つける方法](https://support-jp.denon.com/app/answers/detail/a_id/19304/)

main.pyの中に最大値や初期値などを設定する項目があります。適時変更してください。

音量スライダー設定：
* 最大音量値（vol_max）：スライダーで設定できる最大の音量です。初期設定では 60 に設定されています。
* 最小音量値（vol_min）：スライダーで設定できる最小の音量です。初期設定では 0 に設定されています。
* 初期音量値（vol_default）：ページロード時に表示されるデフォルトの音量値です。初期設定では 30 に設定されています。

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
* 本体設定（https://{AMP_IP}:10443/）へのボタンリンク

## 注意事項
* コマンド送信にはDenon AVR-シリーズのAPI（ポート8080）を使用しています。
* 実際のIPアドレスはmain.pyにある設定部分を変更してください。

## ライセンス
MIT License

## 作者
* まぎらわしぃ
