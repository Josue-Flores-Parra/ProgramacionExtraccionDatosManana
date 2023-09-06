
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # queda pendiente
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size= 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://es-la.facebook.com/")

txtEmail= navegador.find_element(By.NAME, "email")
txtEmail.send_keys("usuario@gmail.com")
time.sleep(2)

txtPassword= navegador.find_element(By.NAME, "pass")
txtPassword.send_keys("***************")
time.sleep(2)

navegador.save_screenshot("img_test.png")

btnLogin= navegador.find_element(By.NAME, "login")
btnLogin.click()

navegador.find

print(navegador.title)

time.sleep(5)

