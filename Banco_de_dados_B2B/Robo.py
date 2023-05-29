from ast import While
import importlib
from pickle import NONE
import re
from tkinter import W
import pyautogui as pg
import cv2
import time
import os
import requests
from datetime import date, datetime


esperar = 65
site = 'https://app.powerbi.com/groups/me/apps/8cc5a663-5fd0-444e-8e67-00c0b6fb44a2/reports/95689238-896e-48fc-9120-5f5f2b0c3139/ReportSectiona3080dba5e1c365164e4'

data_atual = date.today()
data_hora = datetime.now()
data_hora = data_hora.strftime('%d/%m/%Y %H:%M')

   

def relatorio():
    pg.press('winleft')
    time.sleep(1)
    pg.write('Relatorio de Erros B2B')
    pg.press('backspace')
    pg.press('enter')
    time.sleep(2)
    Relatorio = 'imgs/relatorio.png'
    var = None
    while var == None:
        var = pg.locateCenterOnScreen(Relatorio, confidence=0.8)
        time.sleep(1)
        if var != None:
            pg.write( escrita )

            pg.write( data_hora)
            pg.press('enter')
            time.sleep(3)
            pg.hotkey('alt', 'f4')
            time.sleep(2)
            pg.press('enter')
   

def FecharPrograma():
    time.sleep(5)
    imgPasta = 'imgs/pasta.png'
    imgExcel = 'imgs/excel.png'
    imgFechar = 'imgs/fecharJanelas.png'
    imgNavegador = 'imgs/edge.png'
    imgPython = "imgs/expython.png"

    varPasta = None
    varExcel = None
    varFechar = None
    varNavegador = None
    varPython = None

    if varPasta == None:
        varPasta = pg.locateCenterOnScreen(imgPasta, confidence=0.7)
        pg.rightClick(varPasta)
        time.sleep(3)
        varFechar = pg.locateCenterOnScreen(imgFechar, confidence=0.7)
        if varFechar != None:
            pg.click(varFechar)
    time.sleep(5)

    if varExcel == None:
        varExcel = pg.locateCenterOnScreen(imgExcel, confidence=0.7)
        pg.rightClick(varExcel)
        time.sleep(3)
        varFechar = pg.locateCenterOnScreen(imgFechar, confidence=0.7)
        if varFechar != None:
            pg.click(varFechar)
            time.sleep(9)
            pg.click(949 ,453)
            time.sleep(2)
            pg.press('enter')
            time.sleep(2)
            pg.press('enter')
            time.sleep(9)
            pg.press('enter')
    time.sleep(5)

    if varNavegador == None:
        varNavegador = pg.locateCenterOnScreen(imgNavegador, confidence=0.7)
        if varNavegador != None:  
            pg.click(varNavegador)
            time.sleep(3)
            pg.hotkey('alt', 'f4')
    time.sleep(5)

    os._exit(0)

def Iniciar():
    time.sleep(5)
    imgPasta = 'imgs/pasta.png'
    imgExcel = 'imgs/excel.png'
    imgFechar = 'imgs/fecharJanelas.png'
    imgNavegador = 'imgs/edge.png'
    imgPython = "imgs/expython.png"

    varPasta = None
    varExcel = None
    varFechar = None
    varNavegador = None
    varPython = None

    if varPasta == None:
        varPasta = pg.locateCenterOnScreen(imgPasta, confidence=0.7)
        pg.rightClick(varPasta)
        time.sleep(3)
        varFechar = pg.locateCenterOnScreen(imgFechar, confidence=0.7)
        if varFechar != None:
            pg.click(varFechar)
    time.sleep(5)

    if varExcel == None:
        varExcel = pg.locateCenterOnScreen(imgExcel, confidence=0.7)
        pg.rightClick(varExcel)
        time.sleep(3)
        varFechar = pg.locateCenterOnScreen(imgFechar, confidence=0.7)
        if varFechar != None:
            pg.click(varFechar)
            time.sleep(9)
            pg.click(949 ,453)
            time.sleep(2)
            pg.press('enter')
            time.sleep(2)
            pg.press('enter')
            time.sleep(9)
            pg.press('enter')
    time.sleep(5)

    if varNavegador == None:
        varNavegador = pg.locateCenterOnScreen(imgNavegador, confidence=0.7)
        if varNavegador != None:
            pg.click(varNavegador)
            time.sleep(3)
            pg.hotkey('alt', 'f4')
    time.sleep(5)





