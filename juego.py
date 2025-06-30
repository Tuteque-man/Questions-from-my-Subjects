import tkinter as tk
from tkinter import messagebox
import random

# Lista de preguntas (puedes añadir hasta 100 preguntas aquí)
preguntas = ([
    {
        "pregunta": "¿Qué es un gateway en una red y cuál es su función principal?",
        "respuesta_correcta": "Es un dispositivo que conecta diferentes redes y realiza la traducción de protocolos o el enrutamiento entre ellas",
        "respuestas_falsas": [
            "Es un switch de capa 2",
            "Es un servidor DNS",
            "Es una computadora que solo almacena archivos"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre un firewall de red y un proxy en términos de seguridad?",
        "respuesta_correcta": "El firewall controla el tráfico de red en función de reglas, mientras que el proxy actúa como intermediario en las solicitudes",
        "respuestas_falsas": [
            "El firewall solo bloquea correos electrónicos",
            "El proxy solo funciona en IPv6",
            "No hay diferencia entre ambos"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo SNMP y cómo se usa en la gestión de redes?",
        "respuesta_correcta": "SNMP permite monitorear y administrar dispositivos de red mediante agentes y gestores",
        "respuestas_falsas": [
            "SNMP es un protocolo de enrutamiento",
            "Solo funciona en redes IPv6",
            "No tiene funciones de gestión"
        ]
    },
    {
        "pregunta": "¿Cuál es el propósito de un IDS (Intrusion Detection System) en una red?",
        "respuesta_correcta": "Detectar actividades sospechosas o maliciosas en la red y alertar a los administradores",
        "respuestas_falsas": [
            "Bloquear automáticamente todos los ataques",
            "Reemplazar al firewall",
            "No tiene relación con la seguridad"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre NAT estático y NAT dinámico?",
        "respuesta_correcta": "NAT estático asigna una IP fija a un dispositivo, mientras que NAT dinámico asigna IPs de un grupo según disponibilidad",
        "respuestas_falsas": [
            "NAT estático solo funciona en IPv6",
            "NAT dinámico no requiere configuración",
            "No hay diferencia"
        ]
    },
    {
        "pregunta": "¿Qué es un router de borde y cuál es su función en una red corporativa?",
        "respuesta_correcta": "Es un router que conecta la red interna con Internet u otras redes externas, gestionando el tráfico de entrada y salida",
        "respuestas_falsas": [
            "Es un switch de capa 2",
            "Solo funciona en redes domésticas",
            "No tiene funciones de enrutamiento"
        ]
    },
    {
        "pregunta": "¿Qué es la segmentación de red y cuáles son sus beneficios principales?",
        "respuesta_correcta": "Dividir una red en segmentos para mejorar el rendimiento, la seguridad y la gestión del tráfico",
        "respuestas_falsas": [
            "Es eliminar segmentos de una red",
            "Solo se usa en redes inalámbricas",
            "No tiene beneficios concretos"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo LLQ en QoS y para qué se usa?",
        "respuesta_correcta": "Es una cola de prioridad que garantiza el tratamiento preferencial de ciertos tipos de tráfico, como voz y video",
        "respuestas_falsas": [
            "Es un protocolo de enrutamiento",
            "Se usa solo en IPv6",
            "No tiene relación con QoS"
        ]
    },
    {
        "pregunta": "¿Qué ventajas ofrece el uso de enlaces VPN en comparación con conexiones directas sin cifrado?",
        "respuesta_correcta": "Proporcionan seguridad y confidencialidad en las comunicaciones remotas a través de cifrado y túneles seguros",
        "respuestas_falsas": [
            "Reduce la velocidad de la red",
            "Solo funciona en redes IPv6",
            "No ofrecen beneficios de seguridad"
        ]
    },
    {
        "pregunta": "¿Qué es una topología de red en estrella y cuáles son sus ventajas?",
        "respuesta_correcta": "Es una estructura donde todos los dispositivos se conectan a un switch o hub central, facilitando la gestión y aislando fallos",
        "respuestas_falsas": [
            "Es una topología en anillo",
            "No tiene ventajas",
            "Es la menos confiable"
        ]
    },
    {
        "pregunta": "¿Qué es un gateway y su función?",
        "respuesta_correcta": "Conectar redes y traducir protocolos",
        "respuestas_falsas": [
            "Es un switch",
            "Es un servidor DNS",
            "Es una computadora para archivos"
        ]
    },
    {
        "pregunta": "Diferencia entre firewall y proxy",
        "respuesta_correcta": "Firewall controla tráfico, proxy intermedia",
        "respuestas_falsas": [
            "Firewall bloquea correos",
            "Proxy solo funciona con IPv6",
            "Son iguales"
        ]
    },
    {
        "pregunta": "Uso del protocolo SNMP",
        "respuesta_correcta": "Monitorear y administrar redes",
        "respuestas_falsas": [
            "Es de enrutamiento",
            "Solo funciona con IPv6",
            "No gestiona redes"
        ]
    },
    {
        "pregunta": "Propósito del IDS en la red",
        "respuesta_correcta": "Detectar actividad maliciosa",
        "respuestas_falsas": [
            "Bloquear ataques",
            "Reemplaza al firewall",
            "No está relacionado con seguridad"
        ]
    },
    {
        "pregunta": "Diferencia entre NAT estático y dinámico",
        "respuesta_correcta": "Estático fija IP, dinámico usa grupo",
        "respuestas_falsas": [
            "Estático solo IPv6",
            "Dinámico no requiere configuración",
            "Son iguales"
        ]
    },
    {
        "pregunta": "¿Qué hace un router de borde?",
        "respuesta_correcta": "Conectar red interna con externa",
        "respuestas_falsas": [
            "Es un switch",
            "Solo redes domésticas",
            "No enruta tráfico"
        ]
    },
    {
        "pregunta": "¿Qué es la segmentación de red?",
        "respuesta_correcta": "Mejorar rendimiento y seguridad",
        "respuestas_falsas": [
            "Eliminar segmentos",
            "Solo en redes inalámbricas",
            "Sin beneficios"
        ]
    },
    {
        "pregunta": "¿Qué es LLQ en QoS?",
        "respuesta_correcta": "Prioridad para tráfico crítico",
        "respuestas_falsas": [
            "Es de enrutamiento",
            "Solo IPv6",
            "No relacionado con QoS"
        ]
    },
    {
        "pregunta": "Ventajas de enlaces VPN",
        "respuesta_correcta": "Seguridad y privacidad",
        "respuestas_falsas": [
            "Reduce velocidad",
            "Solo IPv6",
            "Sin beneficios"
        ]
    },
    {
        "pregunta": "¿Qué es la topología en estrella?",
        "respuesta_correcta": "Conexión centralizada",
        "respuestas_falsas": [
            "Es un anillo",
            "No tiene ventajas",
            "Es poco confiable"
        ]
    },
    {
        "pregunta": "¿Qué es la encapsulación en redes?",
        "respuesta_correcta": "Envuelve datos en capas OSI",
        "respuestas_falsas": [
            "Solo en IPv6",
            "No afecta la transmisión",
            "Es cifrado"
        ]
    },
    {
        "pregunta": "Función del protocolo DHCP en Wi-Fi",
        "respuesta_correcta": "Asignar IPs automáticamente",
        "respuestas_falsas": [
            "Solo en redes cableadas",
            "No funciona con Wi-Fi",
            "No asigna IPs"
        ]
    },
    {
        "pregunta": "¿Qué es un enlace de redundancia?",
        "respuesta_correcta": "Mantiene conexión si falla el enlace",
        "respuestas_falsas": [
            "Es respaldo de energía",
            "Solo en inalámbricos",
            "No evita fallos"
        ]
    },
    {
        "pregunta": "Aspectos clave en redes IoT",
        "respuesta_correcta": "Seguridad y escalabilidad",
        "respuestas_falsas": [
            "Solo más ancho de banda",
            "Sin consideraciones especiales",
            "Solo IPv4"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre VLAN y subred?",
        "respuesta_correcta": "VLAN segmenta en capa 2, subred en capa 3",
        "respuestas_falsas": [
            "Son iguales",
            "Solo en IPv6",
            "Subred no segmenta"
        ]
    },
    {
        "pregunta": "¿Qué es el modelo OSI y para qué sirve?",
        "respuesta_correcta": "Estandariza cómo transmitir datos",
        "respuestas_falsas": [
            "Es un protocolo de enrutamiento",
            "Solo sirve en redes locales",
            "No tiene aplicación práctica"
        ]
    },
    {
        "pregunta": "¿Qué función cumple el protocolo ARP?",
        "respuesta_correcta": "Resuelve IPs a MAC",
        "respuestas_falsas": [
            "Traduce nombres de dominio",
            "Asigna IPs automáticamente",
            "Bloquea tráfico no deseado"
        ]
    },
    {
        "pregunta": "¿Qué es un switch gestionado?",
        "respuesta_correcta": "Optimiza tráfico y seguridad",
        "respuestas_falsas": [
            "Solo conecta dispositivos",
            "No tiene funciones avanzadas",
            "Es igual a un router"
        ]
    },
    {
        "pregunta": "¿Cómo se realiza el ping?",
        "respuesta_correcta": "Mide conectividad con ICMP",
        "respuestas_falsas": [
            "Usa DNS para nombres",
            "Comprueba velocidad de red",
            "No mide conectividad"
        ]
    },
    {
        "pregunta": "¿Qué es una dirección IP privada?",
        "respuesta_correcta": "Usada solo en redes locales",
        "respuestas_falsas": [
            "Visible en Internet",
            "Es exclusiva para servidores",
            "No tiene límite de uso"
        ]
    },
    {
        "pregunta": "¿Qué es una dirección IP pública?",
        "respuesta_correcta": "Visible en Internet",
        "respuestas_falsas": [
            "Usada solo en redes locales",
            "Exclusiva para servidores",
            "No requiere seguridad"
        ]
    },
    {
        "pregunta": "¿Qué hace un servidor DNS?",
        "respuesta_correcta": "Traduce nombres a IPs",
        "respuestas_falsas": [
            "Asigna IPs automáticamente",
            "Bloquea tráfico malicioso",
            "Almacena archivos"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo FTP?",
        "respuesta_correcta": "Transfiere archivos entre dispositivos",
        "respuestas_falsas": [
            "Proporciona seguridad en redes",
            "Monitorea tráfico de red",
            "Asigna direcciones IP"
        ]
    },
    {
        "pregunta": "¿Qué ventaja tiene el cable UTP?",
        "respuesta_correcta": "Es económico y versátil",
        "respuestas_falsas": [
            "Es inmune a interferencias",
            "Solo para redes inalámbricas",
            "No transmite datos rápido"
        ]
    },
    {
        "pregunta": "¿Qué es una máscara de subred?",
        "respuesta_correcta": "Define el rango de IPs de una red",
        "respuestas_falsas": [
            "Es un protocolo de seguridad",
            "Traduce nombres de dominio",
            "Solo funciona en redes IPv6"
        ]
    },
    {
        "pregunta": "¿Qué es el enrutamiento dinámico?",
        "respuesta_correcta": "Actualiza rutas automáticamente",
        "respuestas_falsas": [
            "Requiere configuración manual",
            "Solo en redes locales",
            "Es menos eficiente que estático"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo ICMP?",
        "respuesta_correcta": "Envía mensajes de diagnóstico",
        "respuestas_falsas": [
            "Asigna direcciones IP",
            "Es exclusivo de IPv6",
            "Detecta intrusiones"
        ]
    },
    {
        "pregunta": "¿Qué hace un switch en la red?",
        "respuesta_correcta": "Conecta y segmenta dispositivos",
        "respuestas_falsas": [
            "Asigna IPs automáticamente",
            "Bloquea tráfico no deseado",
            "Detecta ataques"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre TCP y UDP?",
        "respuesta_correcta": "TCP es confiable, UDP más rápido",
        "respuestas_falsas": [
            "Son iguales",
            "UDP asigna IPs",
            "TCP no asegura entrega"
        ]
    },
    {
        "pregunta": "¿Qué es una red LAN?",
        "respuesta_correcta": "Red local de dispositivos",
        "respuestas_falsas": [
            "Red de larga distancia",
            "Conexión solo inalámbrica",
            "Red exclusiva de servidores"
        ]
    },
    {
        "pregunta": "¿Qué hace un firewall?",
        "respuesta_correcta": "Controla tráfico según reglas",
        "respuestas_falsas": [
            "Traduce nombres de dominio",
            "Conecta dispositivos",
            "Detecta intrusiones automáticamente"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo HTTP?",
        "respuesta_correcta": "Permite la transferencia de páginas web",
        "respuestas_falsas": [
            "Monitorea tráfico de red",
            "Configura dispositivos",
            "Cifra comunicaciones"
        ]
    },
    {
        "pregunta": "¿Qué es una red WAN?",
        "respuesta_correcta": "Red de larga distancia",
        "respuestas_falsas": [
            "Red local",
            "Solo conexión inalámbrica",
            "Red de servidores"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo DNS?",
        "respuesta_correcta": "Resuelve nombres en IPs",
        "respuestas_falsas": [
            "Asigna direcciones IP",
            "Envía mensajes de diagnóstico",
            "Detecta actividad maliciosa"
        ]
    },
    {
        "pregunta": "¿Qué hace el protocolo VPN?",
        "respuesta_correcta": "Cifra conexiones remotas",
        "respuestas_falsas": [
            "Detecta intrusiones",
            "Configura redes locales",
            "Asigna IPs automáticamente"
        ]
    },
    {
        "pregunta": "¿Qué es una red en malla?",
        "respuesta_correcta": "Todos los nodos se conectan entre sí",
        "respuestas_falsas": [
            "Solo funciona con un hub",
            "Es igual a una topología estrella",
            "No tiene redundancia"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo POP3?",
        "respuesta_correcta": "Recibe correos en el cliente",
        "respuestas_falsas": [
            "Envía correos desde servidores",
            "Cifra correos electrónicos",
            "Monitorea tráfico de red"
        ]
    },
    {
        "pregunta": "¿Qué es el cable de fibra óptica?",
        "respuesta_correcta": "Transmite datos mediante luz",
        "respuestas_falsas": [
            "Es inmune a interferencias",
            "Es igual al cable coaxial",
            "Es económico y versátil"
        ]
    },
    {
        "pregunta": "¿Qué hace un servidor proxy?",
        "respuesta_correcta": "Intermedia solicitudes de red",
        "respuestas_falsas": [
            "Controla tráfico según reglas",
            "Asigna direcciones IP",
            "Monitorea dispositivos"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo IMAP?",
        "respuesta_correcta": "Accede correos en el servidor",
        "respuestas_falsas": [
            "Recibe correos en el cliente",
            "Envía correos electrónicos",
            "Monitorea tráfico de red"
        ]
    },
    {
        "pregunta": "¿Qué hace una red VLAN?",
        "respuesta_correcta": "Segmenta en capa 2",
        "respuestas_falsas": [
            "Conecta diferentes redes",
            "Segmenta en capa 3",
            "Configura automáticamente dispositivos"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo SSH?",
        "respuesta_correcta": "Cifra conexiones remotas",
        "respuestas_falsas": [
            "Envía correos electrónicos",
            "Configura redes locales",
            "Detecta actividad sospechosa"
        ]
    },
    {
        "pregunta": "¿Qué hace un hub en la red?",
        "respuesta_correcta": "Conecta dispositivos en red",
        "respuestas_falsas": [
            "Asigna IPs automáticamente",
            "Envía mensajes de diagnóstico",
            "Segmenta en capa 2"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre IPv4 e IPv6?",
        "respuesta_correcta": "IPv6 soporta más dispositivos",
        "respuestas_falsas": [
            "IPv6 es más lento",
            "Son iguales",
            "IPv4 solo funciona en LAN"
        ]
    },
    {
        "pregunta": "¿Qué es un ataque de phishing?",
        "respuesta_correcta": "Robo de datos mediante engaño",
        "respuestas_falsas": [
            "Ataque DDoS",
            "Intrusión directa en sistemas",
            "Deshabilitar servicios"
        ]
    },
    {
        "pregunta": "¿Qué hace el protocolo SMTP?",
        "respuesta_correcta": "Envía correos electrónicos",
        "respuestas_falsas": [
            "Recibe correos en el cliente",
            "Cifra conexiones remotas",
            "Configura redes locales"
        ]
    },
    {
        "pregunta": "¿Qué es un switch no gestionado?",
        "respuesta_correcta": "Conecta dispositivos sin configurar",
        "respuestas_falsas": [
            "Segmenta en capa 3",
            "Controla tráfico según reglas",
            "Monitorea redes automáticamente"
        ]
    },
    {
        "pregunta": "¿Qué hace un ataque DDoS?",
        "respuesta_correcta": "Satura servicios con tráfico",
        "respuestas_falsas": [
            "Bloquea correos electrónicos",
            "Roba datos mediante engaño",
            "Deshabilita el firewall"
        ]
    },
    {
        "pregunta": "¿Qué es un servidor web?",
        "respuesta_correcta": "Aloja páginas web",
        "respuestas_falsas": [
            "Configura redes locales",
            "Traduce nombres de dominio",
            "Asigna IPs automáticamente"
        ]
    },
    {
        "pregunta": "¿Qué hace el protocolo TELNET?",
        "respuesta_correcta": "Gestiona dispositivos remotamente",
        "respuestas_falsas": [
            "Cifra conexiones",
            "Detecta ataques de red",
            "Asigna direcciones IP"
        ]
    },
    {
        "pregunta": "¿Es válida la dirección IP 192.168.1.300?",
        "respuesta_correcta": "Falso",
        "respuestas_falsas": ["Verdadero", "No aplica en redes IPv4", "Es una dirección de broadcast"]
    },
    {
        "pregunta": "¿Es válida la dirección IP 10.0.0.1?",
        "respuesta_correcta": "Verdadero",
        "respuestas_falsas": ["Falso", "No está en rango privado", "Es exclusiva de IPv6"]
    },
    {
        "pregunta": "¿Es válida la máscara de subred 255.255.255.255?",
        "respuesta_correcta": "Verdadero",
        "respuestas_falsas": ["Falso", "No se utiliza en redes privadas", "Es exclusiva de IPv6"]
    },
    {
        "pregunta": "¿Es válida la dirección IP 172.16.256.1?",
        "respuesta_correcta": "Falso",
        "respuestas_falsas": ["Verdadero", "Es una IP pública", "No pertenece a redes IPv4"]
    },
    {
        "pregunta": "¿Es privada la dirección IP 192.168.0.1?",
        "respuesta_correcta": "Verdadero",
        "respuestas_falsas": ["Falso", "Es pública", "No pertenece al rango privado"]
    },
    {
        "pregunta": "¿Es pública la dirección IP 8.8.8.8?",
        "respuesta_correcta": "Verdadero",
        "respuestas_falsas": ["Falso", "Es privada", "Solo funciona en redes locales"]
    },
    {
        "pregunta": "¿Es válida una dirección IP que termina en .0?",
        "respuesta_correcta": "Falso",
        "respuestas_falsas": ["Verdadero", "Solo en redes IPv6", "Es una dirección multicast"]
    },
    {
        "pregunta": "¿Es válida la dirección 256.0.0.1 en IPv4?",
        "respuesta_correcta": "Falso",
        "respuestas_falsas": ["Verdadero", "Es exclusiva de redes locales", "Es una dirección de broadcast"]
    },
    {
        "pregunta": "¿Cuántos bits tiene una dirección IPv4?",
        "respuesta_correcta": "32",
        "respuestas_falsas": ["64", "128", "48"]
    },
    {
        "pregunta": "¿Una IP en la subred 192.168.1.0/24 puede ser 192.168.1.100?",
        "respuesta_correcta": "Verdadero",
        "respuestas_falsas": ["Falso", "No pertenece al rango", "Es una dirección de broadcast"]
    },
    {
        "pregunta": "¿Qué es una dirección MAC?",
        "respuesta_correcta": "Identifica un dispositivo en la red",
        "respuestas_falsas": [
            "Traduce nombres de dominio",
            "Asigna direcciones IP",
            "Es igual a una dirección IP"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo FTP?",
        "respuesta_correcta": "Transfiere archivos entre dispositivos",
        "respuestas_falsas": [
            "Proporciona seguridad en redes",
            "Monitorea tráfico de red",
            "Asigna IPs automáticamente"
        ]
    },
    {
        "pregunta": "¿Qué función tiene un switch gestionado?",
        "respuesta_correcta": "Segmenta redes y mejora tráfico",
        "respuestas_falsas": [
            "Asigna IPs automáticamente",
            "Solo conecta dispositivos",
            "Detecta ataques"
        ]
    },
    {
        "pregunta": "¿Qué es el protocolo DHCP?",
        "respuesta_correcta": "Asigna IPs automáticamente",
        "respuestas_falsas": [
            "Detecta intrusiones",
            "Monitorea redes",
            "Cifra datos"
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre IPv4 e IPv6?",
        "respuesta_correcta": "IPv6 permite más dispositivos",
        "respuestas_falsas": [
            "IPv6 es más lento",
            "Son iguales",
            "IPv4 solo funciona en LAN"
        ]
    },
    {
        "pregunta": "¿Qué hace un ataque DDoS?",
        "respuesta_correcta": "Satura servicios con tráfico",
        "respuestas_falsas": [
            "Bloquea correos electrónicos",
            "Roba datos mediante engaño",
            "Deshabilita el firewall"
        ]
    },
    {
        "pregunta": "¿Qué es una máscara de subred?",
        "respuesta_correcta": "Define el rango de IPs de una red",
        "respuestas_falsas": [
            "Es un protocolo de seguridad",
            "Solo funciona en IPv6",
            "Traduce nombres de dominio"
        ]
    },
    {
        "pregunta": "¿Qué es el modelo OSI?",
        "respuesta_correcta": "Estandariza la transmisión de datos",
        "respuestas_falsas": [
            "Solo sirve en redes locales",
            "Es un protocolo de enrutamiento",
            "No tiene aplicación práctica"
        ]
    },
    {
        "pregunta": "¿Qué hace el protocolo ARP?",
        "respuesta_correcta": "Resuelve IPs a MAC",
        "respuestas_falsas": [
            "Detecta intrusiones",
            "Asigna IPs automáticamente",
            "Bloquea tráfico malicioso"
        ]
    },
    {
        "pregunta": "¿Qué es el enrutamiento dinámico?",
        "respuesta_correcta": "Actualiza rutas automáticamente",
        "respuestas_falsas": [
            "Requiere configuración manual",
            "Solo en redes locales",
            "Es menos eficiente que estático"
        ]
    }
    
])

# Variables globales
puntuacion = 0
preguntas_seleccionadas = random.sample(preguntas, 10)  # Seleccionar 10 preguntas aleatorias
pregunta_actual = None
progreso_actual = 0
total_preguntas = 10

# Lógica del juego
def mostrar_pregunta():
    global pregunta_actual, progreso_actual
    if preguntas_seleccionadas:
        pregunta_actual = preguntas_seleccionadas.pop()  # Tomar una pregunta
        opciones = [pregunta_actual["respuesta_correcta"]] + pregunta_actual["respuestas_falsas"]
        random.shuffle(opciones)  # Mezclar opciones

        # Mostrar progreso
        progreso_actual += 1
        lbl_progreso.config(text=f"Pregunta {progreso_actual} de {total_preguntas}")

        # Ajustar el tamaño del cuadro según el texto
        lbl_pregunta.config(text=pregunta_actual["pregunta"])
        lbl_pregunta.update_idletasks()  # Ajustar tamaño dinámico

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
    # Mostrar puntuación final en un cuadro emergente
    messagebox.showinfo("Fin del Juego", f"Juego terminado. Tu puntuación final es: {puntuacion}/{total_preguntas}")
    
    # Mostrar puntuación final en la pantalla del juego
    lbl_progreso.config(text="")
    lbl_pregunta.config(text="¡Gracias por jugar!")
    
    lbl_puntuacion_final = tk.Label(ventana, text=f"Tu puntuación final es: {puntuacion}/{total_preguntas}",
                                    font=("Arial", 16, "bold"), bg="#1B2631", fg="#F1C40F")  # Dorado vibrante
    lbl_puntuacion_final.pack(pady=20)
    
    # Deshabilitar los botones de respuesta
    for boton in botones_opciones:
        boton.config(state="disabled")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Redes")
ventana.geometry("700x500")  # Aumenté ligeramente la altura para más espacio
ventana.config(bg="#1B2631")  # Fondo oscuro tecnológico

# Widgets de la interfaz
lbl_titulo = tk.Label(ventana, text="🎮 Juego de Redes 🎮", font=("Arial", 20, "bold"), bg="#1B2631", fg="#F1C40F")  # Dorado vibrante
lbl_titulo.pack(pady=10)

lbl_progreso = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#1B2631", fg="#85C1E9")  # Azul claro para el progreso
lbl_progreso.pack()

lbl_pregunta = tk.Label(ventana, text="", font=("Arial", 14), wraplength=600, justify="center", bg="#1B2631", fg="#A9DFBF")  # Verde tecnológico
lbl_pregunta.pack(pady=20)

botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text="", font=("Arial", 12), width=50, command=lambda b=i: verificar_respuesta(botones_opciones[b].cget("text")), bg="#2E86C1", fg="white")  # Azul neón
    boton.pack(pady=5)
    botones_opciones.append(boton)

# Iniciar el juego
mostrar_pregunta()
ventana.mainloop()