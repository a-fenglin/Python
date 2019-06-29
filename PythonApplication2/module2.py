import requests
data = {'a':1,}
headers = {
     "Content-Type": "text/css",
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

r = requests.get("http://111.198.29.45:51816/", data=data,headers=headers)
print(r.text)

