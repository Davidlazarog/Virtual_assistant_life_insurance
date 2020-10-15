import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init() 

volume = engine.getProperty('volume')   
engine.setProperty('volume',1.0)   
voices = engine.getProperty('voices')  
engine.setProperty('voice', 'spanish')
engine.setProperty('voice', voices[0].id)   
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages[0] == u'es_ES':
        engine.setProperty('voice', voice.id)
        break


def hablando(text):
    engine.say(text)
    engine.runAndWait() 

def final():
    hablando(f'Lo siento, debido a tu ultima respuesta no estoy autorizado a darte presupuestos, ¿desea llamar a un agente de alguna de estas aseguradoras?')
    print(f'Lo siento, debido a tu ultima respuesta no estoy autorizado a darte presupuestos, ¿desea llamar a un agente de alguna de estas aseguradoras?')


def trat_audio (x):
    with sr.Microphone() as source:
        x = r.listen(source)
        x = r.recognize_google(x, language = 'es-ES')
        x = x.split()
        return x

        