import numpy as np
import pandas as pd
# Jesus Arriaga NC = 0019
## Datos matriz 4 x 3 
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# Poner nombre a las columnas 
# y almacenar la tabla en la variable df 
print('--- datos a partir de una matriz 4 x 3 -----')
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquete'])
print(df)
# datos a partir de un diccionario 
print('--- datos a partir de un diccionario 4 x 3 -----')
alumno_diccionario={
'nombre':['Jesus','Valeria','Alonso','Matias','Jazz','Nicole'],
'califa':[90,70,50,90,90,10],
'edad':[16,16,16,16,16,16],
}
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print('Jesus Arriaga NC = 0019')