#####################################################################
#                           ESTRUTURA WHILE                         #
#                                                                   #
#   time.sleep(3)                                                   #
#   img01 = 'imgs/IMAGEM.PNG'                                       #
#   var = None                                                      #
#   while var == None:                                              #
#       var =  pg.locateCenterOnScreen(img01, confidence = 0.7)     #
#       time.sleep(1)                                               #
#       if var != None:                                             #
#           pg.moveTo(var)                                          #
#           pg.click(var)                                           #
#   time.sleep(1)                                                   #
#####################################################################
#####################################################################
#                           ESTRUTURA FOR                           #
#                                                                   #
#   img02 = 'imgs/IMAGEM.png'                                       #
#   var = None                                                      #
#   for c in range(1, 10 or var == None):                           #
#       var = pg.locateCenterOnScreen(IMAGEM, confidence=0.7)       #
#       if var != None:                                             #
#           pg.moveTo(var)                                          #
#           pg.hotkey('winleft', 'up')                              #
#           break                                                   #
#       elif c == 10:                                               #
#           time.sleep(1)                                           #
#           escrita = '[ERRO PASSO 2] Nao encontrou img IMAGE.PNG'  #
#           relatorio()            / FUNÇÃO                         #
#           FecharPrograma()      /FUNÇÃO                           #
#   pg.press('enter')                                               #
#####################################################################


prog = True
if(prog == True):
    Iniciar()
time.sleep(2)


# 01 EXCLUIR PLANILHAS ANTERIORES (DAWNLOAD)

pg.press('winleft')
time.sleep(5)
pg.write('coisas')  # LINHA ALTERAVEL (NOME DA PASTA ONDE ESTA O ARQUIVO)
pg.press('enter')
time.sleep(5)
img01 = 'imgs/ArquivoData.png'
var = None
c = 0
while var == None:
    var = pg.locateCenterOnScreen(img01, confidence=0.7)
    time.sleep(1)
    c = c+1
    if var != None:
        pg.hotkey('winleft', 'up')
        pg.click(var)
        time.sleep(0.5)
        pg.press('delete')
        time.sleep(1)
        var = None

    elif c == 6:
        time.sleep(1)
        break
pg.hotkey('alt', 'f4')
time.sleep(2)
pg.press('enter')

# 02 ENTRAR NO NAVEGADOR (EDGE)
pg.press('winleft')
time.sleep(1)
pg.write('microsoft edge')
time.sleep(2)
pg.press('enter')

# 03 ACESSAR SITE REPORT B2B

img02 = 'imgs/navegador.png'
var = None
time.sleep(3)
for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img02, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        time.sleep(1)
        pg.write(site)
        time.sleep(1)
        pg.hotkey('winleft', 'up')
        pg.press('enter')
        break
    elif c == esperar:
        print('fechar programa')
        escrita = '[ERRO PASSO 3] não encontrou img navegador '
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 03 Ok!')

# 04 CLICK IMG SP-CAPITAL

img03 = 'imgs/sp-capital.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img03, confidence=0.9)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.moveTo(var)
        pg.click(var)
        break
    elif c == esperar:
        print('fechar programa')
        escrita = '[ERRO PASSO 4] Nao encontrou img SP-Capital '       
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 04 Ok!')


# 05 CLICK IMG ANALITICO

img04 = 'imgs/analitico.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img04, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.moveTo(var)
        pg.click(var)
        break
    elif c == esperar:
        escrita = '[ERRO PASSO 05] Nao encontrou img analitico '
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 05 Ok!')


# 06 EXPORTAR DADOS

img05 = 'imgs/filtro.png'
img06 = 'imgs/exportarDados.png'
var = None
var1 = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img05, confidence=0.8)
    c = c+1
    time.sleep(1.5)
    if var != None:
        pg.click(993, 715)
        time.sleep(2)
        pg.moveTo(var)
        currentMouseX, currentMouseY = pg.position()
        print(currentMouseX, currentMouseY)
        x = currentMouseX + 80
        y = currentMouseY
        pg.moveTo(x, y)
        pg.click(x, y)
        time.sleep(5)
        var1 = pg.locateCenterOnScreen(img06, confidence=0.7)
        pg.click(var1)
        break

    elif var == None:
        pg.click(993, 715)

    elif c == esperar:
        
        print('Passo 06 ERRO')
time.sleep(1)

# 07 EXPORTAR / DAWNLOAD DO ARQUIVO EXCEL

