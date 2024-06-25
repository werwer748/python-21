from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 밤이 깊었습니다."

tts = gTTS(text=text, lang="ko")
tts.save("./hi.mp3")

playsound("./hi.mp3")