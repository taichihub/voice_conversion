# 音声変換

## 概要
YouTubeの動画を音声ファイルに変換するプログラム

## 事前準備

### ローカル環境にクローン
```
git clone git@github.com:taichihub/voice_conversion.git
```
(※) クローン後、voice_conversionディレクトリに移動する

### pipenvをインストール
```
pip install pipenv
```

### 環境構築
pipfile, pipfile.lockの情報をもとに環境構築される
```
pipenv install
```

### 仮想環境に入る
```
pipenv shell
```

### csvファイルの用意
csvファイルのフォーマット
```
YouTubeリンク,出力ファイル名
https://example1.com,サンプルファイル1
https://example2.com,サンプルファイル2
https://example3.com,サンプルファイル3
.....
```

csvファイルの配置場所<br>
`data`フォルダ配下

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
INPUT_LINK_DATA = 'data/video_info_list.csv'
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
