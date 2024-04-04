from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient
  

Pin_Led = 2  
Pin_Sensor = 14  

led = Pin(Pin_Led, Pin.OUT)
sensor = Pin(Pin_Sensor, Pin.IN)

# Configuración de la pantalla OLED
i2c = I2C(scl=Pin(22), sda=Pin(21))  # Cambia los pines SCL y SDA según tu configuración
oled_width = 128
oled_height = 64

MQTT_BROKER = "localhost"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/adr/ky-021"
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Megacable_LWHJBnu', 'XL7fcpNPsmcmuxzCPR')  
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")

def publicar_mensaje(msg):
    client.publish(MQTT_TOPIC, msg)

def verificar_magnetismo():
    while True:
        magnetismo = sensor.value()  # Lee el valor del sensor (0 o 1)

        if magnetismo == 0:

            publicar_mensaje(b'true')

        else:

            print("No hay campo magnetico detectado")

            publicar_mensaje(b'false')
        time.sleep(5)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()
verificar_magnetismo()