img07 = 'imgs/exportar.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img07, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.click(var)
        break
    elif c == esperar:
        
        print('Passo 07 ERRO!')
time.sleep(1)


img08 = 'imgs/dadosExportados.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img08)
    time.sleep(1)
    currentMouseX, currentMouseY = pg.position()
    print(currentMouseX, currentMouseY)
    x = currentMouseX = 1755
    y = currentMouseY = 641
    pg.moveTo(x, y)
    pg.click(x, y)
    if var != None:
        time.sleep(2)
        pg.press('winleft')
        time.sleep(2)
        # LINHA ALTERAVEL (NOME DA PASTA ONDE ESTA O ARQUIVO)
        pg.write('coisas')
        pg.press('enter')
        time.sleep(3)
        break
    elif c == esperar:
        
       print('Passo 07 ERRO!')
time.sleep(1)




###### Refazendo o passo a passo anterior

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img05, confidence=0.8)
    c = c+1
    time.sleep(1.5)
    if var != None:
        pg.click(993, 715)
        time.sleep(2)
        pg.moveTo(var)
        currentMouseX, currentMouseY = pg.position()
        print(currentMouseX, currentMouseY)
        x = currentMouseX + 80
        y = currentMouseY
        pg.moveTo(x, y)
        pg.click(x, y)
        time.sleep(5)
        var1 = pg.locateCenterOnScreen(img06, confidence=0.7)
        pg.click(var1)
        break

    elif var == None:
        pg.click(993, 715)

    elif c == esperar:
        escrita = '[ERRO PASSO 06] Nao encntrou img filtro/exportar-dados '
        relatorio()
        time.sleep(2)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 06 Ok!')

# 07 EXPORTAR / DAWNLOAD DO ARQUIVO EXCEL

img07 = 'imgs/exportar.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img07, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.click(var)
        break
    elif c == esperar:
        escrita = '[ERRO PASSO 07] Nao encontrou img Exportar '
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 07 Ok!')

img08 = 'imgs/dadosExportados.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img08)
    time.sleep(1)
    currentMouseX, currentMouseY = pg.position()
    print(currentMouseX, currentMouseY)
    x = currentMouseX = 1755
    y = currentMouseY = 641
    pg.moveTo(x, y)
    pg.click(x, y)
    if var != None:
        time.sleep(2)
        pg.press('winleft')
        time.sleep(2)
        # LINHA ALTERAVEL (NOME DA PASTA ONDE ESTA O ARQUIVO)
        pg.write('coisas')
        pg.press('enter')
        time.sleep(3)
        break
    elif c == esperar:
        escrita = '[ERRO PASSO 07] Nao encontrou img exportado com sucesso '
        relatorio()
        FecharPrograma()
time.sleep(1)
print('Passo 07 Ok!')







# 08 ENTRAR NA TABELA EXPORTADA

img09 = 'imgs/ArquivoData.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img09, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.click(var)
        time.sleep(0.5)
        pg.press('enter')
        break
    elif c == esperar:
        escrita = ('[ERRO PASSO 08] Nao encontrou img arquivo excel ')
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
print('Passo 08 Ok!')


# 09 VERIFICAR SE TABELA EXCEL ESTA ATIVA

img10 = 'imgs/sensibilidade.png'
img11 = 'imgs/habilitar.png'
var = None
var1 = None


