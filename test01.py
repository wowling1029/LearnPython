from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    # target = 'https://cps.ppdai.com/landinginfo.html?role=1&regsourceid=wxcaimiao'
    target = 'http://test.wdjzt88.com/wap/other/userService/'
    req = requests.get(target)
    html = req.text  # 获取网页内容
    bf = BeautifulSoup(html)
    print(bf)