import keyboard
import pyautogui
import time

print("Pressione a tecla '...")

# Espera até que a tecla ' seja pressionada
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == "'":
        print("Você pressionou a tecla '")
        pyautogui.moveTo(691,662)
        pyautogui.click()
        print("clicou 1")
        time.sleep(0.1)
        pyautogui.moveTo(1168,787)
        pyautogui.click()
        print("clicou 2")
        time.sleep(0.2)
        