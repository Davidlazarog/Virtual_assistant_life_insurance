import speech_recognition as sr
import pyttsx3
import src.funciones_secundarias as fn
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
'''
def residente():
    fn.hablando(f'antes de nada , necesito saber si eres residente en españa.')
    with sr.Microphone() as source:
        print("¿Es usted residente en España?")
        residente = r.listen(source)
        residente = r.recognize_google(residente, language = 'es-ES')
        residente = residente.split()
        residente = residente.lower()
        residente
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
        print(f'he escuchado bien? Solamente tienes años, te conservas genial')
        residente()

'''
def primerapregunta():
    with sr.Microphone() as source:
            print('Diga su nombre y apellidos')
            nombre = r.listen(source)
            comando = r.recognize_google(nombre, language = 'es-ES')
            fn.hablando(f'Hola {comando}, tienes una voz muy bonita, cuantos años tienes?')
            print(comando)
            return comando

def segundapregunta():
     with sr.Microphone() as source:
        print (f'Diga al asistente cuantos años tiene usted')
        edad = r.listen(source)
        comando_edad = r.recognize_google(edad, language = 'es-ES')
        comando_edad = "".join(comando_edad)
        edad = re.findall('\d+', comando_edad)
        edad = "".join(edad)
        edad = int(edad)
        print(edad)
        if edad in range(70,100):
            final()
            return edad
        else: 
            fn.hablando(f'he escuchado bien? Solamente tienes {edad} años, te conservas genial!')
            return edad


def tercerapregunta():
    fn.hablando(f'antes de nada , necesito saber si eres residente en españa.')
    with sr.Microphone() as source:
        print("¿Es usted residente en España?")
        residente = r.listen(source)
        residente = r.recognize_google(residente, language = 'es-ES')
        residente = residente.split()
        residente
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
                residente()

    


def cuartapregunta():
    lstdeportes =['descenso de barrancos', 'barranquismo', 'esqui', 'esquiar', 'mtb', 'mountanbike', 'snowboard', 'puenting', 'paracaidismo' ]
    with sr.Microphone() as source:
        fn.hablando("Cuentame un poco mas sobre tí. ¿Practicas deporte? ")
        print('¿Practicas deporte?')
        deporte =r.listen(source)
        deporte = r.recognize_google(deporte, language = 'es-ES')
        deporte = deporte.split()
        for a in deporte:
                if a == 'si':
                    fn.hablando(f'Genial, a mi también me gusta el deporte, ¿practicas algun deporte de riesgo?')
                    print("¿Practicas algun deporte de riesgo?")
                    deporte_riesgo =r.listen(source)
                    deporte_riesgo = r.recognize_google(deporte_riesgo, language = 'es-ES')
                    deporte_riesgo = deporte_riesgo.split()
                    for respuesta in deporte_riesgo:
                        if respuesta == 'si':
                            fn.hablando(f'Wow, tu estas en mi equipo, yo hago escalada, ¿tu que deporte practicas?')
                            print("¿Que deporte de riesgo practicas?")
                            deporte_riesgo_total =r.listen(source)
                            deporte_riesgo_total = r.recognize_google(deporte_riesgo_total, language = 'es-ES')
                            deporte_riesgo_total = deporte_riesgo_total.split()
                            for deporteriesgo in deporte_riesgo_total:
                                if deporteriesgo in lstdeportes:
                                    fn.hablando(f'Vaya ese es un deporte de riesgo muy complicado')
                                    fn.final()
                                    break
                                else:
                                    fn.hablando('Que divertido! Seguro que te lo pasas genial')
                                    return 'si'
                        else : 
                            fn.hablando('Mejor, hay que estar seguro siempre de lo que haces.') 
                elif a == 'no':
                    fn.hablando('Vaya, seguro que tienes muchos mas hobbies a parte del deporte')
                    return 'No'
                else:
                    fn.hablando(f'Lo siento, no te he entendido, volvamos a la pregunta')
                    return cuartapregunta()


def sextapregunta():
    profesion_excl = ['militar', 'ejecito', 'piloto', 'aviones', 'policia', 'guardia', 'bombero']
    fn.hablando('Para ir acabando con este pequeño formulario, ¿me podrias decir tu profesion?')
    with sr.Microphone() as source:
        print('Por favor diga su profesión')
        profesion_1 = r.listen(source)
        profesion_1 = r.recognize_google(profesion_1,language = 'es-ES')
        profesion_1 = profesion_1.split()
        for respuesta in profesion_1:
            if respuesta in profesion_excl:
                fn.final()
                break
            else:
                fn.hablando(f'Impresionante , no me dejas de sorprender. Creo que ya tengo suficientes datos')
                return respuesta

def quintapregunta():
    fn.hablando('Quiero saber un poco más sobre tu estilo de vida, ¿Me puedes decir si fumas?"')
    with sr.Microphone() as source:
        print("¿Diga al asistente si fuma o no?")
        fumarl=r.listen(source)
        fumarl = r.recognize_google(fumarl, language = 'es-ES')
        fumarl = fumarl.split()
        for a in fumarl:
                if a == 'si':
                    fn.hablando(f'Vaya, eso quizas pueda aumentar tu prima, ¿fumas mas de una cajetilla diaria?')
                    print("¿Fumas mas de una cajetilla diaria?")
                    fumar_caja=r.listen(source)
                    fumar_caja = r.recognize_google(fumar_caja, language = 'es-ES')
                    fumar_caja = fumar_caja.split()
                    for respuesta in fumar_caja:
                        if respuesta == 'si':
                            fn.final()
                        else: 
                            fn.hablando(f'bueno, aun estas a tiempo de dejarlo! Todo es empezar')
                            return no   
                elif a == 'no':
                    fn.hablando('Como me alegro, fumar estropea el cuerpo humano, o eso dice Wikipedia.')
                    return 'No'
                else:
                    fn.hablando(f'Lo siento, no te he entendido, volvamos a la pregunta')
                    return quitapregunta()



