from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()
userenv = os.getenv("USER_COLLEGE")
passwenv = os.getenv("PASSWORD_USER")


# Inicia o driver
driver = webdriver.Firefox()
try:
    driver.get(
        "https://www4.fumep.edu.br:8443/framehtml/web/app/edu/PortalEducacional/login/"
    )

    wait = WebDriverWait(driver, 10)

    user = wait.until(EC.visibility_of_element_located((By.ID, "User")))
    user.send_keys(userenv)

    password = wait.until(EC.visibility_of_element_located((By.ID, "Pass")))
    password.send_keys(passwenv)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    wait.until(EC.url_contains("#/main"))
    print("Course selection")
    
    small_wait = WebDriverWait(driver, 5)

    try:
        tela_curso = small_wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".selecionar-curso-page-form.page-form.ng-scope")
            )
        )
        accept = small_wait.until(
            EC.element_to_be_clickable((By.ID, "btnConfirmar"))
        )
        accept.click()

    except TimeoutException:
        print("No course selection... skiping")


finally:
    input("press enter to quit")
    driver.quit()
