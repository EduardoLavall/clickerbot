import pyautogui
import time

# Pausa entre as ações (opcional)
#pyautogui.PAUSE = 1
pos_x_abs = [2674,2674,2681,2687,2747,2740,2743,2737,2741,2794,2794,2792,2787,2785,2852,2857,2857,2865,2852,2905,2905,2906,2911,2903,2969,2973,2968,2968,2969,3038,3033,3027,3022,]
pos_y_abs = [650,587,529,477,473,532,587,652,700,698,642,585,531,467,479,533,594,643,706,698,640,593,530,475,491,548,601,653,697,653,595,538,486]


# Defina a posição X, Y onde o clique deve ocorrer
#posicao_x = 100  # Substitua com a coordenada X desejada
#posicao_y = 200  # Substitua com a coordenada Y desejada

# Tempo antes do clique (para dar tempo de posicionar a janela)
#time.sleep(5)

# Mova o mouse para a posição e clique
#
#pyautogui.click()



# Repetir o clique várias vezes (opcional)
time.sleep(3)  
i = 0
pyautogui.moveTo(2674, 650)
pyautogui.click()



for i in range(3):
    time.sleep(1)
    pyautogui.press('1')
    for i in range(len(pos_y_abs)):  # Substitua 5 pelo número de cliques desejado
        print ("clicando em: x="+str(pos_x_abs[i])+ ", y=" +str(pos_y_abs[i]))
        pyautogui.moveTo(pos_x_abs[i], pos_y_abs[i])

        pyautogui.click()
        i += 1
        time.sleep(0.25)

    time.sleep(0.5)    
    print ("Regando..........")
    pyautogui.press('5')
    for i in range(len(pos_y_abs)):  # Substitua 5 pelo número de cliques desejado
        print ("clicando em: x="+str(pos_x_abs[i])+ ", y=" +str(pos_y_abs[i]))
        pyautogui.moveTo(pos_x_abs[i], pos_y_abs[i])

        pyautogui.click()
        i += 1
        time.sleep(0.25)

    print ("AGUARDANDO 50s..........")   
    time.sleep(55)
    print ("Colhendo..........")    
    pyautogui.press('6')

    for i in range(len(pos_y_abs)):  # Substitua 5 pelo número de cliques desejado
        print ("clicando em: x="+str(pos_x_abs[i])+ ", y=" +str(pos_y_abs[i]))
        pyautogui.moveTo(pos_x_abs[i], pos_y_abs[i])

        pyautogui.click()
        i += 1
        time.sleep(0.25)    