from django.test import TestCase

# Create your tests here.

import requests
import json

url = "https://open.pkfare.com/apitest/shoppingV2"
data = {
    "authentication": {
        "partnerId": "0oHQALfqyjPlV0hpyUzoQAHQAkE=",
        "sign": "NWIyODQyZDZkODNiNGEwMWU0NTJiZWE0ZmFjYmQxZmQ="
    },
    "search": {
        "adults": 1,
        "airline": "",
        "children": 1,
        "nonstop": 0,
        "searchAirLegs": [
            {
                "cabinClass": "Economy",
                "departureDate": "2020-06-16",
                "destination": "MEL",
                "origin": "HKG"
            }
        ],
        "solutions": 0
    }
}

import base64
import gzip

# 想将字符串转编码成base64,要先将字符串转换成二进制数据
bytes_url = json.dumps(data).encode("utf-8")
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
a = url + "?param=" + str_url.decode()
print(a)
req = requests.get(a)


txt = gzip.decompress(req.content).decode("utf-8")
print(txt)
