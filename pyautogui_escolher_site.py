import time
import pyautogui

def menu():
    print("1 - linkedin\n2- Facebook\n3- Twitter\n4- Youtube\n5- Instagram\n")
    return int(input("Digite o código do site: "))

site=menu()
pyautogui.press('win') # Pressionar uma tecla
time.sleep(4) # Esperar em segundos
pyautogui.write('chrome') # Escrever algo
pyautogui.press('enter')
time.sleep(4)

if site>1 and site<=5:
    if site==1:
        pyautogui.write("https://br.linkedin.com/")
    elif site==2:
        pyautogui.write("https://pt-br.facebook.com/")
    elif site==3:
        pyautogui.write("https://twitter.com/")
    elif site==4:
        pyautogui.write("https://www.youtube.com/")
    elif site==5:
        pyautogui.write("https://www.instagram.com/")
    else:
        print("")
else:
    menu()


pyautogui.press('enter')
time.sleep(4)

pyautogui.press('enter')