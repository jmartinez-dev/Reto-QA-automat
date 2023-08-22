import time

from faker import Faker

fake = Faker('es_CO')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


# given que estoy en la página de inicio de utest.com
def given():
    driver.get("https://www.utest.com")
    time.sleep(1)


# Cuando ingrese por el boton Join Today
def when():
    join_today_link = driver.find_element(By.CLASS_NAME, "unauthenticated-nav-bar__sign-up")
    join_today_link.click()
    time.sleep(1)


# Cuando ingreso mi primer nombre, apellido, correo, fecha de nacimiento Y hago clic en el botón Next:Location
def when2():
    # Llenar el formulario
    first_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "email")
    birth_month = Select(driver.find_element(By.ID, "birthMonth"))
    birth_day = Select(driver.find_element(By.ID, "birthDay"))
    birth_year = Select(driver.find_element(By.ID, "birthYear"))

    first_name.send_keys(fake.first_name())
    last_name.send_keys(fake.last_name())
    email.send_keys("jd@gmail.com")
    birth_month.select_by_visible_text("March")
    birth_day.select_by_visible_text("14")
    birth_year.select_by_visible_text("2001")



    # Mouse over en "Next: Location"
    next_location = driver.find_element(By.CSS_SELECTOR, ".material-icons:nth-child(2)")
    webdriver.ActionChains(driver).move_to_element(next_location).perform()

    # Hacer click en "Next: Location"
    next_location.click()
    time.sleep(5)

# Entonces debería ver la página de direcciones "https://www.utest.com/signup/address"
def then():
    current_url = driver.current_url
    print(current_url)
    assert 'https://www.utest.com/signup/address' == current_url


#Cuando ingreso a el paso "Agrega tu dirección"
#Entonces el sistema lo autodetecta o ingreso los datos solicitados y hago clic en el botón Next:Devices
def when3():
    """# Llenar el formulario de dirección
    city = driver.find_element(By.ID, "firstName")
    postal_code = driver.find_element(By.ID, "lastName")
    country = driver.find_element(By.ID, "email")

    postal_code.send_keys("111121")"""

    # Mouse over en "Next: Devices"
    next_location = driver.find_element(By.CSS_SELECTOR, ".btn-blue")
    webdriver.ActionChains(driver).move_to_element(next_location).perform()

    # Hacer click en "Next: Devices"
    next_location.click()
    time.sleep(5)

#Entonces debería ver la página de direcciones "https://www.utest.com/signup/devices"
def then2():
    current_url = driver.current_url
    print(current_url)
    assert 'https://www.utest.com/signup/devices' == current_url

#Cuando ingrese a el paso "Cuéntanos sobre tus dispositivos"
#Entonces ingreso los datos solicitados y hago clic en el botón Next:Last Step
def when4():
    driver.find_element(By.CSS_SELECTOR, "#web-device > .form-group:nth-child(1) .ui-select-match-text").click()
    driver.find_element(By.CSS_SELECTOR, "#ui-select-choices-row-3-3 div").click()
    driver.find_element(By.CSS_SELECTOR, "#web-device > .form-group:nth-child(2) .ui-select-placeholder").click()
    driver.find_element(By.CSS_SELECTOR, "#ui-select-choices-row-4-0 > .ui-select-choices-row-inner").click()
    driver.find_element(By.CSS_SELECTOR, "#web-device > .form-group:nth-child(3) .ui-select-placeholder").click()
    driver.find_element(By.CSS_SELECTOR, "#ui-select-choices-row-5-10 div").click()

    # Mouse over en "Next: Last Step"
    next_location = driver.find_element(By.CSS_SELECTOR, ".btn-blue pull-right")
    webdriver.ActionChains(driver).move_to_element(next_location).perform()

    # Hacer click en "Next: Last Step"
    next_location.click()
    time.sleep(5)

#Entonces debería ver la página de direcciones "https://www.utest.com/signup/complete"
def then3():
    current_url = driver.current_url
    print(current_url)
    assert 'https://www.utest.com/signup/complete' == current_url


#Cuando ingrese a el paso "El último paso"
#Cuando complete la contraseña y confirme la contraseña y hago clic en aceptar terminos, condiciones y politicas
def when5():
    password_u = driver.find_element(By.ID, "password")
    confirm_password = driver.find_element(By.ID, "confirm_password")

    password = (fake.password())
    password_u.send_keys(password)
    confirm_password.send_keys(password)

    driver.find_element(By.CSS_SELECTOR, ".signup-consent--highlight").click()
    driver.find_element(By.CSS_SELECTOR, ".error:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, ".error").click()

#Entonces mi usuario se deberia crear correctamente
    driver.find_element(By.CSS_SELECTOR, ".material-icons:nth-child(2)").click()


given()
when()
when2()
then()
when3()
then2()
when4()
then3()
when5()

