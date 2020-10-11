import speech_recognition as sr
import pyttsx3
import funciones_secundarias as fn
import re

r = sr.Recognizer() 
engine = pyttsx3.init() # object creation

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')  
engine.setProperty('voice', 'spanish')
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages[0] == u'es_ES':
        engine.setProperty('voice', voice.id)
        break

def residente():
    fn.hablando(f'antes de nada , necesito saber si eres residente en españa.')
    with sr.Microphone() as source:
        print("¿Es usted residente en España?")
        fn.trat_audio(residente)
        print(residente)
        for a in residente:
            if a == 'si':
                fn.hablando(f'Estupendo, podemos seguir con la conversación')
                return 'si'
            elif a == 'no':
                fn.final()
                break
            else:
                fn.hablando(f'Lo siento, no te he entendido, volvamos a la pregunta')
                return residente()

def tercerapregunta_dos ():
    try :
        print(f'he escuchado bien? Solamente tienes {edad} años, te conservas genial')
        residente()
    except : 
        tercerapregunta_dos()

def primerapregunta():
    with sr.Microphone() as source:
            print('Diga su nombre y apellidos')
            nombre = r.listen(source)
            comando = r.recognize_google(nombre, language = 'es-ES')
            print(comando)
            fn.hablando(f'Hola {comando}, tienes una voz muy bonita, cuantos años tienes?')

def segundapregunta():
     with sr.Microphone() as source:
        print (f'Diga al asistente cuantos años tiene usted')
        edad = r.listen(source)
        comando_edad = r.recognize_google(edad, language = 'es-ES')
        comando_edad = "".join(comando_edad)
        edad = re.findall('\d+', comando_edad)
        print(edad)
        return edad


def tercerapregunta():
    engine.say(f'he escuchado bien? Solamente tienes  años, te conservas genial!')
    engine.runAndWait()
    tercerapregunta_dos()

        

lstdeportes =['descenso de barrancos', 'barranquismo', 'esqui', 'esquiar', 'mtb', 'mountanbike', 'snowboard', 'puenting', '' ]

def cuartapregunta():
    with sr.Microphone() as source:
        print("Cuentame un poco mas sobre tí. ¿Practicas deporte? ")
        fn.trat_audio(deporte)
        for a in deporte:
                if a == 'si':
                    fn.hablando(f'Genial, a mi tambien me gusta el deporte, ¿practicas algun deporte de riesgo?')
                    print("¿Practicas algun deporte de riesgo?")
                    fn.trat_audio(deporte_riesgo)
                    for respuesta in deporte_riesgo:
                        if respuesta == 'si':
                            fn.hablando(f'Genial, a mi tambien me gusta el deporte, ¿practicas algun deporte de riesgo?')
                            print("¿Que deporte de riesgo practicas?")
                            fn.trat_audio(deporte_riesgo_total)
                            for deporteriesgo in deporte_riesgo_total:
                                if deporteriesgo in lstdeportes:
                                    fn.hablando(f'Vaya ese es un deporte de riesgo muy complicado')
                                    fn.final()
                                    break
                                else:
                                    fn.hablando('Que divertido! Seguro que te lo pasas genial')
                                    
                                    return 'si'     
                elif a == 'no':
                    fn.hablando('Vaya, seguro que tienes muchos mas hobbies a parte del deporte')
                    return 'No'
                else:
                    fn.hablando(f'Lo siento, no te he entendido, volvamos a la pregunta')
                    return cuartapregunta()

profesion_excl = ['militar', 'ejecito', 'piloto', 'aviones', 'policia', 'guardia', 'bombero']

def sextapregunta():
    with sr.Microphone() as source:
        print('Por favor diga su profesión')
        fn.trat_audio(profesion)
        for respuesta in profesion:
            if respuesta in profesion_excl:
                final()
                break
            else:
                fn.hablando(f'Impresionante {nombre}, no me dejas de sorprender. Creo que ya tengo suficientes datos')



