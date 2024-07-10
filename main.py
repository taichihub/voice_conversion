import os
import logging
import pandas as pd
from pytube import YouTube
from pydub import AudioSegment
from tqdm import tqdm
from settings import INPUT_LINK_DATA, OUTPUT_FORMAT, OUTPUT_DIRECTORY

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def download_youtube_video_as_audio(url, output_directory, output_format, output_filename):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(output_path=output_directory, filename=output_filename)
        
        base, ext = os.path.splitext(downloaded_file)
        audio_file = base + f'.{output_format}'
        
        AudioSegment.from_file(downloaded_file).export(audio_file, format=output_format)
        os.remove(downloaded_file)
        
        # logger.info(f"ダウンロードと変換完了: {audio_file}")
    except Exception as e:
        logger.error(f"{url} のダウンロード中にエラーが発生しました: {e}")

def batch_download_youtube_videos_as_audio(video_info_list, output_directory, output_format):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    total_videos = len(video_info_list)
    with tqdm(total=total_videos, desc="進捗状況") as pbar:
        for i, video_info in enumerate(video_info_list, start=1):
            url = video_info['YouTubeリンク']
            filename = video_info['出力ファイル名']
            download_youtube_video_as_audio(url, output_directory, output_format, filename)
            pbar.update(1)
            progress = (i / total_videos) * 100
            tqdm.write(f"進捗状況: {progress:.2f}%")

if __name__ == "__main__":
    video_info_list = pd.read_csv(INPUT_LINK_DATA).to_dict('records')
    batch_download_youtube_videos_as_audio(video_info_list, OUTPUT_DIRECTORY, OUTPUT_FORMAT)
