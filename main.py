# Import Libraries
import requests
import selectorlib
from datetime import datetime

# Scrape Web Page
URL = 'https://programmer100.pythonanywhere.com/'


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['temp']
    return value


# Save Values in txt file

def store(extracted):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open('data.txt', 'a') as file:
        file.write(f"{now},{extracted}\n")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
