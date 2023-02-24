# easy_TTS_python

pyVoiceTTS module is designed to convert text to speech with just one line of code.

This module uses pyttsx3 for text-to-speech. pyVoiceTTS is very simple.

pyVoiceTTS uses 1 required argument:
text (this is the text to be spoken)

And 7 optional arguments:
speaker (default "Alexander")
language (what language to voice)
speed (speed of speech)
showText (show spoken text)
say_and_save_to_file (save speech to file)
name_save_file (name of file to be saved, useless if say_and_save_to_file=False)
volume (volume)

Example:

from pyVoiceTTS import say
say("Ok let's go")

from pyVoiceTTS import say
say("Ok let's go", speaker='Aleksandr', speed=150, language='en')

from pyVoiceTTS import say
say("Ok let's go", speaker='Aleksandr', speed=200, language='ru', showText=True, say_and_save_to_file=True, name_save_file="test", volume=1.0)

By bolgaro4ka

