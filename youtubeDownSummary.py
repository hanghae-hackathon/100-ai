from pytube import YouTube
import whisper
from pydub import AudioSegment

# 유튜브 음성 다운로드 
# pytube
url = 'https://www.youtube.com/watch?v=fv1A23xE_AQ&ab_channel=%EB%AA%BB%EC%83%9D%EA%B8%B4%EB%85%B8%EC%9D%84%EC%9D%B4'
yt = YouTube(url)
file_name = yt.video_id + '.mp4'
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download(filename=file_name)

# MP4 to MP3 변환
mp3_file_name = yt.video_id + '.mp3'
audio = AudioSegment.from_file(file_name)
audio.export(mp3_file_name, format="mp3")

# 유튜브 음성 -> 텍스트 변환
model = whisper.load_model("base")
result = model.transcribe(mp3_file_name)
print(result["text"])

# 텍스트 파일로 저장
text_file_name = yt.video_id + '.txt'
with open(text_file_name, 'w', encoding='utf-8') as f:
    f.write(result["text"])
