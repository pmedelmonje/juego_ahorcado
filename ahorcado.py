"""
Juego del ahorcado

Lo que debería hacer el programa:

- 3 niveles de dificultad:
    - Fácil: palabras con 5 letras, 10 intentos
    - Intermedia: palabras con 6 letras, 11 intentos
    - Difícil: palabras con 7 letras, 12 intentos

- El jugador, al empezar, elige la dificultad. Según la dificultad que elija,
el programa selecciona una palabra al azar de una lista y establece la cantidad
de intentos.

- El jugador ingresa una letra para tratar de acertar la palabra. A medida que
vaya acertando, el programa muestra las letras acertadas y su posición en la
palabra.

- Si el jugador falla, se resta al contador de intentos.

- El juego termina cuando el jugador ha acertado a la palabra o haya gastado
todos sus intentos.
"""

import random

# funciones para extraer palabras aleatorias

def elige5():
    print("\nSeleccionada la opción Fácil")
    print("\nDispondrás de 10 intentos")
    print("\n _ _ _ _ _")
    return random.choice(palabras5l)


def elige6():
    palabra = random.choice(palabras6l)
    print("Seleccionada la opción Intermedia")
    print("Dispondrás de 11 intentos")
    print("\n _ _ _ _ _ _")
    return random.choice(palabras6l)

def elige7():
    random.choice(palabras7l)
    print("Seleccionada la opción Difícil")
    print("Dispondrás de 12 intentos")
    print("\n _ _ _ _ _ _ _")
    return random.choice(palabras7l)


# listas con palabras

palabras5l = ["VAGON", "CANCER", "VIRGO", "ABEJA", "VERDE", "HIELO", "LIBRA",
              "GASTO", "APOLO", "APODO", "JOVEN", "AMADO", "AMADA", "MASAS",
              "MAZAS", "GATOS", "PERRO", "ASILO", "ARETE", "ATADO", "ATAUD",
              "ASPID", "ARBOL", "AROMA", "AREPA", "ARGAN", "ARIES", "LLAVE",
              "NINFA", "CHOLO", "BOTES", "ABONO", "MANGO", "ACIDO", "AGRIO",
              "AGUDO", "AGUAS", "MARES", "BAÑOS", "BEBES", "BESOS", "BODAS",
              "ALMAS", "ALOJO", "BRUMA", "CASAS", "CAZAS", "BOMBA", "BRUTO",
              "CACAO", "CARGO", "CAPAZ", "CARGA", "AVARO", "ALANO", "AZOTE",
              "ATAJO", "CREMA", "CASCO", "CASOS", "CASPA", "CAUSA", "CUEVA",
              "CAIDA", "CAÑAS", "PESCA", "CLAVO", "COGER", "CLARA", "CLARO",
              "ESPIA", "FALLA", "FORMA", "FALTA", "FRITO", "FRITA", "INDIO",
              "INDIA", "HUNOS", "GODOS", "LADRON", "LAURA", "LARGO", "LARGA",
              "PASTA", "PASTO", "PISTA", "LOCHA", "PARGO", "PERCA", "PISCO",
              "PULSO", "RIFLE", "CASTA", "LUCHA", "MALTA", "MONTO", "MOSCU",
              "NEPAL", "MENTA", "MAREA", "MINAS", "OGROS", "SHREK", "PATAS",
              "TAURO", "PECES", "PITON", "PYTHON", "DULCE", "SEÑOR", "CERDO",
              "COLON", "TURCO", "TURCA", "PERSA", "TOKIO", "CHINO", "CHINA",
              "BARCO", "BUQUE", "BUCLE", "CANTO", "POETA", "LINDO", "LINDA",
              "YEGUA", "BURRO", "BURRA", "LLAMA", "FUEGO", "NINFA"]

palabras6l = ["PISCIS", "CASTRO", "PERROS", "PISTAS", "ABADIA", "AHORRO",
              "VIBORA", "AGOBIO", "AMARGO", "DULCES", "SALADO", "PASTEL",
              "SEÑORA", "FLAUTA", "CERDOS", "PALOMA", "PICHON", "ZORZAL",
              "ANTENA", "ATENEA", "ATENAS", "ANTISA", "ARABIA", "GENOVA",
              "COSACO", "COSACA", "DRAGON", "HALCON", "AGUILA", "VIRGEN",
              "TOYOTA", "MADRID", "MONGOL", "CUMANO", "CUMANA", "POLACO",
              "POLACA", "VUELTA", "AMORIO", "AFINAR", "AFILAR", "ANIMAR",
              "LAZARO", "LESBOS", "TAMBOR", "CASTOR", "CANTOR", "ESPADA",
              "ESCUDO", "LLAMAR", "LLAMAS"]

palabras7l = ["GEMINIS", "ACUARIO", "ARBOLES", "JOVENES", "CULEBRA", "SEMILLA",
              "TORTOLA", "PALOMAS", "ARDILLA", "CHALECO", "ESPARTA", "ISFAHAN",
              "COLOMBO", "COLOMBA", "BOLIVIA", "TARTARO", "TARTARA", "VIKINGO",
              "VIKINGA", "GENOVES", "CAVERNA", "POLONIA", "MASHHAD", "TEHERAN",
              "FRANCIA", "FRANCOS", "FRANCAS", "VENTANA", "CANCION", "CANTORA",
              "POETISA", "GORRION", "VUELTAS", "DALMATA", "CABALLO", "COBAYA",
              "GLACIAR", ]


aciertos5 = ["_","_","_","_","_"]

aciertos6 = ["_","_","_","_","_","_"]

aciertos7 = ["_","_","_","_","_","_","_"]

palabra = None

intentos = 0

# Comienzo del juego. Selección de dificultad

print("Bienvenido(a) al juego del ahorcado. Acierta la palabra antes de perder todos tus intentos")
print("\nElige la dificultad: \n1- Fácil \n2- Intermedia \n3- Difícil")
dificultad = int(input("> "))

while not dificultad in [1, 2, 3]:
    print("Opción incorrecta")
    print("\nElige la dificultad: \n1- Fácil \n2- Intermedia \n3- Difícil")
    dificultad = int(input("> "))
    
if dificultad == 1:
    palabra = elige5()
    pal_lista = list(palabra)
    aciertos = [" ", " ", " ", " ", " "]
    print(pal_lista)
    print(palabra)
    intentos = 10
    
elif dificultad == 2:
    palabra = elige6()
    intentos = 11
    
else:
    palabra = elige7()
    intentos = 12
    
# El jugador ingresa letras
    
letra = input("\nIngresa una letra: ").capitalize()

for l in pal_lista:
    if l == letra:
        aciertos5[l] = letra
        print("has acertado")
        print(aciertos5)




