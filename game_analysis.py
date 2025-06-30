import tkinter as tk
from tkinter import messagebox
import random

# Base de preguntas por dificultad
preguntas = {
  "facil": [
    {
      "pregunta": "¿Qué significa DRY en el desarrollo de software?",
      "respuesta_correcta": "Don't Repeat Yourself",
      "respuestas_falsas": ["Duplicate Resource Yield", "Dynamic Repetitive Yield", "Do Repeat Yourself"]
    },
    {
      "pregunta": "¿Qué metodología utiliza Sprints?",
      "respuesta_correcta": "SCRUM",
      "respuestas_falsas": ["Kanban", "Waterfall", "XP"]
    },
    {
      "pregunta": "¿Qué principio indica que una clase debe tener una sola responsabilidad?",
      "respuesta_correcta": "Single Responsibility Principle",
      "respuestas_falsas": ["Open/Closed Principle", "Dependency Inversion Principle", "Interface Segregation Principle"]
    },
    {
      "pregunta": "¿Qué hace el tablero Kanban?",
      "respuesta_correcta": "Visualiza el flujo de trabajo",
      "respuestas_falsas": ["Organiza reuniones diarias", "Prioriza requisitos", "Divide ciclos de desarrollo"]
    },
    {
      "pregunta": "¿Qué se hace en la etapa de codificación?",
      "respuesta_correcta": "Traducir el diseño a código",
      "respuestas_falsas": ["Recolectar requisitos", "Definir reglas de negocio", "Crear diagramas UML"]
    },
    {
      "pregunta": "¿Qué metodología utiliza límites WIP?",
      "respuesta_correcta": "Kanban",
      "respuestas_falsas": ["SCRUM", "Agile", "Waterfall"]
    },
    {
      "pregunta": "¿Qué es un Sprint en SCRUM?",
      "respuesta_correcta": "Un ciclo de desarrollo breve",
      "respuestas_falsas": ["Una reunión diaria", "Un tablero Kanban", "Una lista de requisitos"]
    },
    {
      "pregunta": "¿Qué principio sugiere mantener el código simple?",
      "respuesta_correcta": "KISS",
      "respuestas_falsas": ["DRY", "SOLID", "OCP"]
    }
  ],
  "medio": [
    {
      "pregunta": "¿Quién representa al cliente en SCRUM?",
      "respuesta_correcta": "Product Owner",
      "respuestas_falsas": ["Scrum Master", "Development Team", "Stakeholder"]
    },
    {
      "pregunta": "¿Qué principio indica que el código debe estar abierto a extensiones pero cerrado a modificaciones?",
      "respuesta_correcta": "Open/Closed Principle",
      "respuestas_falsas": ["Single Responsibility Principle", "Liskov Substitution Principle", "Dependency Inversion Principle"]
    },
    {
      "pregunta": "¿Qué es un backlog en SCRUM?",
      "respuesta_correcta": "Lista priorizada de requisitos",
      "respuestas_falsas": ["Tablero de tareas", "Revisión del sprint", "Planificación del producto"]
    },
    {
      "pregunta": "¿Qué herramienta es ideal para visualizar el flujo de trabajo?",
      "respuesta_correcta": "Kanban",
      "respuestas_falsas": ["Jira", "SCRUM", "Waterfall"]
    },
    {
      "pregunta": "¿Qué tipo de pruebas garantizan que una función específica funcione correctamente?",
      "respuesta_correcta": "Pruebas Unitarias",
      "respuestas_falsas": ["Pruebas de Integración", "Pruebas de Aceptación", "Pruebas Funcionales"]
    },
    {
      "pregunta": "¿Qué principio SOLID indica que las clases derivadas deben ser intercambiables por sus clases base?",
      "respuesta_correcta": "Liskov Substitution Principle",
      "respuestas_falsas": ["Interface Segregation Principle", "Dependency Inversion Principle", "Single Responsibility Principle"]
    },
    {
      "pregunta": "¿Qué se hace en la etapa de diseño?",
      "respuesta_correcta": "Estructurar la solución técnica",
      "respuestas_falsas": ["Crear diagramas de flujo", "Recolectar requisitos", "Probar el sistema"]
    },
    {
      "pregunta": "¿Qué es el Product Backlog en SCRUM?",
      "respuesta_correcta": "Lista priorizada de requisitos",
      "respuestas_falsas": ["Tablero de tareas", "Revisión del sprint", "Planificación del producto"]
    }
  ],
  "dificil": [
    {
      "pregunta": "¿Qué significa el principio KISS?",
      "respuesta_correcta": "Mantén el código simple",
      "respuestas_falsas": ["Simplifica procesos críticos", "Diseña complejidades avanzadas", "Duplicación de lógica"]
    },
    {
      "pregunta": "¿Qué indica el principio Open/Closed?",
      "respuesta_correcta": "El código debe estar abierto a extensiones pero cerrado a modificaciones",
      "respuestas_falsas": ["Cada clase debe tener una responsabilidad única", "Los módulos de bajo nivel dependen de los de alto nivel", "Mejora gradual del flujo de trabajo"]
    },
    {
      "pregunta": "¿Qué metodología utiliza límites WIP?",
      "respuesta_correcta": "Kanban",
      "respuestas_falsas": ["SCRUM", "Agile", "Waterfall"]
    },
    {
      "pregunta": "¿Qué hace el Scrum Master en SCRUM?",
      "respuesta_correcta": "Eliminar obstáculos y guiar al equipo",
      "respuestas_falsas": ["Representar al cliente", "Planificar tareas", "Priorizar requisitos"]
    },
    {
      "pregunta": "¿Qué pruebas se realizan para verificar la interacción entre módulos?",
      "respuesta_correcta": "Pruebas de Integración",
      "respuestas_falsas": ["Pruebas Unitarias", "Pruebas de Aceptación", "Pruebas Funcionales"]
    },
    {
      "pregunta": "¿Qué define el Liskov Substitution Principle?",
      "respuesta_correcta": "Las clases derivadas deben ser intercambiables por sus clases base",
      "respuestas_falsas": ["Las clases deben depender de abstracciones", "Evitar duplicación de lógica", "Los módulos deben ser abiertos a extensión"]
    },
    {
      "pregunta": "¿Qué tareas se realizan en la etapa de implementación?",
      "respuesta_correcta": "Despliegue del software",
      "respuestas_falsas": ["Codificación del sistema", "Pruebas Unitarias", "Recolección de requisitos"]
    },
    {
      "pregunta": "¿Qué herramienta utiliza un tablero Kanban para visualizar tareas?",
      "respuesta_correcta": "Trello",
      "respuestas_falsas": ["Jira", "SCRUM", "Excel"]
    }
  ]
}

