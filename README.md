# 音声変換

## 概要
YouTubeの動画を音声ファイルに変換するプログラム

## 事前準備

### csvファイルの用意

csvファイルの配置場所<br>
`data`フォルダ配下

data
├── (例)music_list.csv

csvファイルのフォーマット※カンマ(,)と出力ファイル名の間に空白は不必要
```
YouTubeリンク,出力ファイル名
https://example.com,サンプルファイル
```

## 拡張子設定
`settings.py`の`OUTPUT_FORMAT`を変換したい音声の拡張子にする<br>
例
```
OUTPUT_FORMAT = 'mp3'
```

## インプット設定
`settings.py`の`INPUT_LINK_DATA`を読み込ませたいファイルパスにする<br>
例
```
INPUT_LINK_DATA = 'music_list.csv'
```

## アウトプット設定
`settings.py`の`OUTPUT_DIRECTORY`を出力させたいファイルパスにする<br>
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
