import machine
import time

# Definir el pin del módulo de golpes
tap_module_pin = 34

# Definir el pin del servo
servo_pin = 14 
servo_pwm = machine.PWM(machine.Pin(servo_pin), freq=50)

# Función para leer el valor del módulo de golpes
def read_tap_module():
    tap_value = machine.Pin(tap_module_pin, machine.Pin.IN)
    return tap_value.value()

# Función para mover el servo a una posición específica
def move_servo(angle):
    duty = int(40 + (angle / 180) * 115)  # Convertir el ángulo a valor de duty cycle (rango: 40-155)
    servo_pwm.duty(duty)

# Bucle principal
while True:
    tap_val = read_tap_module()
    # Determinar la acción basada en el valor del módulo de golpes
    if tap_val == 1:  # Se ha detectado un golpe
        print("Movimiento detectado")
        move_servo(0)  # Mover el servo a la posición deseada cuando se detecte un golpe
    else:
        print("No se Movimiento golpe")
        move_servo(90)  # Mover el servo a la posición central cuando no se detecte un golpe
    time.sleep(0.1)  # Pequeña pausa para suavizar el movimiento