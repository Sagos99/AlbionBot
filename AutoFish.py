'''
    05/08/2020 - A meta é criar um bot que coleta todos os tipos de algodão
    12/08/2020 - Não deu muito certo, vou tentar pescar peixe automaticamente
    14/08/2020 - Criando um bot de pesca
'''


from time import sleep
import pyautogui


path = 'img/'  


def fishing():
    try:
        x, y = pyautogui.locateCenterOnScreen(path+'skill.png', confidence=0.9)
    except:
        x, y = None,None

    if x and y:
        print('Usando skill de pesca')
        pyautogui.press('q')

    print('Iniciando nova pesca...')
    pyautogui.mouseUp()
    sleep(0.5)
    pyautogui.mouseDown()
    sleep(2)
    pyautogui.mouseUp()
    sleep(2)

    catch_fish()


def catch_fish():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(path+'hook2.png', confidence=0.8)
        except:
            x, y = None,None

        if not x and not y:
            print('Fisgou um peixe')
            pyautogui.mouseDown()
            sleep(0.3)
            break

    progressBar()


def progressBar():
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
            

    fishing()


sleep(5)
fishing()