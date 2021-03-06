from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

def wait_for_element(driver, locator, value, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((locator, value))
    )

def wait_for_clickable_element(driver, locator, value, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((locator, value))
    )

def wait_for_located_element(driver, locator, value, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((locator, value))
    )



