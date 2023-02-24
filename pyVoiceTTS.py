import pyttsx3

tts = pyttsx3.init()

def say(text, speaker='Aleksandr', language='en', speed=180, 
    showText=True, say_and_save_to_file=False, name_save_file="test", volume=1.0):
    
    voices = tts.getProperty('voices')
    tts.setProperty('rate', speed)
    tts.setProperty('voice', language) 
    tts.setProperty('volume',volume)
    for voice in voices:
        if voice.name == speaker:
            tts.setProperty('voice', voice.id)

    if showText==True: print(text)
    if say_and_save_to_file==True: tts.save_to_file(text, str(name_save_file)+str(".mp3"))
    tts.say(text)
    tts.runAndWait()