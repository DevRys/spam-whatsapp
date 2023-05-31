import pyautogui as pg
import time

time.sleep(5)

text = open('pokemones.txt','r')

a = 'Pokemon que me gustaria tener'

for i in text:
   pg.write( a + ' ' + i)
   pg.press('Enter')