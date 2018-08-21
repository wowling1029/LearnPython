from bs4 import BeautifulSoup
import sys , requests

if __name__ == '__main__':
    target = 'https://unsplash.com/'
    req  = requests.get(target)
    texts = req.text
    print(texts)