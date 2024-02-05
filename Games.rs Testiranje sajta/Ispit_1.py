from telnetlib import EC
from pkg_resources import require
from selenium.common import TimeoutException
from selenium.webdriver.common.devtools.v85 import console
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


def pokrenichrome(url):
    driver=webdriver.Chrome(options=webdriver.ChromeOptions(),service=Service())
    driver.maximize_window()
    driver.get(url)
    return driver

def test_search_bar():
    driver=pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/div[3]/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="search-text"]').send_keys('Spiderman')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="search-text"]').send_keys(Keys.ENTER)
    time.sleep(2)

    assert 'Spiderman' in driver.find_element(By.CLASS_NAME,'text').text,'ne postoji trazeni tekts'
    time.sleep(2)
    driver.save_screenshot('screenshot/1.png')
    ugasichrome(driver)

def test_brzi_pregled():
    driver=pokrenichrome('https://www.games.rs/proizvodi?search=spiderman')
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div/div/div[1]/div[4]/a/i').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="product_details_modal"]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[4]/ul/li/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-ajax-wrapper"]/div/div/div[2]/div[3]/div[2]/button').click()
    time.sleep(2)
    assert '' in driver.find_element(By.CLASS_NAME,'modal-header').text, 'los proizvod'
    time.sleep(2)

    driver.save_screenshot('screenshot/2.png')
    ugasichrome(driver)

def test_proizvod_1():
    driver=pokrenichrome('https://www.games.rs/proizvodi?search=spiderman')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 2400);")
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div[3]/div/div[20]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[4]/div/div[1]/div/div/div[2]/div[4]/ul/li/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-ajax-wrapper"]/div/div/div[2]/div[3]/div[2]/button').click()
    time.sleep(2)
    assert '' in driver.find_element(By.CLASS_NAME,'product-details').text,'ne postoji'
    time.sleep(2)
    driver.save_screenshot('screenshot/3.png')
    ugasichrome(driver)

def test_proizvod_2():
    driver=pokrenichrome('https://www.games.rs/proizvodi?search=spiderman')
    time.sleep(2)
    driver.execute_script('window.scrollTo(2400,3200);')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div[3]/div/div[24]').click()
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,550);')
    time.sleep(4)
    driver.execute_script('window.scrollTo(550,0);')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[4]/div/div[1]/div/div/div[2]/div[4]/ul/li/div/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-ajax-wrapper"]/div/div/div[2]/div[3]/div[2]/button').click()
    time.sleep(4)

    assert '' in driver.find_element(By.CLASS_NAME,'modal-header').text, 'los proizvod'

    driver.save_screenshot('screenshot/4.png')
    ugasichrome(driver)

def test_registracija():
    driver=pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'register-btn').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="reg_type_person"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="reg_type_person"]/option[2]').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="reg_type_person"]/option[1]').click()
    time.sleep(2)
    driver.find_element(By.ID,'reg_firstname').send_keys('Lazar')
    time.sleep(2)
    driver.find_element(By.ID,'reg_lastname').send_keys('Bulatovic')
    time.sleep(2)
    driver.find_element(By.ID,'reg_email').send_keys('lazarbulatovic1@gmail.com')
    time.sleep(2)
    driver.find_element(By.ID,'reg_phone').send_keys('069713696')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="registration_modal"]/div[2]/div[2]/div[2]/div[17]/div[1]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="registration_modal"]/div[2]/div[2]/div[2]/div[17]/div[2]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="registration_modal"]/div[2]/div[2]/div[2]/div[17]/div[3]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="registration_modal"]/div[2]/div[2]/div[2]/div[17]/div[4]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="registration_modal"]/div[2]/div[2]/div[2]/div[17]/div[5]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="registration_modal"]/div[1]/button').click()
    time.sleep(2)

    assert '' in driver.find_element(By.CLASS_NAME,'register-btn').text,'losa registracija'

    driver.save_screenshot('screenshot/5.png')
    ugasichrome(driver)

def test_padajuci_meni():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/li[1]/a').click()
    time.sleep(2)
    actions = ActionChains(driver)
    menu_element = driver.find_element(By.XPATH, '/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/a')
    actions.move_to_element(menu_element).perform()
    time.sleep(2)
    actions = ActionChains(driver)
    menu_element = driver.find_element(By.XPATH, '/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/div/div/div/div[1]/div/div[2]/ul/li[13]/a')
    actions.move_to_element(menu_element).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/div/div/div/div[1]/div/div[2]/ul/li[13]/a').click()
    time.sleep(2)

    assert '' in driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/div/div/div/div[1]/div/div[2]/ul/li[13]/a').text, 'los padajuci meni'

    driver.save_screenshot('screenshot/6.png')
    ugasichrome(driver)


