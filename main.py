import os
import logging
import pandas as pd
from yt_dlp import YoutubeDL
from tqdm import tqdm
from settings import INPUT_LINK_DATA, OUTPUT_DIRECTORY, ERROR_DIRECTORY, OUTPUT_FORMAT, YDL_OPTS_STATIC, ERROR_TYPES, HEADER1, HEADER2, HEADER3

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def download_youtube_video_as_audio(url, output_directory, output_format, output_filename):
    ydl_opts = YDL_OPTS_STATIC.copy()
    ydl_opts['outtmpl'] = os.path.join(output_directory, f'{output_filename}.%(ext)s')
    ydl_opts['postprocessors'][0]['preferredcodec'] = output_format
    ydl_opts['logger'] = logger

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return None, None, None
    except Exception as e:
        error_type = ERROR_TYPES["other"]
        if "format not available" in str(e):
            error_type = ERROR_TYPES["unsupported_url"]
        elif "ERROR:" in str(e):
            error_type = ERROR_TYPES["invalid_url"]
        logger.error(f"ダウンロード中に問題が発生しました URL:{url}, Error: {str(e)}")
        return url, output_filename, error_type

def save_error_log(errors):
    if errors:
        df_errors = pd.DataFrame(errors, columns=[HEADER1, HEADER2, HEADER3])
        os.makedirs(os.path.dirname(ERROR_DIRECTORY), exist_ok=True)
        df_errors.to_csv(ERROR_DIRECTORY, index=False)
        logger.info(f"エラーログを保存しました: {ERROR_DIRECTORY}")

def batch_download_youtube_videos_as_audio(video_info_list, output_directory, output_format):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    error_logs = []
    total_videos = len(video_info_list)
    with tqdm(total=total_videos, desc="進捗状況") as pbar:
        for video_info in video_info_list:
            try:
                url = video_info[HEADER1]
                filename = video_info[HEADER2]
                error_url, error_filename, error_type = download_youtube_video_as_audio(url, output_directory, output_format, filename)
                if error_url:
                    error_logs.append({HEADER1: error_url, HEADER2: error_filename, HEADER3: error_type})
            except KeyError as e:
                logger.error(f"キーエラー: {e}。スキップします。ビデオ情報: {video_info}")
            except Exception as e:
                logger.error(f"予期しないエラーが発生しました: {e}。スキップします。ビデオ情報: {video_info}")
            finally:
                pbar.update(1)

    save_error_log(error_logs)

if __name__ == "__main__":
    video_info_list = pd.read_csv(INPUT_LINK_DATA).to_dict('records')
    batch_download_youtube_videos_as_audio(video_info_list, OUTPUT_DIRECTORY, OUTPUT_FORMAT)
