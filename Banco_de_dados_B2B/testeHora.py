from datetime import date, datetime, timedelta
import pyautogui as pg
import time

data_atual = date.today()

data_hora = datetime.now()
data_hora = data_hora.strftime('%d/%m/%Y %H:%M')

print(data_hora)

time.sleep(5)
pg.press('winleft')
pg.write('bloco de notas')
time.sleep(2)
pg.press('enter')
time.sleep(3)
pg.write('ola, mundo', data_hora )

pg.write(data_hora)
print(data_hora)