def test_proizvod_3():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/li[1]/a').click()
    time.sleep(2)
    actions = ActionChains(driver)
    menu_element = driver.find_element(By.XPATH, '/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/a')
    actions.move_to_element(menu_element).perform()
    time.sleep(2)
    actions = ActionChains(driver)
    menu_element = driver.find_element(By.XPATH, '/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/div/div/div/div[1]/div/div[2]/ul/li[13]/a')
    actions.move_to_element(menu_element).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/header/div/div[4]/div/nav/ul/li[1]/div/div/ul/li[6]/div/div/div/div[1]/div/div[2]/ul/li[13]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div[3]/div/div[3]/div/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/main/div[4]/div/div[1]/div/div/div[2]/div[4]/ul/li/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-ajax-wrapper"]/div/div/div[2]/div[3]/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="miniCartContent"]/div[1]').click()
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="order_cart_content"]/div[1]/div[2]/div/div/table/tbody/tr[1]/td[6]/div/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/header/div/div[3]/div/div[1]/div/a/img').click()
    time.sleep(2)
    assert '' in driver.find_element(By.XPATH,'/html/body/header/div/div[3]/div/div[1]/div/a').text, 'los proizvod'

    driver.save_screenshot('screenshot/7.png')
    ugasichrome(driver)

def test_popusti():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/div[2]').click()
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,400);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(400,800);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(800,1600);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(1600,0);')
    time.sleep(2)
    assert 'Privilege Club' in driver.find_element(By.CLASS_NAME,'title').text,'ne postoji ta rec'
    driver.save_screenshot('screenshot/8.png')
    ugasichrome(driver)

def test_facebook():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(3)
    driver.execute_script('window.scrollTo(0,2000);')
    time.sleep(2)
    a = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/a").get_attribute('href')
    time.sleep(3)
    driver.get(a)
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]").click()
    time.sleep(3)
    assert 'GameS' in driver.find_element(By.XPATH, "//h1[contains(.,'GameS')]").text, 'pogresan naslov'
    time.sleep(3)

    driver.save_screenshot('screenshot/9.png')
    ugasichrome(driver)


def test_instagram():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,2000);')
    time.sleep(2)
    a=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/a").get_attribute('href')
    time.sleep(5)
    driver.get(a)
    time.sleep(2)
    assert 'gamesdoo' in driver.find_element(By.XPATH,"//h2[contains(.,'gamesdoo')]").text,"pogresan naslov"
    time.sleep(2)
    driver.save_screenshot('screenshot/10.png')
    ugasichrome(driver)

def test_youtube():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,2000);')
    time.sleep(2)
    a=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div[3]/div/a').get_attribute('href')
    time.sleep(2)
    driver.get(a)
    time.sleep(2)
    assert 'GameS' in driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div/div/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string").text,'pogresan naslov'
    time.sleep(3)
    driver.save_screenshot('screenshot/11.png')
    ugasichrome(driver)

def test_pomoc():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/header/div/div[3]/div/div[2]/div/div/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="accordion"]/div[1]/div[1]/h4/a').click()
    time.sleep(2)

    assert 'NAJČEŠĆA PITANJA' in driver.find_element(By.CLASS_NAME,'heading-wrapper').text, 'pomoc nije pronadjena'
    time.sleep(2)

    driver.save_screenshot('screenshot/12.png')
    ugasichrome(driver)

def test_prodajnamesta():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/header/div/div[3]/div/div[2]/div/div/div[2]').click()
    time.sleep(2)

    driver.execute_script('window.scrollTo(0,100);')
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/a').click()
    time.sleep(2)


    assert 'TC UŠĆE' in driver.find_element(By.CLASS_NAME, 'heading-wrapper').text, 'Prodajno mesto nije nadjeno'
    time.sleep(2)

    driver.save_screenshot('screenshot/13.png')
    ugasichrome(driver)

def test_prijava():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/header/div/div[2]/div/div/div[3]/nav/ul/li[1]/a/span').click()
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="login_modal"]/div/div/form/div[3]/div[1]/a[2]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('vasamailadresa@gmail.com')
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="identifierId"]').clear()
    time.sleep(3)

    assert 'Sign in' in driver.find_element(By.ID,'headingText').text,'Mail nije uspeo'

    driver.save_screenshot('screenshot/14.png')
    ugasichrome(driver)

def test_kolacici():
    driver = pokrenichrome('https://www.games.rs/')
    time.sleep(3)

    driver.find_element(By.XPATH,"//span[contains(text(),'Slažem se')]").click()
    time.sleep(4)

    assert '' in driver.find_element(By.XPATH,'//*[@id="modal-cookie-info"]/div/div/div[1]/div/div[3]/button/span').text,'kolacici nisu prihvaceni'

    driver.save_screenshot('screenshot/15.png')
    ugasichrome(driver)

def ugasichrome(driver):
    driver.minimize_window()
    driver.quit()