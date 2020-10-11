import speech_recognition as sr
import pyttsx3
import funciones as op
import funciones_secundarias as fn

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


#Inicio de la conversacion
fn.hablando("Hola, soy el nuevo asistente virtual del proyecto de David, ¿me podrias decir tu nombre y apellidos?")
print("Hola, soy el nuevo asistente virtual del proyecto de David, ¿me podrias decir tu nombre y apellidos?")

#Pregunta el nombre y apellidos
op.primerapregunta()

#Preguntas sobre la edad
op.segundapregunta() 
#print(f'tienes {edad} años.')

#Pregunta sobre la residencia
op.tercerapregunta()
'''
#Pregunta sobre deporte
op.cuartapregunta()

#Pregunta sobre residencia
op.sextapregunta()

'''
#residente()

