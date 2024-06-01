import sys
from pytube import YouTube
import whisper
from pydub import AudioSegment
from getpass import getpass

# 터미널에서 URL 입력받기
# https://www.youtube.com/shorts/0xvNed3G-18 -> 터미널에서 유튜브 동영상 링크 넣음
url = input('Enter the YouTube URL: ')

# 유튜브 음성 다운로드 
yt = YouTube(url)
file_name = yt.video_id + '.mp4'
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download(filename=file_name)

# MP4 to MP3 변환
mp3_file_name = yt.video_id + '.mp3'
audio = AudioSegment.from_file(file_name)
audio.export(mp3_file_name, format="mp3")

# 텍스트 추출 함수 정의
def transcribe_audio_to_text(file_name):
    model = whisper.load_model("base")
    result = model.transcribe(file_name)
    return result["text"]

# 유튜브 음성 -> 텍스트 변환
transcribed_text = transcribe_audio_to_text(mp3_file_name)

# 텍스트 출력
print(f'"{transcribed_text}"')  # 내용 출력
