from tkinter import *
import tkinter.font as tkFont
from typing_extensions import Self
from xml.dom.pulldom import END_ELEMENT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep
import pyautogui


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class btclick0:
    def btclick(self, END):
        global compra
        compra = txt1.get(END)
        print(compra)
        global remessa
        remessa = txt2.get(END)
        global ordem
        ordem = txt3.get(END)
        global desc
        desc = txt5.get(END)
        global precosvc
        precosvc = txt4.get(END)




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
    sleep(100000)





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()
empObj = btclick0()
window.geometry("862x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    862.0,
    519.0,
    fill="#0038FF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    431.0,
    104.0,
    image=image_image_1
)

canvas.create_rectangle(
    55.0,
    179.0,
    807.0,
    509.0,
    fill="#0038FF",
    outline="")

canvas.create_text(
    55.0,
    189.0,
    anchor="nw",
    text="Ordem de compra",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    483.5,
    207.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_1.place(
    x=352.0,
    y=189.0,
    width=263.0,
    height=35.0
)
txt1 = entry_1

canvas.create_text(
    55.0,
    236.0,
    anchor="nw",
    text="NF de Remessa",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    483.5,
    254.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_2.place(
    x=352.0,
    y=236.0,
    width=263.0,
    height=35.0
)
txt2 = entry_2

canvas.create_text(
    55.0,
    283.0,
    anchor="nw",
    text="NF de Retorno",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    483.5,
    301.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_3.place(
    x=352.0,
    y=283.0,
    width=263.0,
    height=35.0
)
txt3 = entry_3

canvas.create_text(
    55.0,
    330.0,
    anchor="nw",
    text="Preço do serviço",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    483.5,
    348.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_4.place(
    x=352.0,
    y=330.0,
    width=263.0,
    height=35.0
)
txt4 = entry_4

canvas.create_text(
    55.0,
    377.0,
    anchor="nw",
    text="Descrição do\nserviço",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    483.5,
    433.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)
entry_5.place(
    x=352.0,
    y=377.0,
    width=263.0,
    height=110.0
)
txt5 = entry_5

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: empObj.btclick(txt1, txt2, txt3, txt4, txt5),
    relief="flat"
)
button_1.place(
    x=653.0,
    y=179.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: navegador(),
    relief="flat"
)
button_2.place(
    x=653.0,
    y=254.0,
    width=180.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_3.place(
    x=654.0,
    y=329.0,
    width=180.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()



