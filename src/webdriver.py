from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' \
    #              '(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    
    options = webdriver.ChromeOptions()
    # options.add_argument(f'user-agent={user_agent}')
    # options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--user-gesture-required=yes')
    options.add_argument('--autoplay-policy=yes')
    options.add_argument("--user-data-dir=other")
    
    return webdriver.Chrome(
        service = ChromeService(ChromeDriverManager().install()),
        options = options)
