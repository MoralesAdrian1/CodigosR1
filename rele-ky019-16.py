from machine import Pin, PWM, SoftI2C
from time import sleep

green_pin = 15
blue_pin = 4
red_pin = 16
RELAY_PIN = 22

# Inicializar pin del relé
relay = Pin(RELAY_PIN, Pin.OUT)

green_pwm = PWM(Pin(green_pin), freq=5000)
blue_pwm = PWM(Pin(blue_pin), freq=5000)
red_pwm = PWM(Pin(red_pin), freq=5000)

# Función para conectar a la red WiFi
def mostrar_color(color):
    print(color, 0, 0)

colores = [
    {"nombre": "Rojo", "green": 0, "blue": 0, "red": 1023},
    {"nombre": "Blanco", "green": 1023, "blue": 1023, "red": 1023},
    {"nombre": "Verde", "green": 1023, "blue": 0, "red": 0},
    {"nombre": "Azul", "green": 0, "blue": 1023, "red": 0}
]

while True:
    for color in colores:
        # Verificar si el color actual es azul y activar el relé en consecuencia
        if color["nombre"] == "Azul":
            relay.value(1)  # Activar relé
        else:
            relay.value(0)  # Desactivar relé

        green_pwm.duty(color["green"])
        blue_pwm.duty(color["blue"])
        red_pwm.duty(color["red"])

        mostrar_color(color["nombre"])

        msg = color["nombre"]
        sleep(1)
