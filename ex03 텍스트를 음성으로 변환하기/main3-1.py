from gtts import gTTS

text = "안녕하세요. 밤이 깊었습니다."

tts = gTTS(text=text, lang="ko")
tts.save("./hi.mp3")