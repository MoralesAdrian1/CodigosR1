from machine import Pin, ADC
from time import sleep

# Configuración de pines y ADC
sw = ADC(Pin(34))
vrx = ADC(Pin(35))
vry = ADC(Pin(33))

# Pines de control del motor
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(27, Pin.OUT)  # Se cambió el pin para evitar conflicto con vry
IN4 = Pin(32, Pin.OUT)
pins_motor = [IN1, IN2, IN3, IN4]
sequence_motor = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Atenuación y resolución del ADC
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)
vrx.width(ADC.WIDTH_12BIT)
vry.width(ADC.WIDTH_12BIT)

# Función para girar el motor 90 grados
def girar_motor_90_pasos():
    for _ in range(45):  # Se ajustó el número de iteraciones para 90 grados
        for step in reversed(sequence_motor):
            for i in range(len(pins_motor)):
                pins_motor[i].value(step[i])
                sleep(0.001)

# Función para revertir el giro del motor 90 grados
def revertir_motor_90_pasos():
    for _ in range(45):  # Se ajustó el número de iteraciones para 90 grados
        for step in sequence_motor:
            for i in range(len(pins_motor)):
                pins_motor[i].value(step[i])
                sleep(0.001)

while True:
    valory = vry.read()
    print(valory)

    # Si la lectura del joystick en el eje Y supera un umbral, girar el motor
    if valory > 2000:
        girar_motor_90_pasos()
        sleep(0.1)  # Esperar un poco antes de volver a leer
        revertir_motor_90_pasos()
        sleep(0.1)

