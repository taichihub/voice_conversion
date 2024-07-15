from datetime import datetime
now = datetime.now()

# 変換音声拡張子
OUTPUT_FORMAT = 'mp3'

# 入力リンクデータ
INPUT_LINK_DATA = 'data/music_list.csv'

# 出力先ディレクトリ
OUTPUT_DIRECTORY = f'/Users/kawasakitakuma/Downloads/musics/{now.strftime("%Y%m%d%H%M")}_変換音声'
