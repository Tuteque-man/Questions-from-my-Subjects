import tkinter as tk
from tkinter import messagebox
import random

# Preguntas organizadas por dificultad
preguntas = {
    "facil": [
        {
            "pregunta": "¿Qué es un sistema operativo?",
            "respuesta_correcta": "Software que gestiona recursos",
            "respuestas_falsas": [
                "Un tipo de hardware",
                "Un archivo de texto",
                "Una conexión de red"
            ]
        },
        {
            "pregunta": "¿Qué sistema operativo utiliza un kernel?",
            "respuesta_correcta": "Linux",
            "respuestas_falsas": [
                "Microsoft Word",
                "Google Chrome",
                "Dropbox"
            ]
        },
        {
            "pregunta": "¿Cuál es un ejemplo de un sistema operativo?",
            "respuesta_correcta": "Windows",
            "respuestas_falsas": [
                "Intel",
                "NVIDIA",
                "Firefox"
            ]
        },
        {
            "pregunta": "¿Qué tipo de software es Windows?",
            "respuesta_correcta": "Sistema operativo",
            "respuestas_falsas": [
                "Aplicación de escritorio",
                "Programa antivirus",
                "Controlador de red"
            ]
        },
        {
            "pregunta": "¿Qué permite la multitarea?",
            "respuesta_correcta": "Ejecutar múltiples procesos",
            "respuestas_falsas": [
                "Acceso a una sola tarea",
                "Usar un solo núcleo",
                "Evitar interrupciones"
            ]
        },
        {
            "pregunta": "¿Cuál es la función principal de la BIOS?",
            "respuesta_correcta": "Inicializar el hardware al encender",
            "respuestas_falsas": [
                "Gestionar archivos del sistema",
                "Ejecutar programas de usuario",
                "Conectar a Internet"
            ]
        },
        {
            "pregunta": "¿Qué es un controlador de dispositivo?",
            "respuesta_correcta": "Software que controla hardware específico",
            "respuestas_falsas": [
                "Un tipo de procesador",
                "Un programa de edición",
                "Un sistema de archivos"
            ]
        },
        {
            "pregunta": "¿Qué es la interfaz gráfica en un sistema operativo?",
            "respuesta_correcta": "Es la parte visual que interactúa el usuario",
            "respuestas_falsas": [
                "El núcleo del sistema",
                "La línea de comandos",
                "El hardware del monitor"
            ]
        },
        {
            "pregunta": "¿Qué significa 'bootear' un sistema?",
            "respuesta_correcta": "Iniciar el sistema operativo",
            "respuestas_falsas": [
                "Apagar el sistema",
                "Actualizar el software",
                "Formatear el disco"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso en sistemas operativos?",
            "respuesta_correcta": "Programa en ejecución",
            "respuestas_falsas": [
                "Archivo almacenado en disco",
                "Una tarea programada",
                "Un componente de hardware"
            ]
        },
        {
            "pregunta": "¿Qué es la memoria RAM?",
            "respuesta_correcta": "Memoria de acceso rápido para procesos en ejecución",
            "respuestas_falsas": [
                "Disco duro",
                "Memoria solo de lectura",
                "Memoria en la tarjeta gráfica"
            ]
        },
        {
            "pregunta": "¿Qué hace la función 'sleep' en programación?",
            "respuesta_correcta": "Pausa la ejecución del proceso por un tiempo",
            "respuestas_falsas": [
                "Reinicia la computadora",
                "Cierra un programa",
                "Ejecuta en modo seguro"
            ]
        },
        {
            "pregunta": "¿Qué es un sistema de archivos?",
            "respuesta_correcta": "Organiza y almacena datos en los discos",
            "respuestas_falsas": [
                "Un sistema operativo",
                "Un hardware de red",
                "Un programa antivirus"
            ]
        },
        {
            "pregunta": "¿Qué es la virtualización?",
            "respuesta_correcta": "Crear máquinas virtuales en un solo hardware",
            "respuestas_falsas": [
                "Ejecutar programas en línea",
                "Aumentar la velocidad de la CPU",
                "Desactivar el hardware"
            ]
        },
        {
            "pregunta": "¿Para qué sirve el gestor de tareas?",
            "respuesta_correcta": "Monitorea y administra procesos en ejecución",
            "respuestas_falsas": [
                "Instala software",
                "Configura la red",
                "Actualiza el sistema operativo"
            ]
        },
        {
            "pregunta": "¿Qué es la seguridad en el sistema operativo?",
            "respuesta_correcta": "Protege los datos y recursos contra accesos no autorizados",
            "respuestas_falsas": [
                "Permite acceso ilimitado",
                "No tiene importancia",
                "Solo se aplica en redes"
            ]
        }
    ],
    "medio": [
        {
            "pregunta": "¿Qué hace el kernel de un sistema operativo?",
            "respuesta_correcta": "Gestiona hardware y software",
            "respuestas_falsas": [
                "Guarda archivos",
                "Elimina virus",
                "Optimiza gráficos"
            ]
        },
        {
            "pregunta": "¿Qué sistema de archivos usa Windows?",
            "respuesta_correcta": "NTFS",
            "respuestas_falsas": [
                "EXT4",
                "FAT16",
                "APFS"
            ]
        },
        {
            "pregunta": "¿Qué significa multitarea?",
            "respuesta_correcta": "Ejecutar varias tareas a la vez",
            "respuestas_falsas": [
                "Usar un solo núcleo de CPU",
                "Tener varios usuarios en un sistema",
                "Ejecutar un solo programa"
            ]
        },
        {
            "pregunta": "¿Qué es la memoria virtual?",
            "respuesta_correcta": "Espacio en disco usado como RAM",
            "respuestas_falsas": [
                "Un módulo físico adicional",
                "Cache de datos externos",
                "Espacio de datos en la CPU"
            ]
        },
        {
            "pregunta": "¿Qué hace un sistema de archivos?",
            "respuesta_correcta": "Organiza los datos en el disco",
            "respuestas_falsas": [
                "Procesa solicitudes del usuario",
                "Controla los periféricos",
                "Bloquea acceso no deseado"
            ]
        },
        {
            "pregunta": "¿Qué es una partición en un disco duro?",
            "respuesta_correcta": "Una división lógica del disco",
            "respuestas_falsas": [
                "Un tipo de virus",
                "Una copia de seguridad",
                "Un archivo de sistema"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso en sistemas operativos?",
            "respuesta_correcta": "Programa en ejecución",
            "respuestas_falsas": [
                "Archivo almacenado en disco",
                "Una tarea programada",
                "Un componente de hardware"
            ]
        },
        {
            "pregunta": "¿Qué es un hilo en programación?",
            "respuesta_correcta": "Unidad de ejecución dentro de un proceso",
            "respuestas_falsas": [
                "Un archivo de configuración",
                "Un proceso completo",
                "Una función de sistema"
            ]
        },
        {
            "pregunta": "¿Qué es la paginación en memoria?",
            "respuesta_correcta": "División de memoria en páginas para facilitar la gestión",
            "respuestas_falsas": [
                "Un método de compresión",
                "Una técnica de seguridad",
                "Un tipo de hardware"
            ]
        },
        {
            "pregunta": "¿Qué hace el gestor de memoria?",
            "respuesta_correcta": "Asigna y libera memoria para procesos",
            "respuestas_falsas": [
                "Controla la velocidad del CPU",
                "Gestiona la red",
                "Controla la pantalla"
            ]
        },
        {
            "pregunta": "¿Qué es el deadlock en sistemas operativos?",
            "respuesta_correcta": "Situación donde procesos esperan indefinidamente recursos que otros procesos mantienen",
            "respuestas_falsas": [
                "Error en la memoria",
                "Fallo en la red",
                "Proceso terminado"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso zombie?",
            "respuesta_correcta": "Proceso terminado pero aún en la tabla de procesos",
            "respuestas_falsas": [
                "Proceso en ejecución activa",
                "Proceso en espera",
                "Proceso que consume mucho CPU"
            ]
        },
        {
            "pregunta": "¿Qué es un sistema en tiempo real?",
            "respuesta_correcta": "Sistema que responde en un tiempo garantizado",
            "respuestas_falsas": [
                "Sistema que solo funciona en línea",
                "Sistema que no requiere respuesta rápida",
                "Sistema de almacenamiento"
            ]
        },
        {
            "pregunta": "¿Qué es el scheduling en sistemas operativos?",
            "respuesta_correcta": "Planificación de procesos para que se ejecuten en CPU",
            "respuestas_falsas": [
                "Control de la memoria",
                "Gestión de archivos",
                "Configuración de hardware"
            ]
        },
        {
            "pregunta": "¿Qué significa 'preemptive multitasking'?",
            "respuesta_correcta": "El sistema puede interrumpir procesos para asignar CPU a otros",
            "respuestas_falsas": [
                "Los procesos no pueden ser detenidos",
                "Solo un proceso puede ejecutarse a la vez",
                "No hay planificación de procesos"
            ]
        }
    ],
    "dificil": [
        {
            "pregunta": "¿Qué es una interrupción en sistemas operativos?",
            "respuesta_correcta": "Señal que pausa procesos",
            "respuestas_falsas": [
                "Conexión de red inactiva",
                "Error crítico del sistema",
                "Bloqueo de hardware"
            ]
        },
        {
            "pregunta": "¿Qué componente maneja la memoria virtual?",
            "respuesta_correcta": "El kernel",
            "respuestas_falsas": [
                "El BIOS",
                "El navegador web",
                "El sistema de archivos"
            ]
        },
        {
            "pregunta": "¿Qué es el tiempo de conmutación?",
            "respuesta_correcta": "Tiempo para cambiar entre procesos",
            "respuestas_falsas": [
                "Tiempo de inicio del sistema",
                "Tiempo de lectura de disco",
                "Latencia de red"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso hijo?",
            "respuesta_correcta": "Proceso creado por otro proceso",
            "respuestas_falsas": [
                "Un controlador de hardware",
                "Un hilo principal",
                "Una interrupción en memoria"
            ]
        },
        {
            "pregunta": "¿Qué define el estado 'bloqueado' en un proceso?",
            "respuesta_correcta": "Está esperando I/O",
            "respuestas_falsas": [
                "Está ejecutándose en la CPU",
                "Está en espera para acceso a RAM",
                "Está en modo multitarea"
            ]
        },
        {
            "pregunta": "¿Qué es la planificación por prioridad?",
            "respuesta_correcta": "Ejecutar procesos según su prioridad",
            "respuestas_falsas": [
                "Ejecutar procesos en orden de llegada",
                "Ejecutar solo procesos de bajo nivel",
                "No considerar prioridades"
            ]
        },
        {
            "pregunta": "¿Qué es la técnica de paging en memoria?",
            "respuesta_correcta": "División de memoria en páginas iguales",
            "respuestas_falsas": [
                "Segmentación de memoria en segmentos variables",
                "Asignación fija de memoria",
                "Memoria en bloques físicos"
            ]
        },
        {
            "pregunta": "¿Qué es un semáforo en sistemas operativos?",
            "respuesta_correcta": "Mecanismo para controlar acceso concurrente",
            "respuestas_falsas": [
                "Tipo de memoria",
                "Unidad de tiempo",
                "Hardware de red"
            ]
        },
        {
            "pregunta": "¿Qué es un deadlock?",
            "respuesta_correcta": "Situación donde procesos esperan indefinidamente recursos que otros procesos mantienen",
            "respuestas_falsas": [
                "Error de hardware",
                "Proceso que termina abruptamente",
                "Sistema en modo seguro"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso en estado 'suspendido'?",
            "respuesta_correcta": "Proceso que ha sido pausado y no está en ejecución",
            "respuestas_falsas": [
                "Proceso en ejecución activa",
                "Proceso terminado",
                "Proceso que no usa memoria"
            ]
        },
        {
            "pregunta": "¿Qué es un sistema en modo real?",
            "respuesta_correcta": "Sistema que garantiza respuestas en tiempo definido",
            "respuestas_falsas": [
                "Sistema operativo general",
                "Sistema que no requiere respuesta rápida",
                "Sistema de almacenamiento en la nube"
            ]
        },
        {
            "pregunta": "¿Qué es la técnica de mutual exclusion?",
            "respuesta_correcta": "Mecanismo para evitar acceso concurrente a recursos críticos",
            "respuestas_falsas": [
                "Sistema de archivos",
                "Técnica de compresión",
                "Algoritmo de búsqueda"
            ]
        },
        {
            "pregunta": "¿Qué es un proceso zombie?",
            "respuesta_correcta": "Proceso terminado pero aún en la tabla de procesos",
            "respuestas_falsas": [
                "Proceso activo en CPU",
                "Proceso en espera",
                "Proceso en modo de hibernación"
            ]
        },
        {
            "pregunta": "¿Qué es el scheduling en sistemas operativos?",
            "respuesta_correcta": "Planificación de la ejecución de procesos",
            "respuestas_falsas": [
                "Gestión de memoria",
                "Control de dispositivos",
                "Configuración de red"
            ]
        },
        {
            "pregunta": "¿Qué implica la planificación preemptive?",
            "respuesta_correcta": "El sistema puede interrumpir procesos en ejecución para asignar CPU a otros",
            "respuestas_falsas": [
                "Los procesos no pueden ser detenidos",
                "Solo un proceso puede ejecutarse en todo momento",
                "No hay planificación en el sistema"
            ]
        }
    ]
}



# Variables globales
puntuacion = 0
preguntas_seleccionadas = []
pregunta_actual = None
progreso_actual = 0
total_preguntas = 5

def seleccionar_dificultad(dificultad):
    global preguntas_seleccionadas, progreso_actual, puntuacion
    puntuacion = 0
    progreso_actual = 0
    disponibles = preguntas[dificultad]
    if len(disponibles) < total_preguntas:
        preguntas_seleccionadas = disponibles[:]  # Tomar todas las preguntas disponibles
    else:
        preguntas_seleccionadas = random.sample(disponibles, total_preguntas)
    mostrar_pregunta()

def mostrar_pregunta():
    global pregunta_actual, progreso_actual
    if preguntas_seleccionadas:
        pregunta_actual = preguntas_seleccionadas.pop()
        opciones = [pregunta_actual["respuesta_correcta"]] + pregunta_actual["respuestas_falsas"]
        random.shuffle(opciones)
        progreso_actual += 1
        lbl_progreso.config(text=f"Pregunta {progreso_actual} de {total_preguntas}")
        lbl_pregunta.config(text=pregunta_actual["pregunta"])
        for i, opcion in enumerate(opciones):
            botones_opciones[i].config(text=opcion, state="normal", wraplength=450)
    else:
        finalizar_juego()

def verificar_respuesta(opcion_seleccionada):
    global puntuacion
    if opcion_seleccionada == pregunta_actual["respuesta_correcta"]:
        puntuacion += 1
        messagebox.showinfo("✔ ¡Correcto!", "¡Respuesta correcta!")
    else:
        messagebox.showerror("✘ Incorrecto", "Respuesta incorrecta.")
    mostrar_pregunta()

def finalizar_juego():
    messagebox.showinfo("Fin del Juego", f"Juego terminado. Tu puntuación final es: {puntuacion}/{total_preguntas}")
    lbl_progreso.config(text="")
    lbl_pregunta.config(text="¡Gracias por jugar!")
    for boton in botones_opciones:
        boton.config(state="disabled")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Sistemas Operativos")
ventana.geometry("700x500")
ventana.config(bg="#6C3483")  # Fondo morado

lbl_titulo = tk.Label(ventana, text="🖥️ Juego de Sistemas Operativos 🖥️", font=("Arial", 20, "bold"), bg="#6C3483", fg="#F7DC6F")  # Letras amarillas
lbl_titulo.pack(pady=10)

lbl_progreso = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#6C3483", fg="#F7DC6F")  # Letras amarillas
lbl_progreso.pack()

lbl_pregunta = tk.Label(ventana, text="Elige un nivel para comenzar", font=("Arial", 14), wraplength=600, justify="center", bg="#6C3483", fg="#F7DC6F")  # Letras amarillas
lbl_pregunta.pack(pady=20)

frame_niveles = tk.Frame(ventana, bg="#6C3483")
frame_niveles.pack(pady=10)

btn_facil = tk.Button(frame_niveles, text="Fácil", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("facil"), bg="#E91E63", fg="white")  # Botón rosado
btn_facil.grid(row=0, column=0, padx=5, pady=5)

btn_medio = tk.Button(frame_niveles, text="Medio", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("medio"), bg="#C2185B", fg="white")  # Rosado oscuro
btn_medio.grid(row=0, column=1, padx=5, pady=5)

btn_dificil = tk.Button(frame_niveles, text="Difícil", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("dificil"), bg="#B71C1C", fg="white")  # Botón rojo
btn_dificil.grid(row=0, column=2, padx=5, pady=5)

botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text="", font=("Arial", 12), width=50, command=lambda b=i: verificar_respuesta(botones_opciones[b].cget("text")), bg="#8E44AD", fg="white")  # Botón morado claro
    boton.pack(pady=5)
    botones_opciones.append(boton)

ventana.mainloop()