import pyautogui
import time
import keyboard

pos_x_abs = [593,597,608,736,726,722,888,848,869,996,987,989]
pos_y_abs = [398,529,723,717,532,400,407,531,721,714,561,418]

while True:
    event = keyboard.read_event()
    
    
    
    
    if event.event_type == keyboard.KEY_DOWN and event.name == "'":
        
        print ('3 segundos até ativar')
        time.sleep(3)  #clica no jogo
        i = 0
        pyautogui.moveTo(500, 597)
        pyautogui.click()
        print ('ativado')
        for i in range(1):
            i += 1
            time.sleep(1)
            print ('delay 1')
            for i in range(len(pos_y_abs)):  # Substitua 5 pelo número de cliques desejado
                print ("clicando em: x="+str(pos_x_abs[i])+ ", y=" +str(pos_y_abs[i]))
                pyautogui.moveTo(pos_x_abs[i], pos_y_abs[i])
                pyautogui.click()
                time.sleep(1.5)
                pyautogui.moveTo(517, 663)
                pyautogui.click()
                print("clicou 1")
                time.sleep(0.1)
                pyautogui.moveTo(980, 790)
                pyautogui.click()
                print("clicou 2")
                time.sleep(0.1)
                pyautogui.press('esc')
                time.sleep(0.3)
                
            time.sleep(15) 
            
            for i in range(len(pos_y_abs)):  #coletando
                print ("clicando em: x="+str(pos_x_abs[i])+ ", y=" +str(pos_y_abs[i]))
                pyautogui.moveTo(pos_x_abs[i], pos_y_abs[i])
                pyautogui.click()
                pyautogui.press('esc')
                time.sleep(1)
            
            
        