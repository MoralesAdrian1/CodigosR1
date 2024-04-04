from machine import Pin, SoftI2C

from time import sleep
import network
from umqtt.simple import MQTTClient

digitalPin = 15
digital_pin = Pin(digitalPin, Pin.IN)

MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/adr/ky-036"
MQTT_PORT = 1883

def llegada_mensaje(topic, msg):
    print("Mensaje recibido:", msg)

def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
                        MQTT_BROKER, 
                        user=MQTT_USER,
                        password=MQTT_PASSWORD)
    client.set_callback(llegada_mensaje)  # Configurar la función de devolución de llamada
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a %s, en el topico %s" % (MQTT_BROKER, MQTT_TOPIC))
    return client

# Función para conectar a la red WiFi
def conectar_wifi():
    print("Conectando a WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Megacable_LWHJBnu', 'XL7fcpNPsmcmuxzCPR')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.1)
    print("  Connected!  ")

conectar_wifi()
client = subscribir()

while True:
    digital_val = digital_pin.value()

    if digital_val > 0:
        msg = b'true'
        print("Tocando", 0, 0)
    else:
        msg = b'false'
        print("Libre", 0, 0)
        
    client.publish(MQTT_TOPIC, msg)
    sleep(2)