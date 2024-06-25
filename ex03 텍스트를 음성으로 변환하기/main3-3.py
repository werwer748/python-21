from gtts import gTTS
from playsound import playsound

file_path = 'mytext.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save('text.mp3')

playsound('text.mp3')

