'''
    05/08/2020 - A meta é criar um bot que coleta todos os tipos de algodão
    12/08/2020 - Não deu muito certo, vou tentar pescar peixe automaticamente
    14/08/2020 - Criando um bot de pesca
    23/08/2021 - Voltei pra fazer melhorias
'''


import pyscreenshot as ImageGrab
from time import sleep
import pyautogui


path = 'img\\'  


def start_fishing():
    try:
        x, y = pyautogui.locateCenterOnScreen(path+'skill.png', confidence=0.9)
    except:
        x, y = None,None

    if x and y:
        pyautogui.press('q') # Trocar para usar a skill com o mouse
        print('Utilizou habilidade: Escudo de água')

    print('Iniciando pesca')
    pyautogui.mouseUp()
    sleep(0.5)
    pyautogui.mouseDown()
    sleep(2)
    pyautogui.mouseUp()
    sleep(2)

    watch_water()


def capture_hook():
    mouse = pyautogui.position()

    hook = ImageGrab.grab(bbox=(mouse.x-15, mouse.y-15, mouse.x+15, mouse.y+15))

    hook.save('hook.png')

    return hook


def watch_water():
    hook = capture_hook()

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(hook, confidence=0.8)
            print('Encontrou')
        except:
            x, y = None,None
            print('Não encontrou')

        if not x and not y:
            print('Fisgou um peixe')
            pyautogui.mouseDown()
            sleep(0.3)
            break

    catch_fish()


def catch_fish():
    while True:
        try:
            xRight, yRight = pyautogui.locateCenterOnScreen(path+'progressBarRight.png', confidence=0.92, region=(551,364,820,442))
        except:
            xRight, yRight = None,None
            
        try:
            xLeft, yLeft = pyautogui.locateCenterOnScreen(path+'progressBarLeft.png', confidence=0.92, region=(551,364,820,442))
        except:
            xLeft, yLeft = None,None


        if not xRight and not xLeft:
            sleep(1.5)
            break

        if xLeft and yLeft:
            pyautogui.mouseUp() # Solta o botão esquerdo
            pyautogui.mouseDown()

        if xRight and yRight:
            pyautogui.mouseDown() # Pressiona o botão esquerdo
            

    start_fishing()



sleep(7)
start_fishing()
# capture_hook()