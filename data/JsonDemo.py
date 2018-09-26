import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.32,
    'isShow': True
}

json_str = json.dumps(data)  # 编码json
print(json_str)

json_to_data = json.loads(json_str)  # 解码json
print(json_to_data)
print(json_to_data['name'])  # 通过key获取value
