class Nodo:
    def __init__(self, pregunta=None, respuesta=None):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.si = None
        self.no = None

def construir_arbol(diccionario):
    if isinstance(diccionario, str):  # Si es una respuesta final
        return Nodo(respuesta=diccionario)
    
    pregunta = list(diccionario.keys())[0]
    nodo = Nodo(pregunta=pregunta)
    nodo.si = construir_arbol(diccionario[pregunta]["si"])
    nodo.no = construir_arbol(diccionario[pregunta]["no"])
    return nodo

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
        #seguir jugando aunque no adivine, mientras no pase de 20
        if intentos < 20:
            jugar(nodo, intentos +1)
    else:
        if preguntar(nodo.pregunta):
            jugar(nodo.si, intentos + 1)
        else:
            jugar(nodo.no, intentos + 1)

estructura_arbol = {
    "¿Es un ser vivo?": {
        "si": {
            "¿Es un humano?": {
                "si" : "una persona",
                "no" :{
                    "¿Es un animal?": {
                        "si": {
                            "¿Es un mamífero?": {
                                "si": {
                                    "¿Es carnívoro?": {
                                        "si": {
                                            "¿Es un felino?": {
                                                "si": "un tigre",
                                                "no": {
                                                    "¿Es un cánido?": {
                                                        "si": "un lobo",
                                                        "no": "un oso"
                                                    }
                                                }
                                            }
                                        },
                                        "no": {
                                            "¿Es un herbívoro grande?": {
                                                "si": {
                                                    "¿Tiene trompa?": {
                                                        "si": "un elefante",
                                                        "no": "una jirafa"
                                                    }
                                                },
                                                "no": {
                                                    "¿Salta?": {
                                                        "si": "un canguro",
                                                        "no": "un ciervo"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "no": {
                                    "¿Tiene plumas?": {
                                        "si": {
                                            "¿Vuela?": {
                                                "si": {
                                                    "¿Es un ave rapaz?": {
                                                        "si": "un águila",
                                                        "no": "un loro"
                                                    }
                                                },
                                                "no": "un pingüino"
                                            }
                                        },
                                        "no": {
                                            "¿Es acuático?": {
                                                "si": {
                                                    "¿Tiene caparazón?": {
                                                        "si": "una tortuga marina",
                                                        "no": "un tiburón"
                                                    }
                                                },
                                                "no": {
                                                    "¿Es un reptil?": {
                                                        "si": {
                                                            "¿Es venenoso?": {
                                                                "si": "una cobra",
                                                                "no": "una iguana"
                                                            }
                                                        },
                                                        "no": "un anfibio"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "no": {
                            "¿Es una planta?": {
                                "si": {
                                    "¿Da frutos?": {
                                        "si": "un manzano",
                                        "no": "un pino"
                                    }
                                },
                                "no": {
                                    "¿Es un arbol?": {
                                        "si": "un arbol",
                                        "no": {
                                            "¿Es un hongo?": {
                                                "si" : "un hongo",
                                                "no" : "un arbusto"
                                                }
                                            }
                                        }
                                    }
                            }
                        }
                    }
                }
            }
            
        },
        "no": {
            "¿Es un objeto hecho por humanos?": {
                "si": {
                    "¿Es un aparato electrónico?": {
                        "si": {
                            "¿Se usa para comunicarse?": {
                                "si": {
                                    "¿Tiene pantalla táctil?": {
                                        "si": "un teléfono móvil",
                                        "no": "un teléfono fijo"
                                    }
                                },
                                "no": {
                                    "¿Se usa para entretenimiento?": {
                                        "si": {
                                            "¿Es portátil?": {
                                                "si": "una consola de videojuegos portátil",
                                                "no": "una televisión"
                                            }
                                        },
                                        "no": {
                                            "¿Se usa para trabajar?": {
                                                "si": {
                                                    "¿Tiene teclado?": {
                                                        "si": "una computadora portátil",
                                                        "no": "una tablet"
                                                    }
                                                },
                                                "no": {
                                                    "¿Es un electrodoméstico?": {
                                                        "si": {
                                                            "¿Se usa para cocinar?": {
                                                                "si": "un microondas",
                                                                "no": "una lavadora"
                                                            }
                                                        },
                                                        "no": "un reloj inteligente"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "no": {
                            "¿Se usa para comer?": {
                                "si": {
                                    "¿Es un alimento?": {
                                        "si": {
                                            "¿Es dulce?": {
                                                "si": { 
                                                    "¿Es horneado?" : {
                                                        "si": "un pan",
                                                        "no": "un postre"
                                                     }
                                                },
                                                "no": {
                                                    "¿Es salado?": {
                                                        "si": "un platillo salado",
                                                        "no": "un vegetal"
                                                    }
                                                }
                                            }
                                        },
                                        "no": {
                                            "¿Es una bebida?": {
                                                "si": {
                                                    "¿Es caliente?": {
                                                        "si": "un café",
                                                        "no": "un refresco"
                                                    }
                                                },
                                                "no": "un utensilio"
                                            }
                                        }
                                    }
                                },
                                "no": {
                                    "¿Es un medio de transporte?": {
                                        "si": {
                                            "¿Se usa en el agua?": {
                                                "si": "un barco",
                                                "no": {
                                                    "¿Usa motor?": {
                                                        "si": "un automóvil",
                                                        "no": "una bicicleta"
                                                    }
                                                }
                                            }
                                        },
                                        "no": {
                                            "¿Es un instrumento?": {
                                                "si": {
                                                    "¿Se usa para construcción?": {
                                                        "si": "una herramienta",
                                                        "no": {
                                                            "¿Es un instrumento musical?": {
                                                                "si": "un instrumento musical",
                                                                "no": "un instrumento de medición"
                                                            }
                                                        }
                                                    }
                                                },
                                                "no": {
                                                    "¿Es un artículo de ropa o accesorio?": {
                                                        "si": {
                                                            "¿Es ropa?": {
                                                                "si": "una prenda de ropa",
                                                                "no": "un accesorio"
                                                            }
                                                        },
                                                        "no": {
                                                            "¿Es un mueble?": {
                                                                "si": "un mueble",
                                                                "no": {
                                                                    "Se usa para entretenimiento" :{
                                                                        "si" : "una pelicula o un serie",
                                                                        "no" :"un artículo de la casa"
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "no": {
                    "¿Es natural?": {
                        "si": {
                            "¿Es un mineral?": {
                                "si": "una roca o mineral",
                                "no": "un metal"
                            }
                        },
                        "no": {
                            "¿Es un fenómeno natural?": {
                                "si": "un rayo",
                                "no": {
                                    "¿Es un cuerpo celeste?": {
                                        "si": "una estrella",
                                        "no": "un planeta"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Construir el árbol
raiz = construir_arbol(estructura_arbol)

# Jugar
while True:
    print("\nPiensa en algo y responderé con preguntas.")
    jugar(raiz)
    if not preguntar("¿Quieres jugar de nuevo?"):
        break

print("¡Gracias por jugar!")
