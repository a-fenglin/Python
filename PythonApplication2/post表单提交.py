import requests
url="http://111.198.29.45:58509/"
headers={
    #"Upgrade-Insecure-Requests": 1
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
  }
data={
    "disabled":"true"
    }
r=requests.post(url=url,data=data,headers=headers)
print(r.content.decode())
