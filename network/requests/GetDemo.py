import requests

r = requests.get('https://www.baidu.com')

if r.status_code == 200:
    resp_content = 'get baidu : ' + str(r.text)
    print(resp_content)
