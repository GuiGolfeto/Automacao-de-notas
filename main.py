from tkinter import *
import tkinter.font as tkFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import pyautogui


def btclick():
    global compra
    compra = txt.get('1.0', 'end-1c')
    global remessa
    remessa = txt2.get('1.0', 'end-1c')
    global ordem
    ordem = txt3.get('1.0', 'end-1c')
    global desc
    desc = txt4.get('1.0', 'end-1c')
    global precosvc
    precosvc = txt5.get('1.0', 'end-1c')


def navegador():
    nav = webdriver.Chrome()
    nav.maximize_window()

    # login no sistema
    nav.get('http://138.0.140.51:5660/issweb/paginas/login;jsessionid=i7116Yt6Md6IPNX8AcxXFOMJ.undefined')
    sleep(1)
    nav.find_element(By.XPATH, '//*[@id="username"]').send_keys('34894404000198', Keys.TAB)
    sleep(2)
    nav.find_element(By.XPATH, '//*[@id="password"]').send_keys('Gui090503', Keys.ENTER)
    sleep(5)
    nav.find_element(By.XPATH, '//*[@id="navNfse"]/a').click()
    nav.find_element(By.XPATH, '//*[@id="j_idt88:layoutNfs"]').click()

    # preenchendo dados da NF
    data = nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataEmissao_input"]').get_attribute('value')
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataCompetencia_input"]').send_keys(data)

    # Atividade CNAE
    drop = Select(nav.find_element(By.ID, 'formEmissaoNFConvencional:listaAtvCnae_input'))
    drop.select_by_visible_text("4520001 - Serviços de manutenção e reparação mecânica de veículos automotores")
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()
    sleep(0.7)
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()

    # Atividade Municipal
    drop2 = Select(nav.find_element(By.ID, 'formEmissaoNFConvencional:listaAtvAtd_input'))
    drop2.select_by_value('000014;0000001')
    sleep(2)

    # Discriminação dos Serviços
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:descricaoItem"]').send_keys(desc)  # descrição
    sleep(2)
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(Keys.CONTROL, 
                                                                                                                "a")  # valor
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(precosvc,
                                                                                                             Keys.TAB)  # valor
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:btnAddItem"]/span[2]').click()  # add desc
    sleep(2)

    # Observações
    pyautogui.scroll(-1000)
    pyautogui.click(x=1578, y=844)
    sleep(1)
    pyautogui.click(x=507, y=882)
    text_obs = f'Documento referente a Ordem de compra {compra}, NF de remessa {remessa} e NF de retorno de remessa {ordem}. Dados para deposito: Bando Bradesco, Agencia 020-5, Conta corrente 3706-0'
    pyautogui.write(text_obs)
    sleep(36000)


app = Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=15)
buttonStyle = tkFont.Font(family="Lucida Grande", size=20)

app.geometry('390x350')
app.configure(bg='white')
lb = Label(app, text='Ordem de compra', background='white', font=fontStyle)
lb.place(x=1, y=1)
txt = Text(app, background='light gray', font=fontStyle, width=17, height=1)
txt.place(x=185, y=1)

lb2 = Label(app, text='NF de remessa', background='white', font=fontStyle)
lb2.place(x=1, y=30)
txt2 = Text(app, background='light gray', font=fontStyle, width=17, height=1)
txt2.place(x=185, y=30)

lb3 = Label(app, text='NF de Retorno', background='white', font=fontStyle)
lb3.place(x=1, y=59)
txt3 = Text(app, background='light gray', font=fontStyle, width=17, height=1)
txt3.place(x=185, y=59)

lb4 = Label(app, text='Descrição do serviço:', background='white', font=fontStyle)
lb4.place(x=1, y=120)
txt4 = Text(app, background='light gray', font=fontStyle, width=25, height=5)
txt4.place(x=1, y=149)

lb5 = Label(app, text='Preço do serviço', background='white', font=fontStyle)
lb5.place(x=1, y=89)
txt5 = Text(app, background='light gray', font=fontStyle, width=17, height=1)
txt5.place(x=185, y=89)

bt = Button(app, text='Save', command=btclick, font=buttonStyle)
bt.place(x=1, y=280)

bt2 = Button(app, text='Start', command=navegador, font=buttonStyle)
bt2.place(x=100, y=280)

bt3 = Button(app, text='Close', command=app.destroy, font=buttonStyle)
bt3.place(x=200, y=280)

app.mainloop()
