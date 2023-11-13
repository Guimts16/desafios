from googletrans import Translator
from gtts import gTTS
import os
from time import sleep

translator = Translator()
lingua = "fr"
frase = [
    "Hello, how are you?",
    "What's up?",
    "Nice to meet you.",

    ]
frases = translator.translate(frase, dest=lingua)


for t in frases:
    print(t.origin, '->', t.text)
    tradu = gTTS(t.text, lang=lingua, slow=False, tld='com')

    tradu_file = 'traducao.mp3'
    tradu.save(tradu_file)

    os.system(tradu_file)
    sleep(3)