# Tkinter imports
from tkinter import *
import tkinter.font as tkFont
from xml.dom.pulldom import END_ELEMENT
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# pysautogui Imports
from time import sleep
import pyautogui




# save variables
def btclick():
    global compra
    compra = txt.get('1.0', 'end-1c')
    print(compra)
    global remessa
    remessa = txt2.get('1.0', 'end-1c')
    print(remessa)
    global ordem
    ordem = txt3.get('1.0', 'end-1c')
    print(ordem)
    global desc
    desc = txt5.get('1.0', 'end-1c')
    print(desc)
    global precosvc
    precosvc = txt4.get('1.0', 'end-1c')
    print(precosvc)







# Automation with Selenium
def navegador():
    nav = webdriver.Chrome()
    nav.maximize_window()

    # System login
    nav.get('http://138.0.140.51:5660/issweb/paginas/login;jsessionid=i7116Yt6Md6IPNX8AcxXFOMJ.undefined')
    sleep(1)
    nav.find_element(By.XPATH, '//*[@id="username"]').send_keys('34894404000198', Keys.TAB)
    sleep(2)
    nav.find_element(By.XPATH, '//*[@id="password"]').send_keys('Gui090503', Keys.ENTER)
    sleep(5)
    nav.find_element(By.XPATH, '//*[@id="navNfse"]/a').click()
    nav.find_element(By.XPATH, '//*[@id="j_idt88:layoutNfs"]').click()

    # Filling in NF data
    data = nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataEmissao_input"]').get_attribute('value')
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:imDataCompetencia_input"]').send_keys(data)

    # CNAE activity
    drop = Select(nav.find_element(By.ID, 'formEmissaoNFConvencional:listaAtvCnae_input'))
    drop.select_by_visible_text("4520001 - Serviços de manutenção e reparação mecânica de veículos automotores")
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()
    sleep(0.7)
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:listaAtvCnae_label"]').click()

    # Municipal Activity
    drop2 = Select(nav.find_element(By.ID, 'formEmissaoNFConvencional:listaAtvAtd_input'))
    drop2.select_by_value('000014;0000001')
    sleep(2)

    # Services discrimination
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:descricaoItem"]').send_keys(desc)  # descrição
    sleep(2)
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(Keys.CONTROL, 
                                                                                                                "a")  # valor
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:vlrUnitario_input"]').send_keys(precosvc,
                                                                                                             Keys.TAB)  # valor
    nav.find_element(By.XPATH, '//*[@id="formEmissaoNFConvencional:btnAddItem"]/span[2]').click()  # add desc
    sleep(2)

    # Comments
    pyautogui.scroll(-1000)
    pyautogui.click(x=1578, y=844)
    sleep(2)
    pyautogui.click(x=507, y=882)
    sleep(2)
    pyautogui.click(x=507, y=882)
    sleep(2)
    text_obs = f'documento referente a ordem de compra {compra} nf de remessa {remessa} e nf de retorno de remessa {ordem} dados para deposito: banco bradesco agencia 020-5, conta corrente 3706-0'
    pyautogui.write(text_obs)
    sleep(36000)













# Software window using TKinter
window = Tk()
window.geometry("862x519")
window.configure(bg="#FFFFFF")

font = tkFont.Font(family="Lucida Grande", size=15)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
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

txt = Text(window, background='#FFFFFF', width=26, height=1, font=font)
txt.place(x=350, y=199)

canvas.create_text(
    55.0,
    236.0,
    anchor="nw",
    text="NF de Remessa",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

txt2 = Text(window, background='#FFFFFF', width=26, height=1, font=font)
txt2.place(x=350, y=246)

canvas.create_text(
    55.0,
    283.0,
    anchor="nw",
    text="NF de Retorno",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

txt3 = Text(window, background='#FFFFFF', width=26, height=1, font=font)
txt3.place(x=350, y=294)

canvas.create_text(
    55.0,
    330.0,
    anchor="nw",
    text="Preço do serviço",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)

txt4 = Text(window, background='#FFFFFF', width=26, height=1, font=font)
txt4.place(x=350, y=340)

canvas.create_text(
    55.0,
    377.0,
    anchor="nw",
    text="Descrição do\nserviço",
    fill="#000000",
    font=("Montserrat Regular", 30 * -1)
)


txt5 = Text(window, background='#FFFFFF', width=26, height=5, font=font)
txt5.place(x=350, y=380)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: btclick(),
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
