class Nodo:
    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.si = None
        self.no = None

def preguntar(mensaje):
    """Función para obtener respuesta sí/no del usuario"""
    respuesta = ""
    while respuesta not in ("si", "no"):
        respuesta = input(mensaje + " (si/no): ").strip().lower()
    return respuesta == "si"

def jugar(nodo, intentos=0):
    """Función para recorrer el árbol y aprender nuevas respuestas"""
    if intentos >= 20:
        print("¡He perdido! No logré adivinar en 20 preguntas.")
        return
    
    if nodo.respuesta:
        print(f"¿Estás pensando en {nodo.respuesta}?")
        if preguntar("¿Adiviné correctamente?"):
            print("¡Genial! :))")
        else:
            print("¡Vaya! Parece que necesito más conocimiento.")
            nueva_respuesta = input("¿En qué estabas pensando? ").strip()
            nueva_pregunta = input(f"¿Qué pregunta distingue {nueva_respuesta} de {nodo.respuesta}? ").strip()
            es_si = preguntar(f"Si fuera {nueva_respuesta}, ¿la respuesta a '{nueva_pregunta}' sería 'sí'?")
            
            nodo.pregunta = nueva_pregunta
            if es_si:
                nodo.si = Nodo(respuesta=nueva_respuesta)
                nodo.no = Nodo(respuesta=nodo.respuesta)
            else:
                nodo.si = Nodo(respuesta=nodo.respuesta)
                nodo.no = Nodo(respuesta=nueva_respuesta)

            nodo.respuesta = None  
    else:
        if preguntar(nodo.pregunta):
            jugar(nodo.si, intentos + 1)
        else:
            jugar(nodo.no, intentos + 1)

raiz = Nodo("¿Es un ser vivo?")

raiz.si = Nodo("¿Es un animal?")
raiz.si.si = Nodo("¿Es un mamífero?")
raiz.si.si.si = Nodo("¿Es carnívoro?")
raiz.si.si.si.si = Nodo(respuesta="un felino")
raiz.si.si.si.no = Nodo(respuesta="un herbívoro")
raiz.si.si.no = Nodo("¿Vuela?")
raiz.si.si.no.si = Nodo(respuesta="un ave")
raiz.si.si.no.no = Nodo("¿Es acuático?")
raiz.si.si.no.no.si = Nodo(respuesta="un pez")
raiz.si.si.no.no.no = Nodo(respuesta="un reptil")
raiz.si.no = Nodo("¿Es un tipo de planta?")
raiz.si.no.si = Nodo(respuesta="un árbol")
raiz.si.no.no = Nodo(respuesta="una flor")

raiz.no = Nodo("¿Es un objeto hecho por humanos?")
raiz.no.si = Nodo("¿Se usa para comer?")
raiz.no.si.si = Nodo("¿Se usa para cocinar?")
raiz.no.si.si.si = Nodo(respuesta="una sartén")
raiz.no.si.si.no = Nodo(respuesta="un utensilio")
raiz.no.si.no = Nodo("¿Produce sonido?")
raiz.no.si.no.si = Nodo("¿Tiene cuerdas?")
raiz.no.si.no.si.si = Nodo(respuesta="un instrumento musical de cuerda")
raiz.no.si.no.si.no = Nodo(respuesta="un instrumento de viento")
raiz.no.si.no.no = Nodo("¿Se usa para construcción?")
raiz.no.si.no.no.si = Nodo(respuesta="una herramienta")
raiz.no.si.no.no.no = Nodo("¿Es un vehículo?")
raiz.no.si.no.no.no.si = Nodo("¿Usa motor?")
raiz.no.si.no.no.no.si.si = Nodo(respuesta="un automóvil")
raiz.no.si.no.no.no.si.no = Nodo(respuesta="una bicicleta")
raiz.no.si.no.no.no.no = Nodo(respuesta="un barco")
raiz.no.no = Nodo("¿Es natural?")
raiz.no.no.si = Nodo("¿Es un mineral?")
raiz.no.no.si.si = Nodo(respuesta="una roca o mineral")
raiz.no.no.si.no = Nodo(respuesta="un metal")
raiz.no.no.no = Nodo("¿Es un fenómeno natural?")
raiz.no.no.no.si = Nodo(respuesta="un rayo")
raiz.no.no.no.no = Nodo("¿Es un cuerpo celeste?")
raiz.no.no.no.no.si = Nodo(respuesta="una estrella")
raiz.no.no.no.no.no = Nodo(respuesta="un planeta")


while True:
    print("\nPiensa en algo y responderé con preguntas.")
    jugar(raiz)
    if not preguntar("¿Quieres jugar de nuevo?"):
        break

print("¡Gracias por jugar!")
