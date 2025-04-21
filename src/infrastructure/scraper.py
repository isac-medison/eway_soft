import requests
from utils.config_loader import load_config
from selenium import webdriver

config = load_config()

eway_config = config["eway"]
scraper_config = config["scraper"]

def get_cf_clearance():
    driver = webdriver.Chrome()

    url = f"{eway_config['base_url']}/{eway_config['language']}/cities/{eway_config['city']}{eway_config['routes']}"
    driver.get(url)
    
    cf_clearance_value = None
    cookies = driver.get_cookies()
    for cookie in cookies:
        if cookie['name'] == 'cf_clearance':
            cf_clearance_value = cookie['value']
    
    driver.quit()
    return cf_clearance_value


def get_stops_data(cf_clearance_value):
    print("getting stops data")

    session = requests.Session()

    session.headers.update({
        'User-Agent': scraper_config['user_agent'],
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': f"{eway_config['base_url']}/{eway_config['language']}/cities/{eway_config['city']}{eway_config['routes']}"
    })

    session.cookies.set('cf_clearance', cf_clearance_value)
    session.cookies.set('city[key]', eway_config['city'])
    session.cookies.set('lang', eway_config['language'])

    stops_endpoint = f"{eway_config['base_url_ajax']}/{eway_config['language']}/{eway_config['city']}/stops"
    response = session.get(stops_endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch stop data. Status code: {response.status_code}")
