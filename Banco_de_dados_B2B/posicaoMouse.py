import pyautogui as pg
import time
import os

time.sleep(4)
x,y = pg.position()
print(x,y)
#pg.moveTo(993, 715)

#pg.moveTo(1207,260 , duration=2)







img01 = 'imgs/ArquivoData.png'
var = pg.locateCenterOnScreen(img01, confidence=0.7)