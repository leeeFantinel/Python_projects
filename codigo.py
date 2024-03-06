import pyautogui 
import time
import pandas as pd 
pyautogui.PAUSE = 3

time = time.sleep(5)
pyautogui.press("win")
time
pyautogui.write("opera")
time
pyautogui.press("enter")
time
pyautogui.click(x=334, y=66)
time
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time
pyautogui.press("enter")
time
pyautogui.click(x=694, y=492)
time
pyautogui.write("mybestemail@gmail.com")
time
pyautogui.press("tab")
time
pyautogui.write("mybestpassword")
time
pyautogui.press("tab")
time
pyautogui.press("enter")

#acrescentando os produtos
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index: 
    pyautogui.click(x=661, y=335)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    time
    pyautogui.press("tab")
    time
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    time
    pyautogui.press("tab")
    time
    pyautogui.press("enter")
    pyautogui.scroll(5000)

                   
