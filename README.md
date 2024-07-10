# 音声変換

## 概要
YouTubeの動画を音声ファイルに変換するプログラム

## 事前準備

### csvファイルの用意
<b>csvファイルのフォーマット</b>
```
YouTubeリンク, 出力ファイル名
https://example.com, サンプルファイル
```

<b>csvファイルの配置場所</b>
`data`フォルダ配下

## 拡張子設定
`settings.py`の`OUTPUT_FORMAT`を変換したい音声の拡張子にする
例
```
OUTPUT_FORMAT = 'mp3'
```

## インプット設定
`settings.py`の`INPUT_LINK_DATA`を読み込ませたいファイルパスにする
例
```
INPUT_LINK_DATA = 'data/video_info_list.csv'
```

## アウトプット設定
`settings.py`の`OUTPUT_DIRECTORY`を出力させたいファイルパスにする

例
```
OUTPUT_DIRECTORY = f'/Users/chiroru/Downloads/EDM/{now.strftime("%Y%m%d%H%M")}_変換音声'
```

## 実行コマンド
```
python main.py
```

## 実行後
指定したファイルパスに変換された音声が出力されています
