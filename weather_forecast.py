from gtts import gTTS
from playsound import playsound

day =input("요일:")
weather = input("날씨:1(맑음), 2(흐림)")
temp = input("기온:")

weather = int(weather)
temp = int(temp)

if weather == 1:
    weather_msg = "맑습니다."
else:
    weather_msg = "흐립니다."

if temp <= 10:
    temp_msg = "쌀쌀한"
else:
    temp_msg = "따뜻한"

read_msg = day + "요일인 오늘은 전국이 "+weather_msg
read_msg = read_msg + temp_msg + "출근길이 될것으로 예상되므로, 알맞은 옷차림을 준비하시기 바랍니다. "
read_msg = read_msg+ " 전국 대부분 지역에서 낮과 밤의 기온차가 큰 편이므로, 건강관리에 유의하시기 바랍니다. "
read_msg = read_msg+ " 오늘 "+day+"요일도, 편안한 하루 되세요"


tts = gTTS(text=read_msg, lang="ko")
tts.save("e:/python/hi.mp3")
playsound("e:/python/hi.mp3")
