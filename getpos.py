import pyautogui
import time
import keyboard



while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == "'":
        x, y = pyautogui.position()
        print(f'Posição atual do mouse: {x}, {y}')
            
