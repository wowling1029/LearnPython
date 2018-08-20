import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # target = 'http://gitbook.cn'
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(target)
    html = req.text  # 获取网页内容
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt') 
    print(texts[0].text.replace('\xa0'*8,'\n'))
