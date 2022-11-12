import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=2770005")

# print(res.text["status"])
# print(type(res.text))
json = res.json()
result01 = json["results"][0]
print(result01["address1"])
print(result01["address2"])
print(result01["address3"])
print(result01["prefcode"])