for c in range(1, esperar or var == None):
    var1 = pg.locateCenterOnScreen(img11, confidence=0.7)
    var = pg.locateCenterOnScreen(img10, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.moveTo(var)
        break

    elif var1 != None:
        pg.moveTo(var1)
        pg.click(var1)
        time.sleep(1)
        pg.click(var1)

    elif c == esperar:
        escrita = (
            '[ERRO PASSO 09] Nao encontrou img sensibilidade tabela excel (data) ')
        relatorio()
        time.sleep(3)
        FecharPrograma()

pg.press('enter')

print('Passo 09 Ok!')

# 10 ENTRAR NA PASTA DO WINDOWS

img12 = 'imgs/pasta.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img12, confidence=0.8)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.click(var)
        break
    elif c == esperar:
        escrita = ('[ERRO PASSO 10] Não encontrou img pasta ')
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break

print('Passo 10 Ok!')


# 11 ENTRAR NO DIRETÓRIO DO BANCO DE DADOS PASTA ONLINE

img13 = 'imgs/atualizar.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img13, confidence=0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.moveTo(var)
        time.sleep(1)
        currentMouseX, currentMouseY = pg.position()
        print(currentMouseX, currentMouseY)
        x = currentMouseX - 80
        y = currentMouseY
        pg.moveTo(x, y, duration=1)
        pg.click(x, y)
        # LINHA ALTERAVEL (NOME DA PASTA ONDE ESTA O ARQUIVO)
        local = ('\\10.128.222.232\esse_spc$\MIRELLE\Report_B2B')
        pg.write('\\')
        pg.write(local)
        pg.press('enter')
        time.sleep(1)
        pg.press('enter')
        break

    elif c == esperar:
        escrita = ('[ERRO PASSO 11] Nao encontrou img atualizar ')
        relatorio()
        time.sleep(3)
        FecharPrograma()
        break
pg.press('enter')
print('Passo 11 Ok!')

# 12 CLICK NO ARQUIVO EXCEL BANCO REPORT B2B

img14 = 'imgs/bancoReport.png'
var = None

for c in range(1, esperar or var == None):
    var = pg.locateCenterOnScreen(img14, confidence=0.8)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.click(var)
        pg.press('enter')
        break
    elif c == esperar:
        escrita = ('[ERRO PASSO 12] Nao encontrou a tabela excel ReportB2B ')
        relatorio()
        time.sleep(3)
        FecharPrograma()
        pg.press('enter')
        break
print('Passo 12 Ok!')

# 13 VERIFICAR SE A PLANILHA BANCO DE DADOS ESTÁ HABILITADA

time.sleep(7)
img15 = 'imgs/habilitar.png'
var = None
time.sleep(2)


var = pg.locateCenterOnScreen(img15, confidence=0.7)

time.sleep(1)
if var != None:
    pg.hotkey('winleft', 'up')
    time.sleep(1)
    pg.moveTo(var)
    pg.click(var)
    time.sleep(2)
    pg.click(var)
    
        
        
print('Passo 13 Ok!')                               

# 14 INICIANDO PREOCESO CTRL+C  CTRL+V

img16 = 'imgs/sensibilidade.png'
var = None
time.sleep(7)
for c in range (1, esperar or var == None):
    var = pg.locateCenterOnScreen(img16, confidence = 0.7)
    c = c+1
    time.sleep(1)
    if var != None:
        pg.hotkey('winleft', 'up')
        pg.moveTo(var)
        pg.hotkey('ctrl','t')
        time.sleep(2)
        pg.press('delete')
        time.sleep(2)
        break
    elif c == esperar:
        escrita = ('[ERRO PASSO 14] Nao encontrou img sensibilidade da tabela Report B2B ' )
        relatorio()
        time.sleep(3)
        FecharPrograma()
        pg.press('enter')
        break
print('Passo 14 Ok!')

# 15 VOLTAR A PLANILHA EXTRAIDA CTRL+C / VOLTAR B2B CTRL+V

time.sleep(5)   
pg.hotkey('alt','tab')
time.sleep(1)
pg.hotkey('ctrl','t')
time.sleep(1)
pg.hotkey('ctrl','c')
time.sleep(1)

pg.hotkey('alt','tab')
time.sleep(5)
pg.hotkey('ctrl','v')
time.sleep(7)
pg.press('enter')
time.sleep(7)

pg.hotkey('alt', 'f4')
time.sleep(10)
pg.press('enter')

# 16  SALVAR E FECHAR PLANILHA

'''img17 = 'imgs/salvamento.png'
var = None

for c in range (1, esperar or var == None):
    var = pg.locateCenterOnScreen(img17, confidence = 0.8)
    c = c+1
    time.sleep(1)
    if var !=None:
        pg.moveTo(var)
        time.sleep(8)
        pg.hotkey('alt','f4')
        time.sleep(1)
        pg.press('enter')
        break
    elif c == esperar:
        escrita = ('[ERRO PASSO 16] Nao conseguil efetua o salvamento da tabela B2B')
        relatorio()
        time.sleep(3)
        FecharPrograma()
        pg.press('enter')
        break'''
print('Passo 16 Ok!') 
   
# 17 FECHAR ABAS ABERTAS
'''time.sleep(20)
pg.hotkey('alt','f4')
time.sleep(5)
pg.press('enter')
time.sleep(3)
pg.press('enter')
time.sleep(3)
pg.press('enter')
time.sleep(5)
pg.hotkey('alt','f4')
time.sleep(5)
pg.hotkey('alt','f4')'''


print('Fim do programa!')
FecharPrograma()


