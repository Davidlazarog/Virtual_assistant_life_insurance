import pandas as pd



def resultados(nombre, edad = 26):
    url = f'input/tarifarios/{nombre}.csv'
    nombre = pd.read_csv(url, sep=';')
    nombre = pd.DataFrame(nombre)
    nombre = nombre[(nombre['Edad'] == edad)]
    nombre = nombre[['Precio', 'Indemnizacion']]
    nombre.to_csv(f'input/tarifarios/resultado/{nombre}.csv')
    return print(nombre)





