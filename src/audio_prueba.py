import speech_recognition as sr
import pyttsx3
import src.funciones as op
import src.funciones_secundarias as fn
import src.tablas as tb

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

def conversacion():
    #Inicio de la conversacion
    fn.hablando("Hola, soy el nuevo asistente virtual del proyecto de David, ¿me podrias decir tu nombre y apellidos?")
    print("Hola, soy el nuevo asistente virtual del proyecto de David, ¿me podrias decir tu nombre y apellidos?")

    #Pregunta el nombre y apellidos
    nombre = op.primerapregunta()

    #Preguntas sobre la edad
    edad = op.segundapregunta() 

    #print(f'tienes {edad} años.')

    #Pregunta sobre la residencia
    residencia = op.tercerapregunta()

    #Pregunta sobre deporte
    deporte = op.cuartapregunta()

    #Pregunta sobre fumar 

    fumar = op.quintapregunta()

    #Pregunta sobre profesion
    profesion =op.sextapregunta()

    nombre="David"
    edad=25
    residencia="si"
    deporte="si"
    fumar="si"
    profesion="becario"
    fn.hablando(f'Esto es una demo y poco a poco estoy aprendiendo, mientras busco los resultados, revisa los datos')
    print(f'Tu respuesta sobre el nombre ha sido {nombre}')
    print(f'Tu respuesta sobre la edad es que tienes {edad} años')
    print(f'Segun me has contado, {residencia} eres residente en España')
    print(f'{fumar} fumas')
    print(f'Su profesion es {profesion}')

    if fumar == 'si':
        print('ATENCIÓN ESTOS PRECIOS TIENEN UNA SOBREPRIMA DE UN 10% YA QUE FUMAS')
    else:
        pass

    print('ASEGURADORA 1')
    tb.resultados('aseguradoras_1', edad = edad)
    print('ASEGURADORA 2')
    tb.resultados('aseguradoras_2', edad = edad)
    print('ASEGURADORA 3')
    tb.resultados('aseguradoras_3', edad = edad)
    print('ASEGURADORA 4')
    tb.resultados('aseguradoras_4', edad = edad)
    print('ASEGURADORA 5')
    tb.resultados('aseguradoras_5', edad = edad)
    subprocess.Popen(["open", "http://127.0.0.1:5000/test"])
    return 'FIN'

