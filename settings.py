from datetime import datetime
now = datetime.now()

# 変換音声拡張子
OUTPUT_FORMAT = 'mp3'

# 入力リンクデータ
INPUT_LINK_DATA = 'data/video_info_list.csv'

# 出力先ディレクトリ
OUTPUT_DIRECTORY = f'/Users/chiroru/Downloads/EDM/{now.strftime("%Y%m%d%H%M")}_変換音声'

# エラーCSV出力ディレクトリ
ERROR_DIRECTORY = f'data/errors/{now.strftime("%Y%m%d_%H%M")}_エラー.csv'

# タイムアウト秒数
SOCKET_TIMEOUT = 10

# yt_dlpの設定
YDL_OPTS_STATIC = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredquality': '192',
    }],
    'quiet': False,
    'no_warnings': False,
    'socket_timeout': SOCKET_TIMEOUT
}

# エラータイプ定数
ERROR_TYPES = {
    "unsupported_url": "URLがYouTubeでサポートされていない",
    "invalid_url": "URLが有効なものではない",
    "duplicate_filename": "全く同じ名前のファイルがある",
    "other": "その他が原因のエラー"
}

# CSV ヘッダー定数
HEADER1 = 'YouTubeリンク'
HEADER2 = '出力ファイル名'
HEADER3 = 'エラータイプ'
