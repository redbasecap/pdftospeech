# pdftospeech
Simple converter, that allows you to convert PDF to a playable MP3.

Installation:

run `pip3 install -r requirements.txt` to instal all needed stuff. 

make sure you have java installed otherwise the tika server can't run. 

Use:
to choose the right language open the main.py file an change at this position "TTS = gTTS(text=raw['content'], lang='de')"  
the lang='' to the language of your choice. To get a list of all language use "gtts.lang.tts_langs()"
