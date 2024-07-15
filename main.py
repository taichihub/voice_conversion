import os
import logging
import pandas as pd
from yt_dlp import YoutubeDL
from tqdm import tqdm
from settings import INPUT_LINK_DATA, OUTPUT_FORMAT, OUTPUT_DIRECTORY

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def download_youtube_video_as_audio(url, output_directory, output_format, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_directory, f'{output_filename}.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logger.info(f"ダウンロードと変換完了: {output_filename}.{output_format}")
    except Exception as e:
        logger.error(f"{url} のダウンロード中にエラーが発生しました: {e}")

def batch_download_youtube_videos_as_audio(video_info_list, output_directory, output_format):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    total_videos = len(video_info_list)
    with tqdm(total=total_videos, desc="進捗状況", disable=True) as pbar:
        for i, video_info in enumerate(video_info_list, start=1):
            try:
                url = video_info['YouTubeリンク']
                filename = video_info['出力ファイル名']
                download_youtube_video_as_audio(url, output_directory, output_format, filename)
            except KeyError as e:
                logger.error(f"キーエラー: {e}。スキップします。ビデオ情報: {video_info}")
                continue
            except Exception as e:
                logger.error(f"予期しないエラーが発生しました: {e}。スキップします。ビデオ情報: {video_info}")
                continue
            pbar.update(1)
            progress = (i / total_videos) * 100
            tqdm.write(f"進捗状況: {progress:.2f}%")

if __name__ == "__main__":
    video_info_list = pd.read_csv(INPUT_LINK_DATA).to_dict('records')
    batch_download_youtube_videos_as_audio(video_info_list, OUTPUT_DIRECTORY, OUTPUT_FORMAT)
