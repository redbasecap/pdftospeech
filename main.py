import os
from gtts import gTTS
from pathlib import Path
import os 
import tika
tika.initVM()
from tika import parser 

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

for filename in files:
    if os.path.isfile(filename + ".mp3"):
        print ("File " + filename + ".mp3" + " exist")

    raw = parser.from_file(filename)
    print("please wait...processing")
    
    TTS = gTTS(text=raw['content'], lang='de')

    # Save to mp3 in current dir.
    TTS.save(filename + ".mp3")