# Variables globales
puntuacion = 0
preguntas_seleccionadas = []
pregunta_actual = None
progreso_actual = 0
total_preguntas = 5
opcion_seleccionada = 0  # Índice de la opción actualmente resaltada

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
    global pregunta_actual, progreso_actual, opcion_seleccionada
    if preguntas_seleccionadas:
        pregunta_actual = preguntas_seleccionadas.pop()
        opciones = [pregunta_actual["respuesta_correcta"]] + pregunta_actual["respuestas_falsas"]
        random.shuffle(opciones)
        progreso_actual += 1
        opcion_seleccionada = 0  # Reiniciar la opción seleccionada
        lbl_progreso.config(text=f"Pregunta {progreso_actual} de {total_preguntas}")
        lbl_pregunta.config(text=pregunta_actual["pregunta"])
        for i, opcion in enumerate(opciones):
            botones_opciones[i].config(text=opcion, state="normal", wraplength=450, bg="#8E44AD")
        resaltar_opcion()
    else:
        finalizar_juego()

def resaltar_opcion():
    """Resalta la opción seleccionada actualmente."""
    for i, boton in enumerate(botones_opciones):
        if i == opcion_seleccionada:
            boton.config(bg="#F7DC6F", fg="black")  # Resaltar en amarillo
        else:
            boton.config(bg="#8E44AD", fg="white")  # Resetear a morado

def mover_opcion(event):
    """Mueve el resaltado entre las opciones usando teclas arriba y abajo."""
    global opcion_seleccionada
    if event.keysym == "Up":
        opcion_seleccionada = (opcion_seleccionada - 1) % len(botones_opciones)
    elif event.keysym == "Down":
        opcion_seleccionada = (opcion_seleccionada + 1) % len(botones_opciones)
    resaltar_opcion()

def verificar_respuesta_seleccionada(event=None):
    """Verifica la respuesta seleccionada al presionar Enter."""
    verificar_respuesta(botones_opciones[opcion_seleccionada].cget("text"))

def verificar_respuesta(opcion):
    global puntuacion
    if opcion == pregunta_actual["respuesta_correcta"]:
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
ventana.title("Juego de Metodologías y Principios de Software")
ventana.geometry("800x600")
ventana.config(bg="#283747")  # Fondo azul oscuro

lbl_titulo = tk.Label(ventana, text="🖥️ Juego de Metodologías de Desarrollo 🖥️", font=("Arial", 20, "bold"), bg="#283747", fg="#F7DC6F")
lbl_titulo.pack(pady=10)

lbl_progreso = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#283747", fg="#F7DC6F")
lbl_progreso.pack()

lbl_pregunta = tk.Label(ventana, text="Elige un nivel para comenzar", font=("Arial", 14), wraplength=600, justify="center", bg="#283747", fg="#F7DC6F")
lbl_pregunta.pack(pady=20)

frame_niveles = tk.Frame(ventana, bg="#283747")
frame_niveles.pack(pady=10)

btn_facil = tk.Button(frame_niveles, text="Fácil", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("facil"), bg="#1ABC9C", fg="white")
btn_facil.grid(row=0, column=0, padx=5, pady=5)

btn_medio = tk.Button(frame_niveles, text="Medio", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("medio"), bg="#27AE60", fg="white")
btn_medio.grid(row=0, column=1, padx=5, pady=5)

btn_dificil = tk.Button(frame_niveles, text="Difícil", font=("Arial", 12), width=15, command=lambda: seleccionar_dificultad("dificil"), bg="#2C3E50", fg="white")
btn_dificil.grid(row=0, column=2, padx=5, pady=5)

botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text="", font=("Arial", 12), width=50, command=lambda b=i: verificar_respuesta(botones_opciones[b].cget("text")), bg="#8E44AD", fg="white")
    boton.pack(pady=5)
    botones_opciones.append(boton)

# Vincular teclas
ventana.bind("<Up>", mover_opcion)
ventana.bind("<Down>", mover_opcion)
ventana.bind("<Return>", verificar_respuesta_seleccionada)

ventana.mainloop()
