import json

def crear_archivo_json(datos):
    with open("datos.json","w") as ubicaciones:
        json.dump(datos, ubicaciones)
        print("Los datos fueron exportados correctamente")

def leer_archivo_json():
    with open("datos.json","r") as archivo_load:
        importacion_datos = json.load(archivo_load)
        print("Los datos fueron importados correctamente")
        return importacion_datos

base_de_datos = [

    {
        "id":"00047895",
        "nombre":"Gelver Estevan",
        "Apellido":"Castro Alonso",
        "edad":20,
        "notas":[5,5,3.75,3.75,5]
    },

    {
        "id":"00046785",
        "nombre":"Pepito ",
        "Apellido":"Perez",
        "edad":12,
        "notas":[4.5,5,4,3.75,4]
    },
    
    {
        "id":"00047621",
        "nombre":"Carlos ferre",
        "Apellido":"giro",
        "edad":45,
        "notas":[2.1,5,3.75,3,5]
    } 
]
#print(base_de_datos)
crear_archivo_json(base_de_datos)
datos=leer_archivo_json()
print(datos)
print(datos[1]["nombre"])